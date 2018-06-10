import json, __root_path__

from service import email_content


class EmailBuilder:
    """
    Class that holds methods to build email content.
    """
    __props_path__ = __root_path__.path() + "/resources/properties.json"

    __nice_weather_subject__ = "It's nice out! Enjoy a discount on us."
    __not_nice_weather_subject__ = "Not so nice out? That's okay, enjoy a discount on us."
    __avg_weather_subject__ = "Enjoy a discount on us."

    __bad_weather_keywords__ = ["rain", "snow", "storm", "sleet"]
    __good_weather_keywords__ = ["sunny"]

    def __init__(self):
        self.properties = {}
        with open(EmailBuilder.__props_path__, "r") as props:
            self.properties = json.load(props)

    def get_email_content(self, to, city, current_temp, avg_temp, description):
        """
        Constructs email content with deduced html based on the parameters passed.

        If it's nice outside, either sunny or 5 degrees warmer than the average temperature for that location at that
        time of year, the email's subject should be "It's nice out! Enjoy a discount on us." Or if's it's not so nice
        out, either precipitating or 5 degrees cooler than the average temperature, the subject should be "Not so nice
        out? That's okay, enjoy a discount on us." If the weather doesn't meet either of those conditions, it's an
        average weather day and the email subject should read simply "Enjoy a discount on us."

        :param current_temp:
        :param avg_temp:
        :param description:
        :return: email_content obj.
        """

        email_cont = email_content.EmailContent()
        email_cont.set_from_id(self.properties["email_from_id"])
        email_cont.set_from_name(self.properties["email_from_name"])
        email_cont.set_to_id(to)

        # Subject
        good_weather = False

        for weather in EmailBuilder.__good_weather_keywords__:
            good_weather = weather in description

        # If description is positive and temperature 5 deg. warmer, set nice weather subject.
        if good_weather or (current_temp - avg_temp) >= 5.0:
            email_cont.subject = EmailBuilder.__nice_weather_subject__
        else:
            bad_weather = False

            for weather in EmailBuilder.__bad_weather_keywords__:
                bad_weather = weather in description

            # If description is negative and temperature 5 deg. cooler, set not nice weather subject.
            if bad_weather or (avg_temp - current_temp) >= 5.0:
                email_cont.subject = EmailBuilder.__not_nice_weather_subject__
            else:
                # Set average weather subject otherwise.
                email_cont.subject = EmailBuilder.__avg_weather_subject__

        # HTML Content
        html_content = "<html>" \
            "<head><h2>Weather for " + city + "</h2></head>" \
            "<body>" \
            "<img src=\"http://www.clker.com/cliparts/I/X/3/J/K/a/sunny-weather-ed-md.png\" />" \
            "<p>Weather : " + description + " </p><p>Temperature : " + current_temp + "</p>" \
            "</body>" \
            "</html>"

        email_cont.set_html(html_content)

        return email_cont