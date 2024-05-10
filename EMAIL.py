import smtplib
from email.message import EmailMessage
import imghdr
from time import sleep
email_add = 'harsini20072001@gmail.com'
email_pass = "Grijesh@2004"
msg = EmailMessage()
msg['Subject'] = "Face Mask"
msg['From'] = "harsini20072001@gmail.com"
msg['To'] = "harsini20072001@gmail.com"
msg.set_content("With Out Mask")

def email():
    with open('capture.jpg','rb')as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name) 
    with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
        smtp.login(email_add,email_pass)
        smtp.send_message(msg)
# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")
