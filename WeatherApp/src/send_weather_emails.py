import json, os

from service import weather_agent, email_agent
from utils import app_logger, email_builder


class SendWeatherEmails:
    """
    Class that handles the task of sending weather email updates to subscribers.
    This will be an executable python class that would be executed independently.
    """

    __store_path__ = os.path.join("data_store", "store.json")

    def __init__(self):

        self.email_build = email_builder.EmailBuilder()
        self.weather_agnt = weather_agent.WeatherAgent()
        self.email_agnt = email_agent.EmailAgent()
        self.logger = app_logger.AppLogger().get_logger()

        self.properties = {}
        with open(SendWeatherEmails.__store_path__, "r") as data:
            self.properties = json.load(data)

    def send_weather_updates(self):

        for user_id in self.properties:
            for city in self.properties[user_id]:
                weather_json = self.weather_agnt.get_weather_by_city(city)
                current_temp = weather_json["data"][0]["temp"]
                avg_temp = self.weather_agnt.get_avg_temp_for_city(city)

                description = weather_json["data"][0]["weather"]["description"]

                email_cont = self.email_build.get_email_content(user_id, city, current_temp, avg_temp, description)
                self.logger.info("City: {0} Current Temperature: {1} Average Temperature: {2}"
                                 .format(city, str(current_temp), str(avg_temp)))
                self.email_agnt.send_email(email_cont)
                self.logger.info("Email sent to {0} for city {1}".format(user_id, city))


# Main for Test purpose only
def main():
    svc = SendWeatherEmails()
    svc.send_weather_updates()

if __name__ == "__main__":
    main()