import json

with open('./seattle-data.json', 'r') as jsonfile:
    file_data = json.loads(jsonfile.read())
    print("Data for Jan 1, 2018:" + str(file_data["2018-01-01"]))
    