"""
Test class for email agent.

run with

nosetests -v --nocapture test_weather_agent.py

or

nosetests -v test_weather_agent.py

"""
import json

from api import weather_agent


class TestWeatherAgent:
    """
    This class tests the weather agent
    """

    def test_send_email(self):
        """
        Test to get weather.
        """

        agent = weather_agent.WeatherAgent()
        #weather_json = agent.get_weather_by_city("Boston,MA")

        #assert weather_json["data"][0]["temp"] is not None