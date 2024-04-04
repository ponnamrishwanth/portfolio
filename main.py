from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

email_address = "ponnamrishwanth78@gmail.com"
email_password ="tmgj axbr eoec acyd"

def send_email(name, email, message):
    try:
        # Set up the SMTP server
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(email_address, email_password)


        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = email_address
        msg['Subject'] = 'New message from your website'

        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.send_message(msg)
        del msg
        server.quit()

        return True
    except Exception as e:
        print("Error:", e)
        return False

@app.route('/')
def index():
    return render_template('about.html')

@app.route("/aboutme")
def aboutme():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("project.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if send_email(name, email, message):
            return render_template('success.html')
        else:
            return render_template('error.html')

    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
