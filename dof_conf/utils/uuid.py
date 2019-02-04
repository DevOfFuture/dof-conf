from uuid import uuid4
from base64 import urlsafe_b64encode


def uuid():
    """
    Returns an URL safe encoded UUID string.
    """
    return urlsafe_b64encode(uuid4().bytes).decode("ascii").rstrip("=")
