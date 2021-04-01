#coding=utf-8
from config.config import environmental
import requests,json


test_url = environmental()


def delete_email(api_url,store_id,token,email):
    '''删除测试账号'''
    url = test_url + api_url
    data = {"store_id":store_id,"operator":"sunny_hong", "token":token,"account":email}
    r = requests.post(url,data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    # assert  json.loads(result)["data"][0]["account"] == email
    return  "delete email success"

if __name__ == '__main__':
    delete_email("/api/admin/customer/forceDelete",2,"9938a776423d2ecaefacc8510b07c763_1590659072","002936gb@chacuo.net")