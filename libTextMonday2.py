import time

contacts = {
  "Baylin": "+18182637135",
  "Cooper": "+16693008800",
  "Leo": "+17147476686",
  "Sean": "+18053907710",
  "Jaden": "+17147173641",
  "Lucas P": "+19292167373",
  "Gabe": "+16199196511",
  "Aymon": "+19252896150",
  "Jack W": "+13102006258",
  "RJ": "+17866576309",
  "Jack P": "+15106041598",
  "TJ": "+15106405517",
  "Nate": "+14156903732",
  "Connor": "+13018017140",
  "Jack G": "+19253501242",
  "Wesley": "+18183195755",
  "James": "+17608894357",
  "Jackson C": "+19494639970",
  "Kevin L": "+13106506587"
}





# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio import rest
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC96e5b95c2407820a9ba77c9d339053b1"
auth_token = "05329830e9f5f2fb74118fc78558335c"
client = Client(account_sid, auth_token)

message1 = client.messages.create(
  body="Kevin has booked the library room. Please approve the email and send a screenshot to Kevin Lavelle at (310) 650-6587. This booking expires in 30 minutes. Text Kevin if the room expired. DO NOT REPLY. Thank you for your help.",
  from_="+18444970019",
  to = contacts['Jack G']
)

message2 = client.messages.create(
  body="Kevin has booked the library room. Please approve the email and send a screenshot to Kevin Lavelle at (310) 650-6587. This booking expires in 30 minutes. Text Kevin if the room expired. DO NOT REPLY. Thank you for your help.",
  from_="+18444970019",
  to = contacts['Cooper']
)

message3 = client.messages.create(
  body="Kevin has booked the library room. Please approve the email and send a screenshot to Kevin Lavelle at (310) 650-6587. This booking expires in 30 minutes. Text Kevin if the room expired. DO NOT REPLY. Thank you for your help.",
  from_="+18444970019",
  to = contacts['Jack P']
)

message4 = client.messages.create(
  body="Kevin has booked the library room. Please approve the email and send a screenshot to Kevin Lavelle at (310) 650-6587. This booking expires in 30 minutes. Text Kevin if the room expired. DO NOT REPLY. Thank you for your help.",
  from_="+18444970019",
  to = contacts['Kevin L']
)



print(message1.sid)
print(message2.sid)
print(message3.sid)
print(message4.sid)