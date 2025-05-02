from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    message_text = data.get('message', '')
    email = data.get('email', '')

    sender_email = "your_email@gmail.com"
    receiver_email = "your_email@gmail.com"
    password = "your_app_password"  # استخدم Gmail App Password

    msg = MIMEText(f"البريد المرسل: {email}\n\nمحتوى الشكوى:\n{message_text}")
    msg['Subject'] = "شكوى جديدة"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print("Email error:", str(e))
        return jsonify({"status": "fail", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
