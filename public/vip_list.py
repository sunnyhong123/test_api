#coding=utf-8

import requests,json
from config.config import environmental

test_url = environmental()

class VipList(object):
    def __init__(self):
        pass

    def get_integral(self,api_url,store_id,token,email):
        #增加积分
        #1.获取测试邮箱当前积分
        url = test_url +api_url
        data = {"store_id":store_id,"page_size":10,"page":1,"operator":"dev","token":token
            ,"source":"","account":email,"country":"","vip":"","isactivate":"","is_has_profile":""}
        r = requests.post(url,data)
        result = r.text
        # print(result)
        assert json.loads(result)["code"] == 1
        # assert json.loads(result)["data"]["data"]["account"] == email
        #会员列表总积分
        total_credit = json.loads(result)["data"]["data"][0]["total_credit"]
        # print(total_credit)
        customer_id = json.loads(result)["data"]["data"][0]["customer_id"]
        return total_credit,customer_id
        #3.判断增加后积分是否等当前积分+10积分
    def get_exp(self,api_url, store_id, token, email):
            # 增加积分
            # 1.获取测试邮箱当前经验值
            url = test_url + api_url
            data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "dev", "token": token
                , "source": "", "account": email, "country": "", "vip": "", "isactivate": "", "is_has_profile": ""}
            r = requests.post(url, data)
            result = r.text
            # print(result)
            assert json.loads(result)["code"] == 1
            # assert json.loads(result)["data"]["data"]["account"] == email
            # 会员列表总积分
            exp = json.loads(result)["data"]["data"][0]["exp"]
            # print(total_credit)
            customer_id = json.loads(result)["data"]["data"][0]["customer_id"]
            return exp, customer_id

    def add_integral(self, api_url, store_id, token, customer_id):
        # 2.增加测试邮箱10积分
        url = test_url + api_url
        data = {"add_type": "1", "value": "10", "remark": "test", "customer_id": customer_id, "store_id": store_id,
                "operator": "sunny_hong","token": token, "action": "other"}
        r = requests.post(url, data)
        result = r.text
        # print(result)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["msg"] == "ok"
        return "add integral success"

    def add_experience(self, api_url, store_id, token, customer_id):
        #增加经验
        # 2.增加测试邮箱10经验值
        url = test_url + api_url
        data = {"add_type": "1", "value": "10", "remark": "test", "customer_id": customer_id, "store_id": store_id,
                "operator": "sunny_hong", "token": token, "action": "other"}
        r = requests.post(url, data)
        result = r.text
        # print(result)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["msg"] == "ok"
        return "add exp success"



if __name__ == '__main__':
    pass
