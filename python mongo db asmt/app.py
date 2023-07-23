from  pymongo import MongoClient
try:
    client=MongoClient('127.0.0.1',27017)
    print('mongodb server connected') 

    db=client['shri']
    collection=db['MS']

  #  name=input('enter name:')
    #rno=input('enter rno: ')

   # k={}
   # k['name']=name
   # k['rno']=rno

   # collection.insert_one(k)

   # query={'name':'vaibu'}
   # newvalue={"$set":{'name':'vaibhavi'}}
    #collection.update_one(query,newvalue)

    query={'name':'laxmi'}
    collection.delete_one(query)
    for i in collection.find():
        print(i)

except:
    print('mongodb server failed')
