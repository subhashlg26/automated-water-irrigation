import smtplib
import base64
import os
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

TO_ADDRESS = os.environ.get('TO_ADDRESS')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_PORT = 80
EMAIL_USE_TLS = False


def email():
    msg = MIMEMultipart()
    msg['From'] = DEFAULT_FROM_EMAIL
    msg['To'] = TO_ADDRESS
    msg['Subject'] = "Watering Status"

    body = "Status of the day"

    fp = open("watering.log", "rb")
    msg.attach(MIMEText(fp.read(), 'plain'))

    filename = "NAME OF THE FILE WITH ITS EXTENSION"
    attachment = open("PATH OF THE FILE", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    base64.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP(EMAIL_HOST)
    server.starttls()
    server.login( EMAIL_HOST_USER, EMAIL_HOST_PASSWORD )
    server.sendmail(DEFAULT_FROM_EMAIL, TO_ADDRESS, msg.as_string())
    server.quit()
