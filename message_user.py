
import datetime

class MessageUser:
                def __init__(self):
                        self.user_messages = []
                        self.user_details = []
                        self.base_message = """
Hi {name},
Your bill amounts to {amount}$ on {today.day}/{today.month}/{today.month},
Thanks for purchasing with us.
                        """

                def add_user_detail(self,name,amount):
                        name = name.capitalize()
                        amount = '{0:.2f}'.format(amount)

                        today = datetime.date.today()
                        detail = {"name":name,
                                          "amount":amount,
                                          "today":today
                                          }
                        self.user_details.append(detail)

                def get_user_detail(self):
                        return self.user_details

                def make_messages(self):
                        for detail in self.user_details:
                                name = detail['name']
                                amount = detail['amount']
                                today = detail['today']
                                base_msg = self.base_message
                                new_msg = base_msg.format(name=name,amount=amount,today=today)
                                self.user_messages.append(new_msg)
		

                def get_messages(self):
                        return self.user_messages

names = ['Akhil','Madhuri','Mummy','Daddy','Ram']
amounts = [45.908,23.90,783.090,78.034,890.4564]
obj = MessageUser()

for index in range(min(len(names),len(amounts))):
	name = names[index]
	amount = amounts[index]
	obj.add_user_detail(name,amount)

obj.make_messages()
messages = obj.get_messages()
for msg in messages:
        print(msg)




