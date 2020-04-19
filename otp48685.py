import random
from twilio.rest import Client

otp=random.randint(1000,9999)
print(otp)


account_sid = 'ACc86666f6bbf72b3df0bc9c7ae6bfc6df'
auth_token = '1542b4b2b19df88f8cffa1086c8b5ebd'
client = Client(account_sid, auth_token)

client.messages.create(from_='+19177463326',to='+918220490063',body=str(otp))
