

from smtplib import SMTP

host = "smtp.gmail.com"
port = 587
username = "<your email address>"
password = "<Your email password>"

from_email = username
to_email = username
message = """Hi ,
You are going to succesful very soon.
Best of luck.
Team ABC
"""

smtp_instance= SMTP(host,port)
smtp_instance.ehlo()
smtp_instance.starttls()
smtp_instance.login(username,password)
smtp_instance.sendmail(from_email,to_email,message)
print("Success")
