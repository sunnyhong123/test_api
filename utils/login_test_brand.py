#coding=utf-8
import unittest
import requests,json


def login_test_brand():
    # #登录会员系统测试服后台
    # url = "http://test.brand.patozon.net/api/permission/user/login"
    url = "https://brandwtest.patozon.net/api/permission/user/login"
    datas = {"username": "sunny_hong", "password": "123456!@#", "store_id": 2}
    r = requests.post(url=url,data=datas)
    result = r.text
    return json.loads(result)["data"]["token"]

def delete_test_brand(email):
    #删除会员系统测试账号
    # url2 = "http://test.brand.patozon.net/api/admin/customer/forceDelete"

    url2 = "https://brandwtest.patozon.net/api/admin/customer/forceDelete"
    token = login_test_brand()
    datas = {"store_id":2,"operator":"sunny_hong","token":token,"account":email}
    r = requests.post(url=url2,data=datas)
    return  r.text
    # print(result)
    # print(json.loads(result)["code"])
    # self.assertEqual(json.loads(result)["code"],1)

if __name__ == "__main__":
    # unittest.main()
    print(delete_test_brand("mzhlpw08312@chacuo.net"))
