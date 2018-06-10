"""
File implementation of Storage Agent.

This agent would store the subscription record in form of a json:-

{<userid> : [<List of subscribed cities>]}

"""
import __root_path__
import json

from pathlib import Path

from dao import storage_agent, sub_record
from utils import app_logger


class FileAgent(storage_agent.StorageAgent):

    # Default static path to the file storing the subscription records
    __default_data_store_path__ = __root_path__.path() + "/data_store/store.json"

    def __init__(self):

        self.logger = app_logger.AppLogger().get_logger()

        storage_agent.StorageAgent.__init__(self)
        self.data_store_path = FileAgent.__default_data_store_path__
        self.json_data = {}

        # Checking if the data store file path exists
        store_file = Path(self.data_store_path)

        # Initialize the data store json file if not exists.
        if not store_file.is_file():
            with open(self.data_store_path, "w") as store:
                json.dump(self.json_data, store)

            self.logger.info("Initialized empty store file")

    """
    Function sets custom data store path, overriding the default.
    """
    def set_data_store_path(self, path):
        self.data_store_path = path
        self.logger.info("Setting the store file path to {0}", path)

    """
    Function that adds subscription record
    """
    def add_record(self, record):
        with open(self.data_store_path, "r") as json_store:
            # FIXME: Try to use streams instead of loading whole json in memory.
            self.json_data = json.load(json_store)
            self.logger.info("Loaded the current stored data")

        user_id = record.get_user_id()
        city = record.get_city()

        if not user_id in self.json_data:
            self.json_data[user_id] = [city]
            self.logger.info("Subscribed new user with id")
        else:
            city_list = self.json_data[user_id]
            if not city in city_list:
                city_list.append(city)
                self.logger.info("Added city subscription for {0} to existing user")

        # print(self.json_data)
        with open(self.data_store_path, "w") as json_store:
            json.dump(self.json_data, json_store)

    """
    Function to retrieve subscription records stream
    """
    def get_records(self):
        with open(self.data_store_path, "r") as json_store:
            # FIXME: Try to use streams instead of loading whole json in memory.
            self.json_data = json.load(json_store)

            self.logger.info("Retrieved existing data dump")
            return self.json_data


# Main for Test purpose only
def main():
    agent = FileAgent()
    record = sub_record.SubscriptionRecord("mangirish@abc.com", "Cambridge MA")
    agent.add_record(record)
    record = sub_record.SubscriptionRecord("mangirish@abc.com", "Chicago IL")
    agent.add_record(record)
    record = sub_record.SubscriptionRecord("vaglo@abc.com", "New York NY")
    agent.add_record(record)


if __name__ == "__main__":
    main()



