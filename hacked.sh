from twilio.rest import Client
client = Client(account_sid, api_key)
client.calls.create(
   to='+15558675309',
   from_='+17225776229',
   body='Hello there!'
)
