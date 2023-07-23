from flask import Flask,request
from pymongo import MongoClient

client=MongoClient('127.0.0.1',27017)
db=client['shri']
collection=db['MS']

api=Flask(__name__)

@api.route('/')
def home():
    return('API server is online and it can be called')
@api.route('/message',methods=['GET'])
def message():
    name=request.args.get('name')
    rollno=request.args.get('rollno')
    print(name,rollno)

    K={}
    K['name']=name
    K['rollno']=rollno
    collection.insert_one(K)
    return('successfully inserted into mongodb')

   # return('name is {0}, roll no is {1} ',format(name,rollno))

if(__name__)=="__main__":
    api.run(host='0.0.0.0',port=5001,debug=True)