#Based on tutorial: using Pandas and Python to explore your dataset
#https://realpython.com/pandas-python-explore-dataset/

import requests  #a Python library for handling HTTP requests

#to find  government datasets go to data.gov; type keywords in the search box; e.g. "Chicago COVID".  From the results you can filter by format to get csv files or JSON files. In the list of datasets, hover over the CSV button, right-click and copy link address which you willpaste into the download_url variable below

# Chicago vaccinations by zip code
download_url = "https://data.cityofchicago.org/api/views/553k-3xzc/rows.csv?accessType=DOWNLOAD"
target_csv_path = "chicago_vac_by_zip.csv"

response = requests.get(download_url)

response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")
