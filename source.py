from twilio.rest import Client
import requests


account_sid='your account_sid'
auth_token='your auth_token'


client=Client(account_sid,auth_token)

r=requests.get('http://api.open-notify.org/astros.json');
people=r.json()

number_iss=people['number']

Message = 'Hi Fun fact,Number of people in space right now is '+str(number_iss)

message = client.messages.create(
    to="+91xxxxxxxxxx",
    from_="xxxxxxxxxx",
    body=Message)
print(message.sid)


