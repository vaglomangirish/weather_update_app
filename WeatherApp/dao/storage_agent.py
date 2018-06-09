"""

Interface class for Storage Agent

"""

class StorageAgent:

    def __init__(self):
        pass

    def add_record(self, record):
        raise NotImplementedError

    def get_records(self):
        raise NotImplementedError