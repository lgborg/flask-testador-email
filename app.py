import os
from flask import Flask
from flask import render_template
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/")
def index():
    msg = Message('PROD Responsivo 19/07, versão antiga', sender='from@example.com', recipients=['to@example.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    msg.html = render_template('newsletter-PROD.html')
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app.run(debug=True)
