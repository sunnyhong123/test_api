#coding=utf-8
from public import login_test_brand
import requests,random,json

#https://testapi.patozon.net
#"https://release-api.patozon.net"


class MpowOrder(object):
    def __init__(self,store_id):
        self.test_url = "https://release-api.patozon.net"
        self.store_id = store_id

    def register_order(self,orderno):
        '''注册加延保'''
        #1.获取随机邮箱
        rd_email = "".join(random.sample("abcdefgqweruiopzxcvbn1234678090", 8)) + "@chacuo.net"
        print(rd_email)
        # rd_email = "alexhong465@gmail.com"
        url = self.test_url + "/api/shop/customer/createCustomer"
        data = {"platform": "Shopify", "action": "register", "act_id": "0", "store_id": self.store_id, "account": rd_email,
                "orderno": orderno, "order_country": "US", "password": "123456",
                "accepts_marketing": 1, "confirmPassword": "123456"}
        r = requests.post(url, data)
        result = r.text
        print(result)
        assert json.loads(result)["code"] == 1
        return rd_email

    def register(self):
        # 1.获取随机邮箱
        rd_email = "".join(random.sample("QWERTYUIOPasdfghjklzxcvb12345678980", 8)) + "@chacuo.net"
        print(rd_email)
        password = "123456"
        url = self.test_url + "/api/shop/customer/createCustomer"
        data = {"platform": "Shopify", "action": "register", "act_id": "0", "store_id": self.store_id, "account": rd_email,
                "order_country": "US", "password": password, "accepts_marketing": 1,
                "confirmPassword": password}
        r = requests.post(url, data)
        result = r.text
        print(result)
        assert json.loads(result)["code"] == 1
        return rd_email


    def login_order(self,orderno,rd_email):
        '''登录加延保'''
        #1.调用注册账号接口
        url = self.test_url +"/api/shop/order/bind"
        data = {"store_id":self.store_id,"account":rd_email,"orderno":orderno,"order_country":"US"}
        r = requests.post(url,data)
        result = r.text
        print(result)
        assert json.loads(result)["code"] == 1

    def input_start(self,orderno,rd_email,num):
        '''订单评星'''
        url = self.test_url + "/api/shop/order/review/input"
        data = {"account":rd_email,"star":num,"orderno":orderno,"store_id":self.store_id}     #"113-2570035-9962621"
        r = requests.post(url,data)
        result = r.text
        # print(result)

    def upload(self):
        '''上传图片'''
        url = self.test_url + "/api/common/upload"
        with open(r"C:\Users\Administrator\Desktop\lADPBbCc1hhR7O3MhczG_198_133.jpg","rb") as f:
            file = {"file":f.read()}
            data = {"store_id":1}
            r = requests.post(url,data,files=file)
            result = r.text
            print(result)
        assert json.loads(result)["code"] == 1
        print(json.loads(result)["data"]["url"])
        return json.loads(result)["data"]["url"]

    def input_url_picture(self,rd_email,orderno,img_url=None):
        '''提交上传图片或者链接地址'''
        url = self.test_url + "/api/shop/order/review/input"

        payload = "{\n    \"account\": \"%s\",\n    \"orderno\": \"%s\",\n   \"review_link\": \"https://www.amazon.net/123\",\n    \"review_img_url\": \"%s\",\n    \"store_id\": %s\n}"%(rd_email,orderno,img_url,self.store_id)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        result = response.text.encode('utf8')
        # print(result)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["data"]["ext_type"] == "OrderReview"

