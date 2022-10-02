import os
import requests

BASE_URL = "http:/httpbin.org/"

def example1():
    """
    Retrieve the current directory

    Returns:
        Current directory
    """
    current_path = os.getcwd()
    return current_path


def example2():
    """
    Call GET for http://httpbin.org/get

    Returns:
        Status Code of the HTTP Response
        URL in the Text of the HTTP Response
    """
    r = requests.get(BASE_URL + 'get')

    if r.status_code == 200:
        response_data = r.json()
        return r.status_code, response_data["url"]
    else:
        return r.status_code, ''
