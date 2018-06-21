class Response:

    def __init__(self, message, status_code=200):
        self.response = status_code
        self.message = message
