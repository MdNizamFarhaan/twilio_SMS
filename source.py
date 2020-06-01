from twilio.rest import Client
import requests


account_sid='ACedc19b3556fafc9c7d6095c217a6e635'
auth_token='33bea62bc3c2a32cd9fa3f866cdf32ff'


client=Client(account_sid,auth_token)

r=requests.get('http://api.open-notify.org/astros.json');
people=r.json()

number_iss=people['number']

Message = 'Hi Fun fact,Number of people in space right now is '+str(number_iss)

message = client.messages.create(
    to="+918374051298",
    from_="+12074894422",
    body=Message)
print(message.sid)


