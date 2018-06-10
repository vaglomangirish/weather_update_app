class EmailContent:
    """
    Class that encapsulates email content
    """

    def __init__(self):
        self.from_id = ""
        self.from_name = ""
        self.to_id = ""
        self.subject = ""
        self.html = ""

    def set_from_id(self, from_id):
        self.from_id = from_id

    def set_from_name(self, from_name):
        self.from_name = from_name

    def set_to_id(self, to_id):
        self.to_id = to_id

    def set_subject(self, subject):
        self.subject = subject

    def set_html(self, html):
        self.html = html


