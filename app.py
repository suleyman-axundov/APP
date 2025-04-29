from flask import Flask, request
from flask_cors import CORS
from flask_talisman import Talisman
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
CORS(app)
Talisman(app)

GMAIL_USER = 'suleyman.axundov2004@gmail.com'
GMAIL_PASSWORD = 'ldvdfdkbubkffzty'

@app.route('/')
def home():
    return 'Sayt işləyir!'

@app.route('/submit', methods=['POST'])
def submit():
    ad = request.form.get('ad')
    telefon = request.form.get('telefon')
    mesaj = request.form.get('mesaj')

    email_content = f"Yeni müraciət:\n\nAd: {ad}\nTelefon: {telefon}\nMesaj: {mesaj}"

    msg = MIMEText(email_content)
    msg['Subject'] = 'Saytdan Yeni Müraciət'
    msg['From'] = GMAIL_USER
    msg['To'] = GMAIL_USER

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(msg)

    return 'Təşəkkürlər! Mesajınız uğurla göndərildi.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
