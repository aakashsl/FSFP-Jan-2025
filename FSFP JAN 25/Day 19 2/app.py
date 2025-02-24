from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html" ,abc="Car", amt=50)
 
@app.route('/p2')
def product_2():
   name="Computer"
   amt="1000"
   return render_template("index.html", abc=name, amt=amt)

if __name__ == '__main__':
    app.run(debug=True)