import smtplib

from email.message import EmailMessage
from logininfo import EMAIL_ADDRESS, EMAIL_PASS

def sendMail(courseName, studentAction, messageBody):
    msg = EmailMessage()
    msg.set_content(f'Hey, you! Some student(s) has {studentAction}\n {messageBody}')
    msg['Subject'] = f'Registration Alert for {courseName}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as asdf:
        asdf.login(EMAIL_ADDRESS, EMAIL_PASS)

        asdf.send_message(msg)