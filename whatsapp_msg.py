# ------------------------------------------------------------------------
# A simple example in Python to automate sending messages in Whatsapp
# Author: SmushBall
# Date: 13/Aug/2020
# ------------------------------------------------------------------------

import os

from twilio.rest import Client 
 
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token) 

def send_msg(): 
	message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello, How are you today?',      
                              to='whatsapp:+918420959349' 
                          ) 
 
	print(message.sid)