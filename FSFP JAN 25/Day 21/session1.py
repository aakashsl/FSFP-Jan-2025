from flask import Flask, session
app = Flask(__name__)

app.secret_key = '956113165'

@app.route('/')
def hello():
   session['name']="Aakash"
   session['Email']="aakash@nediveil.in"
   return 'Hello World!'

@app.route('/get')
def get():
   name = session.get('name')
   email = session.get('Email')
   return name +" "+ email

if __name__ == '__main__':
    app.run(debug=True)