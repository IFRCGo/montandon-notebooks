# Montandon Data Fetching Examples

Example notebooks demonstrating usage of the Montandon API / STAC data catalog.

## Authentication Required

The Montandon STAC API staging environment now requires authentication using a Bearer Token from the IFRC OpenID Connect system.

**API Endpoint:** https://montandon-eoapi-stage.ifrc.org/

**To get your API token:**

1. Visit: https://goadmin-stage.ifrc.org/
2. Log in with your IFRC credentials
3. Navigate to your account settings to generate an API token
4. When running notebooks, you'll be prompted to enter your token securely

**Setting token as environment variable (optional):**

```bash
# PowerShell
$env:MONTANDON_API_TOKEN = "your_token_here"

# Bash/Linux
export MONTANDON_API_TOKEN="your_token_here"
```

## Run in Binder

Click to open the notebooks in an interactive environment:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/arunissun/Montandon-Data-Fetching-Examples/HEAD)

**Notes:**

- When using Binder, you'll need to provide your own API token when prompted in the notebooks.
- First build may take 5-10 minutes. Subsequent launches use cached builds and start in ~1-2 minutes.
- Environment configuration is in `.binder/` directory for optimized caching.

## Run in Google Colab

You can run any notebook directly in Google Colab:

1. **Open a notebook in Colab:**

   - Navigate to the notebook in the `montandon_notebooks/` folder on GitHub
   - Click the "Open in Colab" badge, or
   - Use this URL pattern: `https://colab.research.google.com/github/arunissun/Montandon-Data-Fetching-Examples/blob/master/montandon_notebooks/<notebook_name>.ipynb`

2. **Install dependencies first:** Add and run this cell at the top of the notebook:

   ```python
   # Install required packages for Google Colab
   !pip install -q pystac-client pandas folium matplotlib seaborn plotly statsmodels pymannkendall geopandas shapely requests ipywidgets
   ```

3. **Set your API token:** Add this cell before running the notebook:

   ```python
   import os
   from getpass import getpass

   # Set your Montandon API token
   os.environ['MONTANDON_API_TOKEN'] = getpass('Enter your Montandon API token: ')
   ```

**Quick Links to Notebooks:**

| Notebook                       | Open in Colab                                                                                                                                                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01 - Getting Started           | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arunissun/Montandon-Data-Fetching-Examples/blob/master/montandon_notebooks/01_Getting_Started_Montandon_STAC_API.ipynb) |
| 02 - Data Analysis             | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arunissun/Montandon-Data-Fetching-Examples/blob/master/montandon_notebooks/02_Montandon_data_analysis.ipynb)            |
| 03 - Time Series Analysis      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arunissun/Montandon-Data-Fetching-Examples/blob/master/montandon_notebooks/03_Time_Series_Analysis.ipynb)               |
| 04 - Cyclone Tracking          | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arunissun/Montandon-Data-Fetching-Examples/blob/master/montandon_notebooks/04_Recent_Cyclone_Tracking.ipynb)            |
| 05 - Earthquakes Visualization | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arunissun/Montandon-Data-Fetching-Examples/blob/master/montandon_notebooks/05_Earthquakes_visualization.ipynb)          |
| 06 - Snow/Cold Wave Analysis   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arunissun/Montandon-Data-Fetching-Examples/blob/master/montandon_notebooks/06_Snow_Cold_Wave_Impact_Analysis.ipynb)     |
| 07 - Cascading Impacts         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arunissun/Montandon-Data-Fetching-Examples/blob/master/montandon_notebooks/07_cascading_impacts_analysis.ipynb)         |
| 08 - Queryables Deep Dive      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arunissun/Montandon-Data-Fetching-Examples/blob/master/montandon_notebooks/08_Queryables_Deep_Dive.ipynb)               |
| 09 - EM-DAT Impact Analysis    | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arunissun/Montandon-Data-Fetching-Examples/blob/master/montandon_notebooks/09_EMDAT_Impact_Analysis.ipynb)               |
| 10 - Crete Flood Imagery       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IFRCGo/montandon-notebooks/blob/main/book/notebooks/10_CEMS_Flood_Satellite_Imagery.ipynb) |

## Run Locally

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Option 1: Using uv (Recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/arunissun/Montandon-Data-Fetching-Examples.git
cd Montandon-Data-Fetching-Examples

# Install dependencies and run JupyterLab
uv sync
uv run jupyter lab
```

### Option 2: Using pip

```bash
# Clone the repository
git clone https://github.com/arunissun/Montandon-Data-Fetching-Examples.git
cd Montandon-Data-Fetching-Examples

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run JupyterLab
jupyter lab
```

### Set API Token as Environment Variable

**PowerShell (Windows):**

```powershell
$env:MONTANDON_API_TOKEN = "your_token_here"
```

**Bash/Linux/Mac:**

```bash
export MONTANDON_API_TOKEN="your_token_here"
```

## Notebooks

All notebooks are located in the `montandon_notebooks/` folder:

| #   | Notebook                                      | Description                                                     | Key Packages                                      |
| --- | --------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------- |
| 01  | `01_Getting_Started_Montandon_STAC_API.ipynb` | Introduction to the Montandon STAC API and basic data retrieval | pystac-client, pandas, matplotlib, seaborn        |
| 02  | `02_Montandon_data_analysis.ipynb`            | Data analysis and interactive map visualization                 | pystac-client, pandas, folium, matplotlib         |
| 03  | `03_Time_Series_Analysis.ipynb`               | Time series analysis with parallel processing                   | pystac-client, statsmodels, pymannkendall, pandas |
| 04  | `04_Recent_Cyclone_Tracking.ipynb`            | Tracking recent cyclone events                                  | pystac-client, pystac, folium, pandas             |
| 05  | `05_Earthquakes_visualization.ipynb`          | Interactive earthquake visualization                            | pystac-client, folium, ipywidgets, pandas         |
| 06  | `06_Snow_Cold_Wave_Impact_Analysis.ipynb`     | Winter hazard impact analysis                                   | pystac-client, plotly, pandas, seaborn            |
| 07  | `07_cascading_impacts_analysis.ipynb`         | Cascading disaster impact analysis                              | pystac-client, geopandas, folium, pandas          |
| 08  | `08_Queryables_Deep_Dive.ipynb`               | Deep dive into STAC API queryables and CQL2 filtering           | pystac-client, requests, plotly, pandas           |
| 09  | `09_EMDAT_Impact_Analysis.ipynb`              | EM-DAT people impact analysis with memory-optimized CSV export  | pystac-client, csv, pandas                        |
| 10  | `book/notebooks/10_CEMS_Flood_Satellite_Imagery.ipynb` | Crete flood from satellite imagery: extent, depth, land and buildings | pystac-client, rasterio, lonboard, manywidgets |

## Data Sources

The Montandon STAC API aggregates disaster and hazard data from multiple sources:

- **GDACS** - Global Disaster Alert and Coordination System
- **EM-DAT** - Emergency Events Database
- **GLIDE** - Global Library of Insurance Disaster Events
- **DesInventar** - Disaster Inventory System
- **GFD** - Geospatial Facility Database
- **IBTRACS** - International Best Track Archive for Climate Stewardship
- **IDMC** - Internal Displacement Monitoring Centre
- **IFRCEVENT** - IFRC Event Database
- **UNDRR-ISC** - UN Disaster Risk Reduction Registry
- **CEMS** - Copernicus Emergency Management Service
