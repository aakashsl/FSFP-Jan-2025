from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'
 
@app.route('/demo')
def Summa():
    return "demo"
 
@app.route('/test')
def test():
    return "Test output here"

@app.route('/html')
def html():
    return "<h1>Hello World</h1> <br> <h2>Nediveil</h2>"

@app.route('/html2')
def html2():
    return ''' <h1>Nediveil</h1>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel consequatur inventore cumque animi dicta illum placeat, soluta, velit blanditiis perferendis eum qui delectus tenetur voluptatibus quas laudantium! Tempora, velit reprehenderit.</p>
<a href="/">Home</a> '''


@app.route('/html3')
def html3():
    return render_template("index.html")

@app.route('/html4')
def html4():
    return render_template("demo.html")

if __name__ == '__main__':
   app.run(debug=True)