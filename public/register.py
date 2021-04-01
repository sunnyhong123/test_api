#coding=utf-8
import requests,random,json
from config.config import environmental
#活动id
act_id = 26
test_url = environmental()


# orderno = "112-5385779-2689042"

def register(store_id):
    #注册官网账号
    #获取随机邮箱
    rd_email = "".join(random.sample("abcdefgqweruiopzxcvbn1234678090", 8)) + "@chacuo.net"
    # print(rd_email)
    rd_ip = "".join(random.sample("1234567890",3))+"."+"".join(random.sample("1234567890",3))+"."+"".join(random.sample("1234567890",3))
    # rd_email = "alexhong465@gmail.com"
    url = test_url + "/api/shop/customer/createCustomer"
    #"app_env":"sandbox"
    data = {"platform":"Shopify","action":"register","act_id":act_id,"store_id":store_id,"account":rd_email,
            "orderno":"","order_country":"HK","password":"123456","invite_code":"","ip":"",
            "accepts_marketing":1}
    # print(data)
    r = requests.post(url, data)
    result = r.text.encode('utf-8')
    # print(result)
    assert json.loads(result)["code"] == 1
    return rd_email

if __name__ == '__main__':
    register(1)