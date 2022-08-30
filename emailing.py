import smtplib

from email.message import EmailMessage
from logininfo import EMAIL_ADDRESS, UBC_EMAIL_ADDRESS, EMAIL_PASS

def sendMail(nseats, courseName):
    msg = EmailMessage()
    msg.set_content(f'Hey, you!\n\nThere\'s **{nseats}** people registered in {courseName}')
    msg['Subject'] = f'Registration Alert for {courseName}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = UBC_EMAIL_ADDRESS

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as asdf:
        asdf.login(EMAIL_ADDRESS, EMAIL_PASS)

        asdf.send_message(msg)