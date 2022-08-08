from twilio.rest import Client
import os

# import environmental variables
account_sid = os.environ.get("Account_sid")
auth_token = os.environ.get("Auth_token")
messaging_service_SID = os.environ.get("Messaging_service_SID")
destination_phone_number = os.environ.get("Destination_phone_number")


class TwillioSMS:

    """
        Send message via Twillio API to provided phone number
    """

    def __init__(self, message):

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            messaging_service_sid=messaging_service_SID,
            body=message,
            to=destination_phone_number
        )

  
