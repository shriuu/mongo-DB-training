from  pymongo import MongoClient
try:
    client=MongoClient('127.0.0.1',27017)
    print('mongodb server connected') 

    db=client['shri']
    collection=db['players']

    query={'player_name':'dhoni'}
    newvalue={"$set":{'player_name':'thanav'}}
    collection.update_one(query,newvalue)

    for i in collection.find():
        print(i)
except:
    print('mongodb server failed')

