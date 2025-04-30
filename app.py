from flask import Flask, request, render_template, redirect, flash
from flask_cors import CORS
from flask_talisman import Talisman
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"
CORS(app)
Talisman(app)

GMAIL_USER = os.environ.get('EMAIL_USER')
GMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

@app.route('/')
def home():
    return render_template('index.html')

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

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.send_message(msg)
        flash("✅ Təşəkkürlər! Mesajınız göndərildi.", "success")
    except Exception as e:
        flash("❌ Xəta baş verdi: " + str(e), "danger")

    return redirect('/')
