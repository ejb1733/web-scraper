import smtplib

from email.message import EmailMessage
from logininfo import EMAIL_ADDRESS, UBC_EMAIL_ADDRESS, EMAIL_PASS

def sendMail(courseName, studentAction, lastnum, nextnum, messageBody):
    msg = EmailMessage()
    msg.set_content(f'Hey, you! Some student(s) have {studentAction} the course, going from {lastnum} to {nextnum}:\n {messageBody}')
    recipients = [EMAIL_ADDRESS, UBC_EMAIL_ADDRESS]
    msg['Subject'] = f'Registration Alert for {courseName}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as asdf:
        asdf.login(EMAIL_ADDRESS, EMAIL_PASS)

        asdf.send_message(msg)