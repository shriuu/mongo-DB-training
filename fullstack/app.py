from flask import Flask

#creating an object
app=Flask(__name__) #app is flask application name
#running the server

@app.route('/')
def home():
    return('server is online')
@app.route('/shri')
def shri():
    return('server is hosted by shri')
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)