#!/bin/sh
# This script uses the Twilio REST APIs to make a prank call
Copy code`# Get your Account Sid and Auth Token from your Account Dashboard at twilio.com/console
ACCOUNT_SID=
AuthToken=
# Get the phone number to call
PhoneNumber=+15551234567`
  `# Create a call request
twilio_call=$(curl -X PATCH --data-urlencode '{ "To"