import csv
import json

fieldnames = (
    "STATION","NAME","DATE","AWND","PRCP","SNOW","SNWD",
    "TAVG","TMAX","TMIN","WT01","WT02","WT03","WT05","WT08"
)

with open('./seattle-data.csv', 'r') as csvfile:
    with open('./seattle-data.json', 'w') as jsonfile:
        # The above just means we close the files automatically after these 
        # with blocks end and we're done writing and reading the files
        next(csvfile)
        reader = csv.DictReader(csvfile, fieldnames)
        final_data = {}
        for row in reader:
            print(row)
            print(type(row))
            final_data[row["DATE"]] = {
                "STATION": row["STATION"],
                "NAME": row["NAME"],
                "DATE": row["DATE"],
                "AWND": row["AWND"],
                "PRCP": row["PRCP"],
                "SNOW": row["SNOW"],
                "SNWD": row["SNWD"],
                "TAVG": row["TAVG"],
                "TMAX": row["TMAX"],
                "TMIN": row["TMIN"]
            }
        json.dump(final_data, jsonfile)
        jsonfile.write('\n')
