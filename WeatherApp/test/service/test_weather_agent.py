import json

from service import weather_agent


class TestWeatherAgent:
    """
    Test class for email agent.

    run with

    nosetests -v --nocapture test_weather_agent.py

    or

    nosetests -v test_weather_agent.py

    """

    def __init__(self):
        pass

    def test_get_weather_by_city(self):
        """
        Test to get weather.
        """

        agent = weather_agent.WeatherAgent()
        # weather_json = agent.get_weather_by_city("Boston,MA")

        # assert weather_json["data"][0]["temp"] is not None

    def test_get_avg_temp_for_city(self):
        """
        Test to get averate temp.
        """

        agent = weather_agent.WeatherAgent()
        # avg_temp = agent.get_avg_temp_for_city("Seatle,WA")

        # assert avg_temp is not None
