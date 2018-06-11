import json, os
import requests


class EmailAgent:
    """
    Class that handles email sending.
    """

    __props_path__ = os.path.join("resources", "properties.json")

    def __init__(self):
        self.properties = {}
        with open(EmailAgent.__props_path__, "r") as props:
            self.properties = json.load(props)

    def send_email(self, email_cont):
        """
        Method that sends an email based on the content passed.
        :param email_cont:
        :return:
        """
        return requests.post(
            self.properties["email_send_api_url"],
            data={"apikey": self.properties["elasticmail_api_key"],
                  "to": [email_cont.to_id],
                  "from": email_cont.from_id ,
                  "fromName": email_cont.from_name,
                  "subject": email_cont.subject,
                  "bodyHtml": email_cont.html
                  })
