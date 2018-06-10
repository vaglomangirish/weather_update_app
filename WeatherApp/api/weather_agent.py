"""
Class for get operations on weather based on city.
"""
import json, __root_path__

from weatherbit.api import Api

class WeatherAgent:

    __props_path__ = __root_path__.path() + "/resources/properties.json"

    def __init__(self):
        self.properties = {}
        with open(WeatherAgent.__props_path__, "r") as props:
            self.properties = json.load(props)

        self.weatherbit_key = self.properties["weatherbit_api_key"]

    def get_weather_by_city(self, city):
        weather_api = Api(self.weatherbit_key)

        current = weather_api.get_current(city=city)
        #print(current.json)

        return current.json


# Main for Test purpose only
def main():
    agent = WeatherAgent()
    agent.get_weather_by_city("Boston,MA")

if __name__ == "__main__":
    main()

