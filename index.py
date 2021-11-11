import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
with open("./target.json", "r") as json_file0:
    config = json.load(json_file0)
with open("./emails.json", "r") as json_file1:
    emails_data = json.load(json_file1)

input('Turn off antivirus before using(press enter to continue) ')
msg = MIMEMultipart()
input("Target is " + config["CONFIG1"]["EMAIL_ADDR"] + " ")
msg['Subject'] = input('Mail subject: ')
message = input('Spam with text: ')
msg.attach(MIMEText(message, 'plain'))
mail_to = config["CONFIG1"]["EMAIL_ADDR"]

i = 0
while i < len(emails_data):
    i += 1
    try:    
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(emails_data["EMAIL_" + str(i)]["EMAIL_LOGIN"], emails_data["EMAIL_" + str(i)]["PASSWRD"])
        server.sendmail(emails_data["EMAIL_" + str(i)]["EMAIL_LOGIN"], mail_to, msg.as_string())
        server.quit()
        print(emails_data["EMAIL_" + str(i)]["EMAIL_LOGIN"] + " ✅")
    except:
        print(emails_data["EMAIL_" + str(i)]["EMAIL_LOGIN"] + " ❌")