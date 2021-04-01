#coding=utf-8

import requests,json
from config.config import environmental

test_url = environmental()

def add_order(api_url,email,orderno,store_id,token):
    '''新增订单'''
    url = test_url + api_url
    data = {"account":email,"orderno":orderno,"country":"US","store_id":store_id,
            "operator":"sunny_hong","paltform":"Amazon","token":token}
    r = requests.post(url,data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["msg"] == "Your order has submitted successfully, and it is in review. The points will be added to your account in 48 hours."
    return "add order success"

def delete_order(api_url,store_id,id,token):
    '''删除订单'''
    url = test_url + api_url
    data = {"store_id":store_id,"operator":"sunny_hong","id":id,"token":token}
    r = requests.post(url,data)
    result = r.text
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["msg"] == "删除成功"
    return  "delete order success"


if __name__ == '__main__':
    add_order("/api/admin/order/bind","pnevifad@chacuo.net","114-6368351-8939418",2,"1ed7a1ee96317147fef6ac0dd349ebf2_1590995625")