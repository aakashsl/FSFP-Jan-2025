from flask import Flask, jsonify

import firebase_admin
from firebase_admin import db

app = Flask(__name__)

cred = firebase_admin.credentials.Certificate("serviceAccountKey2.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-1ef0d-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


ref = db.reference('/')

@app.route('/')
def hello():
    return 'Hello World!'
 
@app.route('/add/<name>')
def add(name):
      user_ref = ref.child('demo').push({
        'name': name,})
      return "Done"
   
@app.route('/get')
def get():
   users = ref.child('users').get()
   return jsonify(users)

@app.route('/delete')
def delete():
   ref.child('users').delete()
   return "Done"
    
    
if __name__ == '__main__':
    app.run(debug=True)