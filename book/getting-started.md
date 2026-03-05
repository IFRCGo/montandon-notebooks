(getting-started)=
# Getting Started

:::{admonition} Prerequisites
:class: tip
- Python 3.9+
- Git
- A modern web browser
- An [IFRC GO Platform](https://goadmin-stage.ifrc.org/) account for API access
:::

---

## Run in the Cloud (No Install)

Click any badge below to open a notebook in a live **Binder** or **Google Colab** environment —
all dependencies are pre-installed.

| # | Recipe | Binder | Colab |
|---|--------|--------|-------|
| 01 | Connecting to the STAC API | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IFRCGo/montandon-notebooks/main?urlpath=lab/tree/book/notebooks/01_Getting_Started_Montandon_STAC_API.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IFRCGo/montandon-notebooks/blob/main/book/notebooks/01_Getting_Started_Montandon_STAC_API.ipynb) |
| 02 | Multi-Source Hazard Analysis | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IFRCGo/montandon-notebooks/main?urlpath=lab/tree/book/notebooks/02_Montandon_data_analysis.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IFRCGo/montandon-notebooks/blob/main/book/notebooks/02_Montandon_data_analysis.ipynb) |
| 03 | Time-Series Decomposition | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IFRCGo/montandon-notebooks/main?urlpath=lab/tree/book/notebooks/03_Time_Series_Analysis.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IFRCGo/montandon-notebooks/blob/main/book/notebooks/03_Time_Series_Analysis.ipynb) |
| 04 | Cyclone Track Animation | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IFRCGo/montandon-notebooks/main?urlpath=lab/tree/book/notebooks/04_Recent_Cyclone_Tracking.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IFRCGo/montandon-notebooks/blob/main/book/notebooks/04_Recent_Cyclone_Tracking.ipynb) |
| 05 | Earthquake Cluster Maps | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IFRCGo/montandon-notebooks/main?urlpath=lab/tree/book/notebooks/05_Earthquakes_visualization.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IFRCGo/montandon-notebooks/blob/main/book/notebooks/05_Earthquakes_visualization.ipynb) |
| 06 | Cold-Wave Impact Dashboard | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IFRCGo/montandon-notebooks/main?urlpath=lab/tree/book/notebooks/06_Snow_Cold_Wave_Impact_Analysis.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IFRCGo/montandon-notebooks/blob/main/book/notebooks/06_Snow_Cold_Wave_Impact_Analysis.ipynb) |
| 07 | Cascading-Impact Analysis | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IFRCGo/montandon-notebooks/main?urlpath=lab/tree/book/notebooks/07_cascading_impacts_analysis.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IFRCGo/montandon-notebooks/blob/main/book/notebooks/07_cascading_impacts_analysis.ipynb) |
| 08 | Queryables & CQL2 Reference | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IFRCGo/montandon-notebooks/main?urlpath=lab/tree/book/notebooks/08_Queryables_Deep_Dive.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IFRCGo/montandon-notebooks/blob/main/book/notebooks/08_Queryables_Deep_Dive.ipynb) |
| 09 | EM-DAT People-Impact Mining | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IFRCGo/montandon-notebooks/main?urlpath=lab/tree/book/notebooks/09_EMDAT_Impact_Analysis.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IFRCGo/montandon-notebooks/blob/main/book/notebooks/09_EMDAT_Impact_Analysis.ipynb) |

:::{note}
Binder may take 1–3 minutes to start if the Docker image is not cached.
Once loaded, all dependencies are ready.
:::

---

## Local Setup

## Step 1: Obtain an API Token

:::{important}
The Montandon STAC API requires **Bearer Token** authentication.
You must have a valid token before any data can be retrieved.
:::

### How to Get Your Token

1. Navigate to [goadmin-stage.ifrc.org](https://goadmin-stage.ifrc.org/) and
   click **Sign In**.
2. Go to **Account Settings** → **API Tokens**.
3. Click **Generate New Token**, name it (e.g., *Montandon Cookbook*),
   and copy the value immediately.

:::{warning}
**Never** commit your API token to version control or share it publicly.
Store it in an environment variable or a `.env` file that is listed in
your `.gitignore`.
:::

## Step 2: Set Up Your Environment

### Clone and Install

```bash
git clone https://github.com/IFRCGo/montandon-notebooks.git
cd montandon-notebooks
pip install uv   # one-time setup
uv sync          # resolves and installs all dependencies
```

### Configure Your Token

::::{tab-set}
:::{tab-item} macOS/Linux
```bash
export MONTANDON_API_TOKEN='your_token_here'
```

To make this permanent, add it to your shell profile:
```bash
echo "export MONTANDON_API_TOKEN='your_token_here'" >> ~/.bashrc
# or for zsh users:
echo "export MONTANDON_API_TOKEN='your_token_here'" >> ~/.zshrc
```
:::

:::{tab-item} Windows (PowerShell)
```powershell
$env:MONTANDON_API_TOKEN = "your_token_here"
```

To make this permanent:
```powershell
[System.Environment]::SetEnvironmentVariable('MONTANDON_API_TOKEN', 'your_token_here', 'User')
```
:::

:::{tab-item} Windows (Command Prompt)
```cmd
set MONTANDON_API_TOKEN=your_token_here
```

To make this permanent:
```cmd
setx MONTANDON_API_TOKEN "your_token_here"
```
:::
::::

## Step 3: Launch Jupyter

```bash
uv run jupyter lab
```

Navigate to `book/notebooks/` and open any recipe.

## Step 4: Verify Your Setup

Open **Recipe 1** (`01_Getting_Started_Montandon_STAC_API.ipynb`) and execute
the first three cells. You should see:

- All libraries import without errors
- The `MONTANDON_API_TOKEN` environment variable is detected
- A successful connection message from the STAC API
- Sample items returned from `gdacs-events`

:::{admonition} Pre-Executed Outputs
:class: note
This Jupyter Book ships with cached cell outputs so you can **read results
without running code** or providing a token. To fetch *live* data, run the
notebooks locally or via Binder.
:::

## Troubleshooting

:::{dropdown} {kbd}`ImportError`: No module named `pystac_client`
Run `uv sync` from the repository root to install all pinned dependencies.
:::

:::{dropdown} {kbd}`401 Unauthorized` from the API
Your token may be missing, invalid, or expired.

* Verify the variable is set: `echo $MONTANDON_API_TOKEN`
* Re-generate a token at [goadmin-stage.ifrc.org](https://goadmin-stage.ifrc.org/)
:::

:::{dropdown} Folium maps not rendering in JupyterLab
Ensure JavaScript is enabled and try:
```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```
As a fallback, save the map to HTML: `m.save("map.html")` and open in a
browser.
:::

---

## What's Next?

1. Start with [Recipe 1 — Connecting to the STAC API](notebooks/01_Getting_Started_Montandon_STAC_API)
2. Explore the [Queryables Deep Dive](notebooks/08_Queryables_Deep_Dive) to
   master CQL2 filtering
3. Try modifying queries to analyse your own region or hazard type
4. Build your own visualisations using the helper functions from any recipe