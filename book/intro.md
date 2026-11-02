# Montandon Data Cookbook

:::{admonition} About This Cookbook
:class: important
A hands-on collection of **10 ready-to-run recipes** for querying, analysing, and
visualising disaster data through the IFRC Montandon STAC API — from your first
API call to animated cyclone-track maps and cascading-impact case studies.
:::

---

## What Is Montandon?

**Montandon** is the IFRC's disaster-data platform. It provides a single,
standards-based [SpatioTemporal Asset Catalog (STAC)](https://stacspec.org)
endpoint that aggregates records from multiple authoritative sources
{cite}`stac_spec`.

The platform organises every record into three linked item types:

| Item Type | Description | Example Collections |
|-----------|-------------|---------------------|
| **Event** | A discrete disaster occurrence | `gdacs-events`, `emdat-events`, `glide-events` |
| **Hazard** | Physical parameters of the event | `gdacs-hazards`, `usgs-hazards`, `ibtracs-hazards` |
| **Impact** | Human, economic, and infrastructure consequences | `emdat-impacts`, `idmc-gidd-impacts` |

Items sharing the same `monty:corr_id` (correlation&nbsp;ID) can be joined
across types, enabling event → hazard → impact analysis in a single workflow.

---

## Cookbook at a Glance

::::{grid} 2

:::{grid-item-card} Part I — Foundations
:link: notebooks/01_Getting_Started_Montandon_STAC_API.ipynb
**Recipe 1** Connect, authenticate, and run your first STAC query.
**Recipe 2** Master the Queryables schema and CQL2 filter language.
:::

:::{grid-item-card} Part II — Data Analysis
:link: notebooks/02_Montandon_data_analysis.ipynb
**Recipe 3** Multi-source hazard-code analysis with stacked charts.
**Recipe 4** STL decomposition and Mann–Kendall trend tests.
**Recipe 5** EM-DAT people-impact mining & natural-disaster filtering.
:::

:::{grid-item-card} Part III — Visualization
:link: notebooks/04_Recent_Cyclone_Tracking.ipynb
**Recipe 6** Animated cyclone tracking with Saffir–Simpson colouring.
**Recipe 7** Global earthquake cluster maps with magnitude sizing.
**Recipe 8** Cold-wave impact dashboards with Plotly.
:::

:::{grid-item-card} Part IV — Advanced
:link: notebooks/07_cascading_impacts_analysis.ipynb
**Recipe 9** Cascading-impact analysis: 2023 Türkiye–Syria earthquake,
aftershocks, triggered landslides, and displacement data.
**Recipe 10** Crete flood from satellite imagery: before/after swipe, flood depth,
and the land and buildings under the water.
:::
::::

---

## Quick Start

:::{tip}
To run any recipe **without installing anything**, click the
**Launch Binder** button at the top of each notebook page.
:::

For local development:

```bash
git clone https://github.com/IFRCGo/montandon-notebooks.git
cd montandon-notebooks
pip install uv && uv sync
export MONTANDON_API_TOKEN='<your_token>'   # see Getting Started
uv run jupyter lab
```

Detailed instructions are in [Getting Started](getting-started.md).

---

## Data Sources

::::{tab-set}
:::{tab-item} Events & Hazards
- **GDACS** — Global Disaster Alert and Coordination System {cite}`gdacs`
- **EM-DAT** — Emergency Events Database {cite}`emdat`
- **GLIDE** — Global Identifier for disaster events {cite}`glide`
- **USGS** — U.S. Geological Survey earthquake catalogue {cite}`usgs_earthquake`
- **IBTrACS** — International Best Track Archive for Climate Stewardship {cite}`ibtracs`
- **PDC** — Pacific Disaster Center {cite}`pdc`
- **CEMS** — Copernicus Emergency Management Service rapid mapping {cite}`cems`
:::

:::{tab-item} Impacts
- **EM-DAT** — People, economic, and infrastructure impacts {cite}`emdat`
- **IDMC** — Internal displacement data {cite}`idmc`
- **IFRC** — Red Cross / Red Crescent field reports
- **DesInventar** — National loss databases
:::
::::

---

## Support & Resources

| Resource | Link |
|----------|------|
| Montandon STAC Extension Doc | <https://ifrcgo.org/monty-stac-extension/> |
| Repository | <https://github.com/IFRCGo/montandon-notebooks> |
| Contact | [im@ifrc.org](mailto:im@ifrc.org) |

## License

These examples are provided under the **MIT License**. Data accessed through the
Montandon API is subject to each provider's own licence terms.

---

```{bibliography}
:filter: docname in docnames
```
