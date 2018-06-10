class SubscriptionRecord:
    """
    Class for Subscription record
    """

    def __init__(self, user_id, city):
        self.user_id = user_id
        self.city = city

    def get_user_id(self):
        return self.user_id

    def get_city(self):
        return self.city
