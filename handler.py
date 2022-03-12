import os


def hello(event, context):
    return os.environ.get("FIRST_NAME")

