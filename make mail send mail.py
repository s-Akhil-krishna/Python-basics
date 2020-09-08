
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

class MessageUser:
                def __init__(self):
                        self.user_messages = []
                        self.user_details = []
                        self.email_messages = []
                        
                        self.base_message = """
Hi {name},
Your bill amounts to {amount}$ on {date},
Thanks for purchasing with us.
                        """

                def add_user_detail(self,name,amount,email=None):
                        name = name.capitalize()
                        amount = '{0:.2f}'.format(amount)

                        today = datetime.date.today()
                        date = "{today.day}/{today.month}/{today.year}".format(today=today)
                        detail = {"name":name,
                                          "amount":amount,
                                          "date":date
                                          }
                        if  email is not None:
                           detail['email'] = email
                        self.user_details.append(detail)
 
    
                def get_user_detail(self):
                        return self.user_details

                def make_messages(self):
                        for detail in self.user_details:
                                name = detail['name']
                                amount = detail['amount']
                                date = detail['date']
                                base_msg = self.base_message
                                new_msg = base_msg.format(name=name,amount=amount,date=date)
                                email = detail.get("email",None)
                                if email:
                                    user_email = {
                                        "email": email,
                                        "message":new_msg
                                        }
                                    self.email_messages.append(user_email)
                                self.user_messages.append(new_msg)
		
                def get_messages(self):
                        return self.user_messages

                def send_mail(self):
                    if len(self.email_messages) == 0 :return "No messages to send"
                    for detail in self.email_messages:
                            email = detail["email"]
                            message = detail["message"]
                            host = "smtp.gmail.com"
                            port = 587
                            username = "ptt.trail.email@gmail.com"
                            password = "Cognitive@24"
                            smtp_instance = SMTP(host,port)
                            from_email = username
                            to_email = email
                            try:
                                    #setup the connection
                                smtp_instance.ehlo()
                                smtp_instance.starttls()
                                smtp_instance.login(username,password)

                                #create the mail details
                                send_message = MIMEMultipart("alternative")
                                send_message["Subject"]  = "Python mail Sender"
                                send_message["From"] = username
                                send_message["To"] = username
                                text_msg = MIMEText(message,"plain")
                                send_message.attach(text_msg)

                                #Actually send the email
                                smtp_instance.sendmail(from_email,to_email,send_message.as_string())

                                #end the session connection
                                smtp_instance.quit()
                            except:#handle any exception occured in the above process
                               print(email +":An error occured while sending mail")
                    print("Success!!!   All Mails are Sent :)")
                 


names = ['Akhil','Madhuri','Mummy','Daddy','Ram']
amounts = [45.908,23.90,783.090,78.034,890.4564]
emails = ["sirasanagandlaakhil@gmail.com","121015123@sastra.ac.in",None,None,None]
obj = MessageUser()

for index in range(min(len(names),len(amounts))):
	name = names[index]
	amount = amounts[index]
	email = emails[index]
	obj.add_user_detail(name,amount,email)

obj.make_messages()
messages = obj.get_messages()
for msg in messages:
        print(msg)
obj.send_mail()



