from src.service import email_agent, email_content


class TestEmailAgent:
    """
    Test class for email agent.

    run with

    nosetests -v --nocapture test_email_agent.py

    or

    nosetests -v test_email_agent.py

    """

    def __init__(self):
        pass

    def test_send_email(self):
        """
        Test to send an email.
        """

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

        agent = email_agent.EmailAgent()
        #response = agent.send_email(content)

        #resp_json = json.loads(response.content)

        #assert resp_json["success"] == True
