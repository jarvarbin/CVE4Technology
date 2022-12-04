# Import the necessary modules
import requests
from bs4 import BeautifulSoup


# Set the technology and version to search for
technology = "nginx"
version = "1.17"

# Set the URL for the NVD website
nvd_url = "https://nvd.nist.gov/vuln/search"

# Set the parameters for the search
params = {
    "adv_search": "true",
    "cpe_version": f"cpe:2.3:a:{technology}:{version}:*",
    "startIndex": 0,
    "resultsPerPage": 50,
}

# Send a GET request to the NVD website
response = requests.get(nvd_url, params=params)

# Parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")

# Get the table with the CVEs
cve_table = soup.find("table", id="vuln-list-table")

# Initialize a list for the CVEs
cves = []

# Iterate over the rows in the table
for row in cve_table.find_all("tr"):
    # Get the columns in the row
    columns = row.find_all("td")

    # Skip rows without enough columns
    if len(columns) < 5:
        continue

    # Get the CVE ID and description
    cve_id = columns[0].text
    description = columns[4].text

    # Append the CVE to the list
    cves.append({"cve_id": cve_id, "description": description})

# Print the CVEs
for cve in cves:
    print(f"{cve['cve_id']}: {cve['description']}")
