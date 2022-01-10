import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#To get database list:
print("List of Database : {}".format(myclient.list_database_names()))

#To get collection/table in database
dblist = myclient.list_database_names()
for i in dblist:
    collectionlist = myclient[i].list_collection_names()
    print("Collection in database {} is : {}".format(i,collectionlist))

    
##To insert in specified collection in DB:
mydb = myclient['shop']
mycollection = mydb["porducts"]
mydict = { "name": "Amina", "address": "Kolkata","Age":"45" }
insrt_dta = mycollection.insert_one(mydict)
print(insrt_dta.inserted_id)


#Select * from collection with result sorted in descending:
where = { "age": { "$gt": 15 }}
select_find = mycollection.find(where).sort("age",-1)   #<--- remove where to get full result set
for x in select_find:
    print(x)
#print(select_find)

#To delete items from collection:
Delete item from collection:
item = {"name" : "azhar"}
dlt_items = mycollection.delete_one(item)   #mycollection.delete_many(item) <-- To delete many items
print(dlt_items.deleted_count, " documents deleted.")

# print("List of Database : {}".format(myclient.list_database_names()))
# print("List of Collection : {}".format(myclient['shop'].list_collection_names()))


