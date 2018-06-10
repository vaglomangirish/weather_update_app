class StorageAgent:
    """
    Interface class for Storage Agent
    """

    def __init__(self):
        pass

    def add_record(self, record):
        raise NotImplementedError

    def get_records(self):
        raise NotImplementedError