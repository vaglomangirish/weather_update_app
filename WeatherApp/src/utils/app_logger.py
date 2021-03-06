import logging


class AppLogger:
    """
    Logger handler class for the application
    """

    def __init__(self):
        self.logger = logging.getLogger('WeatherAppLogger')
        self.logger.setLevel(logging.DEBUG)

        # Create file handler
        # file_handler = logging.FileHandler(__root_path__.path() + "/log/app.log")
        # file_handler.setLevel(logging.DEBUG)

        # create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # add the handlers to the logger
        # self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger