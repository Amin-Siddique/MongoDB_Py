import requests
import json
import pymongo
from pprint import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
r = requests.get('https://formulae.brew.sh/api/formula.json')

packages_json = r.json()
packages_str = json.dumps(packages_json, indent = 2)

with open("json.txt", "w") as external_file:
    for i in range(1):
        names = json.dumps(packages_json[i], indent = 2)
        print(names, file=external_file)
external_file.close()




# Loading or Opening the json file
with open('json.txt') as dta:
    file = json.load(dta)
    
    #Setting DB & collection:
    mydb = myclient['shop']
    mycollection = mydb["porducts"]
    
    #Checking whether single row to insert or many rows.
    if isinstance(file, list):
        mycollection.insert_many(file)  
        print("insert many")
    else:
        mycollection.insert_one(file)
        print("insert one")

##print out the result
select_find = mycollection.find()
for x in select_find:
    pprint(x)
