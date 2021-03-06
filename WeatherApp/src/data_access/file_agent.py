import json, os

from pathlib import Path

import storage_agent
from utils import app_logger


class FileAgent(storage_agent.StorageAgent):
    """
    File implementation of Storage Agent.

    This agent would store the subscription record in form of a json:-

    {<userid> : [<List of subscribed cities>]}

    """

    # Default static path to the file storing the subscription records
    __default_data_store_path__ = os.path.join("data_store", "store.json")

    def __init__(self):

        self.logger = app_logger.AppLogger().get_logger()

        storage_agent.StorageAgent.__init__(self)
        self.data_store_path = FileAgent.__default_data_store_path__
        self.json_data = {}

        # Checking if the data store file path exists
        store_file = Path(self.data_store_path)

        # Initialize the data store json file if not exists.
        self.logger.info(self.data_store_path)
        if not store_file.is_file():
            with open(self.data_store_path, "w") as store:
                json.dump(self.json_data, store)

            self.logger.info("Initialized empty store file")

    def set_data_store_path(self, path):
        """
        Function sets custom data store path, overriding the default.
        """
        self.data_store_path = path
        self.logger.info("Setting the store file path to {0}".format(path))

    def add_record(self, record):
        """
        Function that adds subscription record
        """
        with open(self.data_store_path, "r") as json_store:
            # FIXME: Performance perspective try to use streams instead of loading whole json in memory every time.
            self.json_data = json.load(json_store)
            self.logger.info("Loaded the current stored data.")

        user_id = record.get_user_id()
        city = record.get_city()

        if not user_id in self.json_data:
            self.json_data[user_id] = [city]
            self.logger.info("Subscribed user with id {0} and city {1}".format(user_id, city))
        else:
            city_list = self.json_data[user_id]
            if not city in city_list:
                city_list.append(city)
                self.logger.info("Added subscription to existing user {0} for city {1}".format(user_id, city))

        # print(self.json_data)
        with open(self.data_store_path, "w") as json_store:
            json.dump(self.json_data, json_store)

    def get_records(self):
        """
        Function to retrieve subscription records stream
        """
        with open(self.data_store_path, "r") as json_store:
            # FIXME: Try to use streams instead of loading whole json in memory.
            self.json_data = json.load(json_store)

            self.logger.info("Retrieved existing data dump")
            return self.json_data
