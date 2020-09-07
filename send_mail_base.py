
from email.mime.multipart  import MIMEMultipart
from email.mime.text            import MIMEText
from smtplib import SMTP

host = "smtp.gmail.com"
port = 587
username = "ptt.trail.email@gmail.com"
password = "Cognitive@24"

from_email = username
to_email = username

smtp_instance= SMTP(host,port)
smtp_instance.ehlo()
smtp_instance.starttls()
smtp_instance.login(username,password)

message = """Hi Akhil,
You are going to succesful very soon.
Best of luck.
Team ABC
"""

html_txt = """
<html>
    <h1>HTML TeXT</h1>
</html>
"""
plain_txt = "Plain Text:" + message

message = MIMEMultipart("alternative")
message["Subject"] = "Email sender"
message["From"] = username
message["To"] = username

part1 = MIMEText(html_txt,"html")
part2 = MIMEText(plain_txt,"plain")
message.attach(part1)
message.attach(part2)


smtp_instance.sendmail(from_email,to_email,message.as_string())
print("Success")
smtp_instance.quit() # cut the connection
