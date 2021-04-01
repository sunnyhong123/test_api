#coding=utf-8
import unittest
import json,random,requests
from public.login_test_brand import login_test_brand
from config.config import environmental
from public.reader_csv import reader_text


store_id = reader_text(r"\data\store_id.txt")

# 测试环境地址
test_url = environmental("test")


class ActivityList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 1.登录会员系统获取token
        cls.token = login_test_brand(store_id)

    def test_01search(self):
        """查询"""
        num = random.randrange(1,7)
        # print(num)
        url = test_url+ "/api/admin/activity/product/actProductList"
        if num == 1:
            # 1.查询全部
            data = {"page_size":10,"page":1,"store_id":store_id,"operator":"sunny_hong","token":self.token}
        elif num == 2:
            # 2.活动名称查询
            data = {"page_size":10,"page":1,"store_id":store_id,"operator":"sunny_hong","token":self.token,
                 "name": "vt 新翻牌活动"}
            # 3.活动类型查询
        elif num == 3:
            data = {"page_size":10,"page":1,"store_id":store_id,"operator":"sunny_hong","token":self.token,
               "act_type":"4"}
            # 4.产品类型查询
        elif num == 4:
            data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": self.token,
                    "type": 3}
            # 5.活动时间查询
        elif num == 5:
            data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": self.token,
                    "start_at":"2020-04-22 00:00:00","end_at":"2020-04-30 00:00:00"}
            # 6.根据所有条件查询唯一一条数据
        else :
            data = {"page_size":10,"page":1,"store_id":store_id,"operator":"sunny_hong","token":self.token,
                    "name":"vt 新翻牌活动","act_type":"4","type":3,"start_at":"","end_at":""}

        r = requests.post(url=url,data=data)
        result = r.text
        # print(result)
        self.assertEqual(json.loads(result)["code"],1)

    def test_02import(self):
        """导出"""
        url = test_url + "/api/admin/activity/product/exportActProducts"
        data = {"store_id": store_id, "operator": "sunny_hong", "token": self.token, "name": "",
                "act_type": "", "start_time": "", "end_time": "", "lastDate": ["", ""]}
        r = requests.post(url=url, data=data)
        result = r.text
        # print(result)
        self.assertEqual(json.loads(result)["code"], 1)
        url2 = test_url + json.loads(result)["data"]["url"]
        # print(url2)
        r2 = requests.get(url=url2)
        results = r2.text
        # print(results)
        if len(results) > 4:
            print("导出成功")

    # def test_03edit(self):
    #     pass
    #     #3.修改

    def test_04page_turning(self):
        """翻页"""
        url = test_url + "/api/admin/activity/product/actProductList"
        num = random.randint(1, 3)

        data = {"page_size": 10, "page": num, "store_id": store_id, "operator": "sunny_hong", "token": self.token,
                "name": "",
                "act_type": "", "start_time": "", "end_time": ""}

        # print(num)
        r = requests.post(url=url, data=data)
        result1 = r.text
        # print(result1)
        self.assertEqual(json.loads(result1)["code"], 1)

    def test_05delete(self):
        """删除"""
        # 1.访问list接口获取ActivityPrize-id
        url1 =test_url + "/api/admin/activity/product/actProductList"
        data1 =  {"page_size":10,"page":1,"store_id":store_id,"operator":"sunny_hong","token":self.token}
        r = requests.post(url=url1,data=data1)
        result1 = r.text
        # print(result1)
        del_id = json.loads(result1)["data"]["data"][0]["id"]
        # print(del_id)
        # 2.请求删除产品接口,根据id删除
        url2 = test_url + "/api/admin/activity/product/delActProducts"
        data2 = {"store_id":store_id,"operator":"sunny_hong","token":self.token,"id[]":del_id}
        r2 = requests.post(url=url2,data=data2)
        result2 = r2.text
        # print(result2)
        self.assertEqual(json.loads(result2)["code"],1)


    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()