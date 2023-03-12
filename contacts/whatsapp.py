from twilio.rest import Client
import twilio


# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()

export TWILIO_ACCOUNT_SID = 'AC45596b9c017143f070ddd0fec8313ff1'
export TWILIO_AUTH_TOKEN = '9f84820594e9e7012537c980ce0b011e'
# this is the Twilio sandbox testing number
from_whatsapp_number = 'whatsapp:+919414472171'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number = 'whatsapp:+919829530402'

client.messages.create(body='Ahoy, world!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
