from src.utils import email_builder


class TestEmailBuilder:
    """
    Test class for email agent.

    run with

    nosetests -v --nocapture test_email_builder.py

    or

    nosetests -v test_email_builder.py

    """

    def __init__(self):
        self.email_build = email_builder.EmailBuilder()

    def test_get_email_content(self):
        """
        Test email content subject based on parameters.
        :return:
        """

        # Test nice weather subject
        email_cont = self.email_build.get_email_content("test@email.com", "Boston,MA", 25, 20, "warm")
        assert email_cont.subject == email_builder.EmailBuilder.__nice_weather_subject__

        # Test bad weather subject
        email_cont = self.email_build.get_email_content("test@email.com", "Boston,MA", 20, 26, "cold")
        assert email_cont.subject == email_builder.EmailBuilder.__not_nice_weather_subject__

        # Test avg weather subject
        email_cont = self.email_build.get_email_content("test@email.com", "Boston,MA", 24, 26, "")
        assert email_cont.subject == email_builder.EmailBuilder.__avg_weather_subject__

        # Test nice weather subject when description is good.
        email_cont = self.email_build.get_email_content("test@email.com", "Boston,MA", 24, 26, "sunny")
        assert email_cont.subject == email_builder.EmailBuilder.__nice_weather_subject__


