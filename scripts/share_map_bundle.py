"""Copy the executed notebook into the site folder, with the lonboard map code moved into one shared file.

Usage: python share_map_bundle.py <executed notebook> <site folder> <tile tag>

lonboard keeps its 4.4 MB JavaScript bundle in the widget state of every Map, and MyST writes the widget state into the
page twice, so five maps add about 48 MB to index.html. In the copy, every Map holds only a small module that imports
the shared file. The notebook passed in is not changed, so it stays re-runnable.

In the cookbook the folder is book/notebooks. Use the tile tag "test" for local builds and "ifrcgo" for the copy that gets
published.
"""
import json
import sys
from pathlib import Path

BUNDLE_FILE = "lonboard_bundle.mjs"        # the Credits section of the notebook links to this file
WIDGET_STATE_MIME = "application/vnd.jupyter.widget-state+json"
# NOTE: widgets run from blob: URLs, which can't import a relative path, and MyST renames the file with a hash when it
# copies it into the site. The link in the Credits is the one place on the page that holds the final address.
BUNDLE_LOADER = """const link = document.querySelector('a[href*="lonboard_bundle"]');
if (!link) throw new Error("The link to lonboard_bundle.mjs is missing from the page, so the maps can't load.");
export default (await import(link.href)).default;
"""
# FIXME: deck.gl's scale widget works out metres per pixel for a 256 px world, but the map's zoom is for a 512 px world,
# so its label reads double the true distance. Remove this once lonboard ships a fix; the assert below flags any change.
SCALE_BUG, SCALE_FIX = "/Math.pow(2,e+8)}function gNt(", "/Math.pow(2,e+9)}function gNt("
# NOTE: titiler.xyz caches each tile with the CORS header of the site that asked first, so a tile first fetched from
# localhost, Binder or Colab is blocked on the live page. titiler ignores the extra parameter, but it gives each tag its
# own cache entries. Remove this once the page has its own TiTiler instance.
TILE_URL_START = "https://titiler.xyz/cog/tiles/"

src_nb, site_dir, tile_tag = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
nb = json.load(open(src_nb, encoding="utf-8"))
models = nb["metadata"]["widgets"][WIDGET_STATE_MIME]["state"].values()
maps = [m["state"] for m in models if "layers" in m["state"] and "_esm" in m["state"]]
bundles = {m["_esm"] for m in maps}
assert len(bundles) == 1, f"expected one lonboard bundle shared by all maps, found {len(bundles)}"
bundle = bundles.pop()
assert bundle.count(SCALE_BUG) == 1, "lonboard's bundle changed: check whether the scale bar patch is still needed"

for m in maps:
    m["_esm"] = BUNDLE_LOADER
tile_layers = [m["state"] for m in models if str(m["state"].get("data", "")).startswith(TILE_URL_START)]
assert tile_layers, "no titiler layers found: check whether TILE_URL_START is still right"
for layer in tile_layers:
    layer["data"] += f"&site={tile_tag}"
bundle_path, nb_path = site_dir / BUNDLE_FILE, site_dir / src_nb.name
with open(bundle_path, "w", encoding="utf-8", newline="") as f:
    f.write(bundle.replace(SCALE_BUG, SCALE_FIX))
with open(nb_path, "w", encoding="utf-8", newline="") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print(f"wrote {nb_path} ({nb_path.stat().st_size / 1e6:.1f} MB) and {bundle_path} ({bundle_path.stat().st_size / 1e6:.1f} MB), shared by {len(maps)} maps, {len(tile_layers)} tile layers tagged site={tile_tag}")
