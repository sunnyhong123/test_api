#coding=utf-8

import requests,json
from config.config import environmental


test_url = environmental()

def login_test_brand(store_id):
    '''登录测试环境会员系统'''
    url = test_url + "/api/permission/user/login"
    data = {"username":"alice_huang","password":"123456!@#","store_id":store_id}
    r = requests.post(url,data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    return json.loads(result)["data"]["token"]

def login_brand(url,store_id):
    test_url1 = environmental()
    '''登录测试环境会员系统'''
    url = test_url1 + "/api/permission/user/login"
    data = {"username":"alice_huang","password":"123456!@#","store_id":store_id}
    header  = {
  'Connection': 'keep-alive',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
  'Content-Type': 'application/json'}
    r = requests.request("POST",url,data=data,headers=header)
    result = r.text
    print(result)
    assert json.loads(result)["code"] == 1
    return json.loads(result)["data"]["token"]


def release_brand(store_id):
    url = "https://release-api.patozon.net/api/permission/user/login"

    payload="{\n    \"username\": \"alice_huang\",\n    \"password\": \"123456!@#\",\n    \"store_id\": %s\n}"%store_id
    headers = {
      'Connection': 'keep-alive',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = response.text
    # print(result)
    assert json.loads(result)["code"] == 1
    return json.loads(result)["data"]["token"]

def release_brand1():
    url = "https://release-api.patozon.net/api/permission/user/login"


    payload="{\n    \"username\": \"alice_huang\",\n    \"password\": \"123456!@#\",\n    \"store_id\": 1\n}"
    headers = {
      'Connection': 'keep-alive',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = response.text
    print(result)
    assert json.loads(result)["code"] == 1
    return json.loads(result)["data"]["token"]



if __name__ == '__main__':
    release_brand1()