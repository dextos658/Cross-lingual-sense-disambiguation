import xml.etree.ElementTree as ET
from pprint import pprint
import csv

USERNAME = 'username'
API_KEY = 'api-key'
base_url = 'https://api.sketchengine.eu/bonito/run.cgi'

mytree = ET.parse('CJVT_Thesaurus-v1.0.xml')

# get root element
root = mytree.getroot()

count = 0
besede = []
# iterate news items
for item in root.findall('./'):
    beseda = ""
    # iterate child elements of item
    for child in item:
        status = str(child).split("\'")[1]

        if (status == "headword"):
            if len(str(child.text).split(" ")) > 1:
                break
            beseda = child.text

        if (status == "groups_core" or status == "groups_near"):
            group = child.getchildren()
            stevilo = len(group)

            if stevilo > 4:
                count = count + 1
                besede.append(beseda)
                break

with open('besede.csv', 'w', newline='', encoding="utf-8") as csvfile:
    fieldnames = ['beseda']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in besede:
        writer.writerow({'beseda': i})

pprint(besede)
print(len(besede))
print(count)