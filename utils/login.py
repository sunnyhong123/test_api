#coding=utf-8
import requests
from config.config import TEST_HOST


def login(url_path,data):
    url = TEST_HOST +url_path

    r = requests.post(url,data=data)

    return  r.text


if __name__ == "__main__":
    pass
