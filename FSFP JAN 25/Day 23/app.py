from flask import Flask, render_template

#mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME="nediveiltech@gmail.com"
GMAIL_PASSWORD="zsrs bysa uvyv ehr"


def Send_mail():
   try:
      server=smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
      server.ehlo()
      server.starttls()
      server.login(GMAIL_USERNAME,GMAIL_PASSWORD)
      msg = MIMEMultipart()
      msg['From'] = "Aakash SL"
      msg['To'] = "slaakash06@gmail.com"
      msg['Subject'] = "Test mail"
      body = "Hello,\n\nThis is a test mail."
      msg.attach(MIMEText(body,'plain'))
      server.sendmail(GMAIL_USERNAME,"slaakash06@gmail.com",msg.as_string())
      server.close()
      print("Mail sent successfully")
   except Exception as e:
      return "Something Went wrong"
   

def Send_mail_html():
   server=smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
   server.ehlo()
   server.starttls()
   server.login(GMAIL_USERNAME,GMAIL_PASSWORD)
   msg = MIMEMultipart()
   msg['From'] = "Aakash SL"
   msg['To'] = "slaakash06@gmail.com"
   msg['Subject'] = "Test mail"
   html = render_template("mail.html")
   msg.attach(MIMEText(html,'html'))
   server.sendmail(GMAIL_USERNAME,"slaakash06@gmail.com",msg.as_string())
   server.close()
    
   
@app.route('/')
def hello():
    return 'Hello World!'
 
 
@app.route('/send')
def send():
   abc=Send_mail()
   return abc

@app.route('/html')
def html():
   Send_mail_html()
   return "Done"
 

if __name__ == '__main__':
    app.run(debug=True)