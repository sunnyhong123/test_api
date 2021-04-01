#coding=utf-8

import requests,json
from config.config import environmental


test_url = environmental("test")


def add_test_brand(store_id,api_url,email,order,token):
    #获取token
    url = test_url + api_url
    data = {"account":email,"orderno":order,"country":"US","store_id":store_id,
            "operator":"sunny_hong","paltform":"Amazon","token":token}
    r = requests.post(url=url,data=data)
    result = r.text
    print(result)
    assert json.loads(result)["code"] == 1


if __name__ == '__main__':
    add_test_brand(2,"/api/admin/order/bind","u6qr192c@chacuo.net","114-6368351-8939418","a5c754cf4abca386405f7c54e908c9d3_1590723532")
