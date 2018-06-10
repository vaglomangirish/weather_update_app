"""
Test class for file agent.

run with

nosetests -v --nocapture test_file_agent.py

or

nosetests -v test_file_agent.py

"""

import os

from dao import file_agent, sub_record


class TestFileAgent:
    """
    This class tests the email agent
    """

    def test_add_record(self):
        """
        Test to send an email.
        """

        agent = file_agent.FileAgent()
        record = sub_record.SubscriptionRecord("mangirish@abc.com", "Cambridge MA")
        agent.add_record(record)
        record = sub_record.SubscriptionRecord("mangirish@abc.com", "Chicago IL")
        agent.add_record(record)
        record = sub_record.SubscriptionRecord("vaglo@abc.com", "New York NY")
        agent.add_record(record)

        assert os.path.isfile(agent.data_store_path)


    def test_get_records(self):
        """
        Test get records.
        """
        agent = file_agent.FileAgent()

        record = sub_record.SubscriptionRecord("mangirish@abc.com", "Cambridge MA")
        agent.add_record(record)

        records = agent.get_records()

        assert len(records) > 0
