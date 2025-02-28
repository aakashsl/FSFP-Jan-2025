from flask import Flask, render_template, request, redirect,url_for
app = Flask(__name__)


Emails=['slaakash06@gmail.com', 'info@nediveil.in']
passwords='123456'

@app.route('/')
def hello():
   value=request.cookies.get('abc')
   if value in ['1d6fh98df2h651', '51cg6hxf1h65xf1hf']:
      return redirect(url_for('dashboard'))
   return 'Hello World!'
 
@app.route('/login')
def login():
   value=request.cookies.get('abc')
   if value in ['1d6fh98df2h651', '51cg6hxf1h65xf1hf']:
      return redirect(url_for('dashboard'))
   return render_template("login.html")

@app.route('/dashboard')
def dashboard():
   value=request.cookies.get('abc')
   if value not in ['1d6fh98df2h651', '51cg6hxf1h65xf1hf']:
      return redirect(url_for('login'))
   return render_template("dashboard.html")

@app.route('/verify', methods=['post'])
def verify():
   email=request.form['email']
   password=request.form['password']
   name=""
   cookies=""
   if email in Emails:
      if password==passwords:
         if email==Emails[0]:
            name="Aakash"
            cookies="1d6fh98df2h651"
         else:
            name="Nediveil"
            cookies="51cg6hxf1h65xf1hf"
         resp = redirect(url_for('dashboard'))
         resp.set_cookie('abc', cookies, max_age=3600)
         return resp
      return "Wrong Password"
   return "Wrong Email"
            
      
            

if __name__ == '__main__':
    app.run(debug=True)