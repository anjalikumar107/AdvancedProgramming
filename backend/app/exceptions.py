class appError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class validationError(appError):
    def __init__(self, message: str = "Invalid project input"):
        super().__init__(message, 400)

class ExternalApiError(appError):
    def __init__(self, message: str = "Gerrit project data was not retrieved"):
        super().__init__(message, 502)