"""
Class that handles email sending.

"""

import requests, json, os, sys, __root_path__

from api import email_content


class EmailAgent:

    __props_path__ = __root_path__.path() + "/resources/properties.json"

    def __init__(self):
        self.properties = {}
        with open(EmailAgent.__props_path__, "r") as props:
            self.properties = json.load(props)

    def send_email(self, email_content):
        return requests.post(
            self.properties["email_send_api_url"],
            data={"apikey": self.properties["elasticmail_api_key"],
                  "to": [email_content.to_id],
                  "from": email_content.from_id ,
                  "fromName": email_content.from_name,
                  "subject": email_content.subject,
                  "bodyHtml": email_content.html
                  })
