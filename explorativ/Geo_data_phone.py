import os
from twilio.rest import Client

# Set up the Twilio client
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Set up the phone number to look up
phone_number = '+1234567890'

# Make a request to the Twilio API to get the geolocation
response = client.lookups.v1.phone_numbers(phone_number).fetch()

# Print the geolocation information
print(f"The geolocation of {phone_number} is: {response.carrier.name}, {response.country}, {response.region}, {response.city}")