import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

csv_file = "jarvis/contacts.csv"
contact_list = pd.read_csv(csv_file)


def send_email(to,subject, title, messagetext,name="Siddharth Mohanakrishnan"):
    message = MIMEMultipart()
    message["To"] = to
    message["From"] = name
    message["Subject"] = subject

    title = f'<b> {title} </b>'
    messageText = MIMEText(f'''{messagetext}''', 'html')
    message.attach(messageText)

    email = 'siddharthmohanakrishnan@gmail.com'
    password = 'lbcu kiqu djga bhqt'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo('Gmail')
    server.starttls()
    server.login(email, password)
    fromaddr = 'siddharthmohanakrishnan@gmail.com'
    toaddrs = 'pranavkakula985@gmail.com'
    server.sendmail(fromaddr, toaddrs, message.as_string())

    server.quit()

# name = input("Enter the name of the person: ")
# to = phone_number = contact_list.loc[contact_list['Name'] == name, 'Email'].values[0]
# subject = input("Enter the subject of the email: ")
# title = input("Enter the title of the email: ")
# messagetext = input("Enter the message of the email: ")
# send_email(to, name, subject, title, messagetext)