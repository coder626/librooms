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
  "Vedant": "+18182648740",
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
  body="This is Kevin Lavelle, I am sending this message through an automated system. In 30 minutes at around 12:00 am, you will receive an email with a library room booking. Please approve this email and send Kevin a screenshot with the booking at (310) 650-6587. You will receive a second text when you should check your Gmail. DO NOT REPLY. Thank you.",
  from_="+18444970019",
  to = contacts['Jack G']
)


message4 = client.messages.create(
  body="This is Kevin Lavelle, I am sending this message through an automated system. In 30 minutes at around 12:00 am, you will receive an email with a library room booking. Please approve this email and send Kevin a screenshot with the booking at (310) 650-6587. You will receive a second text when you should check your Gmail. DO NOT REPLY. Thank you.",
  from_="+18444970019",
  to = contacts['Kevin L']
)

print(message1.sid)
#print(message2.sid)
#print(message3.sid)
print(message4.sid)