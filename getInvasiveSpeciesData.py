#Based on tutorial: using Pandas and Python to explore your dataset
#https://realpython.com/pandas-python-explore-dataset/

import requests

# to get government datasets go to data.gov; type keywords in the search box; e.g. "invasive species" from the results you can filter by format to get csv files. In the list of datasets, hover over the CSV button, right-click and copy link address

#US Invasive species
''' download_url = "https://data.nal.usda.gov/system/files/Espeland-Sylvain-BiodivConserv-2019-raw-data.csv"
target_csv_path = "usgov_BioDivConserv_species.csv" '''

#invasive mussels in California
download_url = "https://data-cdfw.opendata.arcgis.com/datasets/7a0ed3fc34cd4ce688832c32f90ae2c3_0.csv"
target_csv_path = "cal_mussels.csv"

response = requests.get(download_url)

response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")
