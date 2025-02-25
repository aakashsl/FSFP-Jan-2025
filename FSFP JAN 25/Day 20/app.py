from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
 
@app.route('/demo')
def demo():
    return "Demo"


@app.route('/demo/hello/')
def test():
    return " Hello"

@app.route('/test/<n>')
def value(n):
    return n

@app.route('/login')
def login():
    return render_template("index.html")

@app.route('/verify_login' , methods=['post'])
def verify_login():
    email=request.form["email"]
    pas=request.form['password']
    if email == 'slaakash06@gmail.com' and pas == "12345":
        return "Login Successfull"
    return "Either Email or Password Wrong"


@app.route('/api')
def api():
    return jsonify({"message":"This is API"})

@app.route('/test_ajax')
def ajax():
    return render_template("ajax.html")

@app.route('/demo_ajax' , methods=['post'])
def demo_ajax():
    name = request.form['name']
    if name=="Aakash":
        return jsonify({"message":"Hello Aakash"})
    return jsonify({"message":"Hello Stranger"})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")