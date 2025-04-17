import smtplib
from email.mime.text import MIMEText
smtp_server = "smtp.gmail.com"
port= 587
sender_email="pavanvaranasi95@gmail.com"
receiver_mail="radha.medavarapu193@gmail.com"
message="Jagannadh saying I love you to Radha using Python script"

msg= MIMEText(message)
msg['Subject']="Automated mail using Python"
msg['From']=sender_email
msg['To']=receiver_mail

with smtplib.SMTP(smtp_server,port) as server:
    server.starttls()
    password=input("Please enter your gmail app password")
    #avss vroo uzrn ohwa
    server.login(sender_email, password)
    server.sendmail(sender_email, [receiver_mail], msg.as_string())