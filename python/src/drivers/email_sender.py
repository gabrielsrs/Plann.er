import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "p66kkjbwsoafohuw@ethereal.email"
    login = "p66kkjbwsoafohuw@ethereal.email"
    password = "yMqapYwRsxbs7HadqN"

    msg = MIMEMultipart()
    msg["from"] = "confirm@mail.com"
    msg["to"] = ', '.join(to_addrs)

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)

    server.starttls()
    server.login(login, password)
    
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    
    server.quit()