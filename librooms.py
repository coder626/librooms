#!/usr/bin/python3
#import selenium
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains
#import mysql.connector
#from mysql.connector.constants import ClientFlag
#import tkinter as tk
#from tkinter import *
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
  "Kevin L": "+13106506587",
  "Ben" : "+18318012575"
}





# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio import rest
from twilio.rest import Client

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('pnm.csv')

# Function to reformat phone numbers
def reformat_phone(phone):
    # Remove any non-numeric characters from the phone number
    numeric_phone = ''.join(filter(str.isdigit, str(phone)))
    
    # Add "+1" prefix to the numeric phone number
    formatted_phone = "+1" + numeric_phone
    
    return formatted_phone

# Create a list of pairs (name, reformatted phone number)
pairs_list = [(row['Firstname'] + ' ' + row['Lastname'], reformat_phone(row['Phone'])) for _, row in df.iterrows()]

for pair in pairs_list:
    print(pair)
"""
# Save the list to a new CSV file
with open('pairs.csv', 'w') as f:
    for pair in pairs_list:
        f.write(f"{pair[0]},{pair[1]}\n")
"""


# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC96e5b95c2407820a9ba77c9d339053b1"
auth_token = "05329830e9f5f2fb74118fc78558335c"
client = Client(account_sid, auth_token)

pairs_list_test = [
    ('Jack', '+15106041'),
    ('RJ', '+17866576309'),
    ('Leland', '+14155900533'),
    ('Kevin', '+13106506587')
]

pairs_list_test_2 = [
    ('Bailey Theisen', '+18057123071')
]

for name, phone_number in pairs_list_test_2:
    # Compose your message here
    message_body = f"Hi {name}, this is Leland, the President of Delta Tau Delta. Sorry for the late notice, there have been some technical difficulties with invites today. I wanted to let you know I am extending an invitation for you to come out tonight to our house at 6515 Pardall Rd anytime before 9pm. Hope to see you there. Feel free to text me at (415) 590-0533 with any questions. This is an automated message and you will not receive any more. Do not Reply."
    
    try:
        # Send the message using Twilio
        message = client.messages.create(
            body=message_body,
            from_="+18444970019",
            to=phone_number
        )
        
        # Print confirmation
        print(f"Message sent to {name} at {phone_number}: {message.sid}")
    
    except Exception as e:
        # Handle the exception (e.g., print an error message)
        print(f"Error sending message to {name} at {phone_number}: {str(e)}")









"""

for name, phone_number in pairs_list_test:

  

  message = client.messages.create(
    
    body="Hi " + name + ", this is Leland, the President of Delta Tau Delta. Sorry for the late notice, there have been some technical difficulties with invites today. I wanted to let you know I am extending an invitation for you to come out tonight to our house at 6515 Pardall Rd anytime before 9pm. Hope to see you there. Feel free to text me at (415) 590-0533 with any questions. This is an automated message and you will not receive any more. Do not Reply.",
    from_="+18444970019",
    to = phone_number
  )

  print(message.sid)
"""


"""

message1 = client.messages.create(
  body="This is Kevin Lavelle, I am sending this message through an automated system. In 30 minutes at around 12:00 am, you will receive an email with a library room booking. Please approve this email and send Kevin a screenshot with the booking at (310) 650-6587. DO NOT REPLY. Thank you.",
  from_="+18444970019",
  to = contacts['Kevin L']
)

message2 = client.messages.create(
  body="This is Kevin Lavelle, I am sending this message through an automated system. In 30 minutes at around 12:00 am, you will receive an email with a library room booking. Please approve this email and send Kevin a screenshot with the booking at (310) 650-6587. DO NOT REPLY. Thank you.",
  from_="+18444970019",
  to = contacts['Kevin L']
)

message3 = client.messages.create(
  body="This is Kevin Lavelle, I am sending this message through an automated system. In 30 minutes at around 12:00 am, you will receive an email with a library room booking. Please approve this email and send Kevin a screenshot with the booking at (310) 650-6587. DO NOT REPLY. Thank you.",
  from_="+18444970019",
  to = contacts['Kevin L']
)

message4 = client.messages.create(
  body="This is Kevin Lavelle, I am sending this message through an automated system. In 30 minutes at around 12:00 am, you will receive an email with a library room booking. Please approve this email and send Kevin a screenshot with the booking at (310) 650-6587. DO NOT REPLY. Thank you.",
  from_="+18444970019",
  to = contacts['Kevin L']
)

print(message1.sid)
print(message2.sid)
print(message3.sid)
print(message4.sid)

"""



"""

print('HELLO WORLD')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://libcal.library.ucsb.edu/booking/24hour")

dateScroll = driver.find_element(By.CLASS_NAME, 'ui-datepicker-month')

selectMonth = Select(dateScroll)

selectMonth.select_by_visible_text("Feb")

dateButton = driver.find_element(By.XPATH, '//*[@id="s-lc-rm-cal"]/div/table/tbody/tr[2]/td[5]/a')

dateButton.click()










time.sleep(4)
driver.close()

"""

#Select se = new Select(driver.find_element(By.CLASS_NAME, 'ui-datepicker-month'))

#se.selectByIndex(1)


"""

#creates the webdriver
driver = webdriver.Chrome(executable_path='/Users/edwardlavelle/Downloads/chromedriver')

#NOTE: Chromedriver now works!!!!



#go to CMU website
driver.get("https://academy.cs.cmu.edu/login")

#maximize the window and wait so everything can be formatted into the screen
driver.maximize_window()
time.sleep(3)

#find the username and password elements by HTML ID
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

#send the keys 
username.send_keys("coder626")
password.send_keys("Password1")

"""
