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


# Main for Test purpose only
def main():

    print(os.path.dirname(sys.modules['__main__'].__file__))

    from_id = "funday@weatherapp.com"
    from_name = "FunDay Weather App"
    to_id = "vaglomangirish@gmail.com"
    subject = "Test Email"
    html_content = "<p>This is a test email.</p>"

    content = email_content.EmailContent()
    content.set_from_id(from_id)
    content.set_from_name(from_name)
    content.set_to_id(to_id)
    content.set_subject(subject)
    content.set_html(html_content)

    agent = EmailAgent()
    response = agent.send_email(content)

    print(response.content)

    respjson = json.loads(response)

    #print(respjson["success"])

    #assert response["success"] == True


if __name__ == "__main__":
    main()