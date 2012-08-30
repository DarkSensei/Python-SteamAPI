class HttpForbidden(Exception):
    def __init__(self, msg):
        Exception.__init__(msg)

class HttpTimeout(Exception):
    def __init__(self, msg):
        Exception.__init__(msg)