class Brandwtest(object):
    def __init__(self,store_id):
        #获取token
        self.store_id = store_id
        self.test_url = "https://release-api.patozon.net"
        self.token =login_test_brand.release_brand1()
        # print(self.token)

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
            print(result)
            assert json.loads(result)["code"] == 1


    def add_reward(self,asin,country):
        """添加实物奖励"""
        url =  self.test_url + "/api/admin/reward/add"
        payload = {'name': 'shiwu',
                   'type': '3',
                   'type_value':'https://cdn.shopify.com/s/files/1/0074/9987/4402/files/617_FT_500.jpg?v=1599719707',
                   'asin':asin,
                   'country':country,
                   'business_type': '1',
                   'reward_status': '2',
                   'store_id':self.store_id ,
                   'operator': 'Sunny_hong(洪磊)',
                   'token': self.token,
                   'category_data': '[{"category_code":"BA","category_name":"母婴","level":1},{"category_code":"BA02",'
                                    '"category_name":"婴儿用品","level":2},{"category_code":"BA0201","category_name":"婴儿车罩","level":3}]'}
        r = requests.post( url=url, data=payload)
        r.encoding = "utf-8"
        result = r.text
        print(result)
        assert json.loads(result)["code"] == 1


    def add_coupon(self):
        """添加折扣码奖励"""
        url = self.test_url + "/api/admin/reward/add"
        with open(r"F:\test_1_brand\data\reward_coupon_template (1).xlsx", "rb") as f:
            file = {"file": f.read()}
            payload = {'name': '30% off coupon',
                       'type': '2',
                       'business_type': '1',
                       'reward_status': '2',
                       'store_id': self.store_id,
                       'operator': 'Sunny_hong(洪磊)',
                       'token': self.token,
                       'category_data': '[{"category_code":"AR","category_name":"艺术手工","level":1},{"category_code":"AR01","category_name":"手工制作","level":2},{"category_code":"AR0103","category_name":"胶枪","level":3}]'}

            r = requests.request("POST", url=url, data=payload, files=file)
            r.encoding = "utf-8"
            result = r.text
            # print(result)
            assert json.loads(result)["code"] == 1

    def add_points(self,asin,country):
        """添加积分奖励"""
        url = self.test_url + "/api/admin/reward/add"
        payload = {'name': '11 points',
                   'type': '5',
                   'type_value': '10',
                   'asin': asin,
                   'country': country,
                   'business_type': '1',
                   'reward_status': '2',
                   'store_id': self.store_id,
                   'operator': 'Sunny_hong(洪磊)',
                   'token': self.token,
                   'category_data': '[{"category_code":"BA","category_name":"母婴","level":1},{"category_code":"BA02",'
                                    '"category_name":"婴儿用品","level":2},{"category_code":"BA0201","category_name":"婴儿车罩","level":3}]'}
        r = requests.post(url=url, data=payload)
        r.encoding = "utf-8"
        result = r.text
        # print(result)
        assert json.loads(result)["code"] == 1

    def add_other(self,asin,country):
        """添加其他奖励"""
        url = self.test_url + "/api/admin/reward/add"
        payload = {'name': '11 other',
                   'type': '0',
                   'type_value': '10',
                   'asin': asin,
                   'country': country,
                   'business_type': '1',
                   'reward_status': '2',
                   'store_id': self.store_id,
                   'operator': 'Sunny_hong(洪磊)',
                   'token': self.token,
                   'category_data': '[{"category_code":"BY","category_name":"个护化妆","level":1},'
                                    '{"category_code":"BY02","category_name":"身体护理","level":2},{"category_code":"BY0203","category_name":"美甲机","level":3}]'}
        r = requests.post(url=url, data=payload)
        result = r.text.encode('utf8')
        print(result)
        assert json.loads(result)["code"] == 1

    def audit_award(self):
        """礼品卡、实物、其他奖励审核通过"""
        # 1.获取评论列表data数据，判断邮箱，通过审核
        api_url =  "/api/admin/orderReview/list"
        payload = {"store_id":self.store_id,"token":self.token,"page":1,"page_size":10,"operator":"Sunny_hong(洪磊)"}
        result = Brandwtest.public_post(self,api_url,payload)
        ids = Brandwtest.return_ids(self,result)
        audit_url = "/api/admin/orderReview/audit"
        payload1 = {"audit_status":1,"reviewer":"sunny test","ids[]":[ids],"store_id":self.store_id,"remarks":"test",
                    "token":self.token,"operator":"Sunny_hong(洪磊)"}
        result1 = Brandwtest.public_post(self,audit_url,payload1)
        assert json.loads(result1)["code"] == 1
        return json.loads(result1)["msg"]

    def return_ids(self,result):
        """判断是否为测试账号且未审核"""
        num = 0
        while num < 10:
            if json.loads(result)["data"]["data"][num]["account"] == "alexhong465@gmail.com":
                if json.loads(result)["data"]["data"][num]["audit_status"] == "未审核":
                    # 审核通过
                    ids = json.loads(result)["data"]["data"][num]["id"]
                    return ids
            else:
                num += 1



    def get_add_id(self):
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
        assert  json.loads(result)["msg"] == "ok"

    def delete_email(self, email):
        '''删除测试账号'''
        url = "/api/admin/customer/forceDelete"
        data = {"store_id": self.store_id, "operator": "Sunny_hong(洪磊)", "token": self.token, "account": email}
        result = Brandwtest.public_post(self, url, data)
        # print(result)
        assert json.loads(result)["msg"] == "success"

    def public_post(self,api_url, data, file=None):
        '''请求公共方法'''
        try:
            url = self.test_url + api_url
            r = requests.post(url, data, files=file)
            result = r.text
            if json.loads(result)["code"] == 1:
                return result
            else:
                return "requests is False"
        except Exception as e:
            return e


if __name__ == '__main__':
    a = MpowOrder(11)
    #2.登录延保+评星+提交rv
    # email = "alexhong465@gmail.com"
    # order_list = ["406-6288392-4481968"]
    # for order in order_list:
    #     a.login_order(order,email)  #登录延保
    #     a.input_start(order, email, 4) #评星
    #     # img_url = a.upload()
    #     a.input_url_picture(email,order) #提交RV


    order = "250-1879415-6824664"
    #1.注册账号
    # rd_email = a.register()
    rd_email = 'alexhong465@gmail.com'
    #登录延保
    a.login_order(order,rd_email)
    #评星
    a.input_start(order,rd_email,4)
    a.input_url_picture(rd_email, order)


    # order = "114-6326085-1513042"
    # email = "alexhong465@gmail.com"
    # a.login_order(order,email)
    # # 评星
    # a.input_start(order, email, 2)
    # img_url = a.upload()
    # a.input_url_picture(email,order,img_url)


    #2.注册加延保
    # order = "205-8692661-1139566"
    # rd_email = a.register_order(order)
    # print(rd_email)
    # # 评星
    # a.input_start(order, rd_email,4)
    #
    # #3.上传图片获取图片地址
    # img_url = a.upload()
    # a.input_url_picture(rd_email,order,img_url)


