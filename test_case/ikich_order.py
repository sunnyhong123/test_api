#coding=utf-8
import unittest,requests,json
from public.login_test_brand import login_choice_website
from public.connect_dba import connect_dba
store_id = 1

class MemberList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_choice_website(store_id, "brand")
        cls.brand_url = "https://brand.patozon.net"

    def test_01get_order_status(self):
        '''获取Matching状态订单号'''
        url = self.brand_url + "/api/admin/order/list"
        data = {"store_id":store_id,"page_size":10,"page":1,"operator":"alice_huang",
                "token":self.token,"orderno":"","country":"","act_id":"","order_status":-1}
        r = requests.post(url,data)
        result = r.text
        # print(result)
        self.assertEqual(json.loads(result)["code"],1)
        total_page = json.loads(result)["data"]["pagination"]["total_page"]
        # print(total_page)
        num = 0
        order_country = ["us", "ca", "uk", "fr", "de"]
        for i in range(total_page):
            num = num +1
            data1 = {"store_id":store_id,"page_size":10,"page":num,"operator":"alice_huang",
                "token":self.token,"orderno":"","country":"","act_id":"","order_status":-1}
            r1 = requests.post(url, data1)
            result1 = r1.text
            # print(result1)
            assert json.loads(result1)["code"] == 1
            datas = json.loads(result1)["data"]["data"]
            for da in datas:
                # print(da["orderno"])
                for o in order_country:
                    connect_dba("select * from amazon_order_item_%s where amazon_order_id = '%s';" % (o,da["orderno"]))
        print(num)


if __name__ == '__main__':
    unittest.main()