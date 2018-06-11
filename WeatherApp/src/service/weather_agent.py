import datetime
import json, os

from weatherbit.api import Api


class WeatherAgent:
    """
    Class for get operations on weather based on city.
    """

    __props_path__ = os.path.join("resources", "properties.json")

    def __init__(self):
        self.properties = {}
        with open(WeatherAgent.__props_path__, "r") as props:
            self.properties = json.load(props)

        self.weatherbit_key = self.properties["weatherbit_api_key"]
        self.weather_api = Api(self.weatherbit_key)

    def get_weather_by_city(self, city):
        """
        Get the current weather details for a city.
        :param city:
        :return: Weather json
        """

        current = self.weather_api.get_current(city=city)
        #print(current.json)

        return current.json

    def get_avg_temp_for_city(self, city):
        """
        Function that returns the average temperature for city provided.
        :param city: <City>,<State> e.g. Boston,MA
        :return: Temperature in Celcius
        """
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(1)

        # Converting to the eventually expected formatted string to bypass date.hour check.
        # 'hour' somehow is not a part of the 'datetime.date'
        end_date = end_date.strftime('%Y-%m-%d:%H')
        start_date = start_date.strftime('%Y-%m-%d:%H')

        history = self.weather_api.get_history(city=city, start_date=start_date, end_date=end_date)

        history_json = history.json

        # Getting average from all sources.
        sum = 0
        for data_item in history_json["data"]:
            sum += data_item["temp"]

        avg = sum / len(history_json["data"])

        return avg
