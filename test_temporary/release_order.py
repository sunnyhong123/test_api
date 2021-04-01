#coding=utf-8
import requests,json
from public import login_test_brand

class Brandwtest(object):
    def __init__(self,store_id):
        #获取token
        self.test_url = "https://release-api.patozon.net"
        self.token =login_test_brand.release_brand(1)
        self.store_id = store_id
        print(self.token)

    def add_gift_card(self):
        """添加礼品卡"""
        url = self.test_url + "/api/admin/reward/add"
        with open(r"F:\test_1_brand\data\reward_gift_card_template (4).xlsx", "rb") as f:
            file = {"file": f.read()}
            payload = {'name': '10 gift card',
                       'type': '1',
                       'business_type': '1',
                       'reward_status': '2',
                       'store_id': self.store_id,
                       'operator': 'Sunny_hong(洪磊)',
                       'token': self.token,
                       'category_data': '[{"category_code":"AR","category_name":"艺术手工","level":1},{"category_code":"AR01","category_name":"手工制作","level":2},{"category_code":"AR0103","category_name":"胶枪","level":3}]'}

            r = requests.request("POST", url=url, data=payload, files=file)
            r.encoding= "utf-8"
            result = r.text
            # print(result)
            assert json.loads(result)["code"] == 1


    def add_reward(self,store_id,asin,country):
        """添加实物奖励"""
        url =  self.test_url + "/api/admin/reward/add"
        payload = {'name': 'shiwu',
                   'type': '3',
                   'type_value':'https://cdn.shopify.com/s/files/1/0074/9987/4402/files/617_FT_500.jpg?v=1599719707',
                   'asin':asin,
                   'country':country,
                   'business_type': '1',
                   'reward_status': '2',
                   'store_id':store_id ,
                   'operator': 'Sunny_hong(洪磊)',
                   'token': self.token,
                   'category_data': '[{"category_code":"BA","category_name":"母婴","level":1},{"category_code":"BA02",'
                                    '"category_name":"婴儿用品","level":2},{"category_code":"BA0201","category_name":"婴儿车罩","level":3}]'}
        r = requests.post( url=url, data=payload)
        r.encoding = "utf-8"
        result = r.text
        # print(result)
        assert json.loads(result)["code"] == 1


    def add_coupon(self,store_id):
        """添加折扣码奖励"""
        url = self.test_url + "/api/admin/reward/add"
        with open(r"F:\test_vt_brand\data\reward_coupon_template (1).xlsx", "rb") as f:
            file = {"file": f.read()}
            payload = {'name': '30% off coupon',
                       'type': '2',
                       'business_type': '1',
                       'reward_status': '2',
                       'store_id': store_id,
                       'operator': 'Sunny_hong(洪磊)',
                       'token': self.token,
                       'category_data': '[{"category_code":"AR","category_name":"艺术手工","level":1},{"category_code":"AR01","category_name":"手工制作","level":2},{"category_code":"AR0103","category_name":"胶枪","level":3}]'}

            r = requests.request("POST", url=url, data=payload, files=file)
            r.encoding = "utf-8"
            result = r.text
            # print(result)
            assert json.loads(result)["code"] == 1

    def add_points(self,store_id,asin,country):
        """添加积分奖励"""
        url = self.test_url + "/api/admin/reward/add"
        payload = {'name': '11 points',
                   'type': '5',
                   'type_value': '10',
                   'asin': asin,
                   'country': country,
                   'business_type': '1',
                   'reward_status': '2',
                   'store_id': store_id,
                   'operator': 'Sunny_hong(洪磊)',
                   'token': self.token,
                   'category_data': '[{"category_code":"BA","category_name":"母婴","level":1},{"category_code":"BA02",'
                                    '"category_name":"婴儿用品","level":2},{"category_code":"BA0201","category_name":"婴儿车罩","level":3}]'}
        r = requests.post(url=url, data=payload)
        r.encoding = "utf-8"
        result = r.text
        # print(result)
        assert json.loads(result)["code"] == 1

    def add_other(self,store_id,asin,country):
        """添加其他奖励"""
        url = self.test_url + "/api/admin/reward/add"
        payload = {'name': '11 other',
                   'type': '0',
                   'type_value': '10',
                   'asin': asin,
                   'country': country,
                   'business_type': '1',
                   'reward_status': '2',
                   'store_id': store_id,
                   'operator': 'Sunny_hong(洪磊)',
                   'token': self.token,
                   'category_data': '[{"category_code":"BY","category_name":"个护化妆","level":1},'
                                    '{"category_code":"BY02","category_name":"身体护理","level":2},{"category_code":"BY0203","category_name":"美甲机","level":3}]'}
        r = requests.post(url=url, data=payload)
        result = r.text.encode('utf8')
        # print(result)
        assert json.loads(result)["code"] == 1

    def add_list(self):
        """获取添加礼品成功的id"""
        url = self.test_url + "/api/admin/reward/list"
        payload = {"store_id":"1","token":self.token,"operator":"Sunny_hong(洪磊)","one_category_code":[],"two_category_code":[],"three_category_code":[],"country":[],"page":1,"page_size":10}
        r = requests.post(url=url, data=payload)
        result = r.text.encode('utf8')
        # print(result)
        assert json.loads(result)["code"] == 1
        return json.loads(result)["data"]["data"][0]["id"]

    def delete_prize(self,id):
        """删除添加的奖励"""
        url = self.test_url + "/api/admin/reward/delete"
        payload = {"store_id":"1","token":self.token,"operator":"Sunny_hong(洪磊)","ids":[id]}
        response = requests.request("POST", url, data=payload)
        result = response.text
        # print(result)
        assert json.loads(result)["code"] == 1

if __name__ == '__main__':
    a = Brandwtest(14)
    #后台添加礼品卡奖励 /对应不同国家
    # 延保 us => 发送us邮件
    # 延保 de => 发送de邮件
    # 延保 it => 发送it邮件
    # 延保 es => 发送es邮件
    # 延保 fr => 发送fr邮件
    # 延保其他国家 => 发送us邮件
    #有7封邮件分别为： 礼品卡审核通过、审核不通过、折扣码系统自动审核成功、实物审核通过、积分系统自动审核成功
    #其他奖励审核通过、二次索评邮件、延保成功邮件

    #1.后台添加礼品卡类型奖励   订单号：112-6409285-6813860、112-4849917-6457045
    # a.add_gift_card()
    #2.添加折扣码类型 114-7063842-1356250
    # a.add_coupon(1)
    #3.添加实物奖励类型
    a.add_reward(14,"B074W7TLNZ","FR") #111-6679141-4840239
    # 4.添加积分类型
    # a.add_points(1,"B07JDZQ4BH","FR")   #113-2569650-1893828
    # 5.添加其他奖励
    # a.add_other(1,"B07G7PDBKM","FR")    #113-9993397-5413835
