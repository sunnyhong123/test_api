#coding=utf-8
import unittest,requests,json
from public.login_test_brand import login_test_brand
from config.config import environmental
import random
from datetime import *
from public.reader_csv import read_save_txt,reader_text

# 官网id
from public.reader_csv import reader_text
import os

dir_path = os.path.dirname(__file__).split("test_case")[0]


store_id = reader_text(r"\data\store_id.txt")
# 创建活动类型
act_type = "1"  # 活动类型 1:九宫格 2:转盘 3:砸金蛋 4:翻牌 5:邀请好友注册 6:上传图片投票

# 活动类型      # 1.九宫格/转盘/砸金蛋/翻牌   # 2.邀请好友注册    #3.上传图片投票
activity_type = 1

# 上传产品  奖项==1   投票项==0
is_prize = 0

# 测试环境地址
test_url = environmental()

class Activity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #登录会员系统后台获取token
        cls.token = login_test_brand(store_id)
        # print(cls.token)

    def test_01add_activity(self):
        """创建活动"""
        name = "test"+ str(random.randint(0,100000))
        mark = str(random.randint(0,100000))
        now = datetime.now()
        y_now = now - timedelta(days=1)
        # print(y_now)
        next_now = now + timedelta(days=15)
        # print(name)
        url = test_url + "/api/admin/activity/insert"
        data = {"store_id":store_id,"operator":"sunny_hong","token":self.token,"lastDate":[],"name":name,
                "act_type":act_type,"mark":mark,"start_at":y_now,"end_at":next_now}
        r = requests.post(url=url,data=data)
        result = r.text
        # print(result)
        edit_id = str(json.loads(result)["data"]["id"])
        # print(edit_id)
        read_save_txt(r"\data\edit_id.txt",edit_id)
        self.assertEqual(json.loads(result)["code"],1)

    def test_02edit(self):
        """编辑活动"""
        name = "test_" + str(random.randint(0, 100000))
        mark = str(random.randint(0, 10000000))
        now = datetime.now()
        next_now = now + timedelta(days=20)
        # 随机获取活动类型
        num = random.randrange(1,5)
        # 读取创建活动id
        edit_id = reader_text(r"\data\edit_id.txt")
        url = test_url + "/api/admin/activity/edit"
        data = {"store_id":store_id,"operator":"sunny_hong","token":self.token,"id":edit_id,"name":name,"start_at":now,"end_at":next_now,"act_type":num,"mark":mark}
        r = requests.post(url=url,data=data)
        result = r.text
        # print(result)
        self.assertEqual(json.loads(result)["code"], 1)
        self.assertEqual(json.loads(result)["data"]["offset"],1)


    def test_03upload(self):
        """上传产品"""
        # 读取创建活动id
        global file
        edit_id = reader_text(r"\data\edit_id.txt")

        url = test_url + "/api/admin/activity/product/importActProduct"

        if activity_type == 1:
            # 1.九宫格/转盘/砸金蛋/翻牌
            lottery_path = (str(dir_path) + "data\\lottery_prize.xlsx")
            with open(lottery_path, 'rb') as f:
                file = {"file": f.read()}
                data = {"store_id": store_id, "act_id": edit_id, "operator": "sunny_hong", "token": self.token,
                        "is_prize": is_prize}
                r = requests.post(url=url, data=data, files=file)
                result = r.text
                print(result)
        elif activity_type == 2:
            # 2.邀请好友注册
            invite_path = str(dir_path) + "data\\activity_products_helped.xlsx"
            with open(invite_path, 'rb') as f:
                file = {"file": f.read()}
                data = {"store_id": store_id, "act_id": edit_id, "operator": "sunny_hong", "token": self.token,
                        "is_prize": is_prize}
                r = requests.post(url=url, data=data, files=file)
                result = r.text
                print(result)
        elif activity_type == 3:
            # 3.上传图片投票
            activity_vpr = str(dir_path) + "data\\activity_vote_prize_products.xlsx"
            with open(activity_vpr, 'rb') as f:
                file = {"file": f.read()}
                data = {"store_id": store_id, "act_id": edit_id, "operator": "sunny_hong", "token": self.token,
                    "is_prize": is_prize}
                r = requests.post(url=url, data=data, files=file)
                result = r.text
                print(result)


    def test_04search_activity(self):
        """查询"""
        # 1.根据单个活动名称查询
        url = test_url + "/api/admin/activity/list"
        num = random.randint(1,3)
        if num == 1:
            data =  {"page_size":10,"page":1,"store_id":store_id,"operator":"sunny_hong","token":self.token,"name":"test_6590",
                     "act_type":"","start_time":"","end_time":""}
        elif num == 2:
            data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": self.token,
                "name": "test_6590", "act_type": "1", "start_time": "", "end_time": ""}
        else:
            data ={"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": self.token,
                "name": "test_6590", "act_type": "", "start_time": "2020-04-20 19:41:49", "end_time": "2020-05-10 19:41:49"}
        # print(num)
        r = requests.post(url=url,data=data)
        result1 = r.text
        # print(result1)
        self.assertEqual(json.loads(result1)["code"],1)



    def test_05page_turning(self):
        """翻页"""
        url = test_url + "/api/admin/activity/list"
        num = random.randint(1, 3)

        data = {"page_size": 10, "page": num, "store_id": store_id, "operator": "sunny_hong", "token": self.token,
                "name": "",
                "act_type": "", "start_time": "", "end_time": ""}

        # print(num)
        r = requests.post(url=url, data=data)
        result1 = r.text
        # print(result1)
        self.assertEqual(json.loads(result1)["code"], 1)

    # def test_06click_activity(self):
    #     # 6.点击活动链接
    #     pass

    def test_07export(self):
        """导出"""
        url = test_url + "/api/admin/activity/export"
        data = {"store_id":store_id,"operator":"sunny_hong","token":self.token,"name":"",
                "act_type":"","start_time":"","end_time":"","lastDate":["",""]}
        r = requests.post(url=url,data=data)
        result = r.text
        # print(result)
        self.assertEqual(json.loads(result)["code"],1)
        url2 = environmental()+json.loads(result)["data"]["url"]
        # print(url2)
        r2 = requests.get(url=url2)
        results = r2.text
        # print(results)
        if len(results) > 4:
            print("导出成功")

    def test_08delete(self):
        """删除"""
        # 读取创建活动id
        edit_id = reader_text(r"\data\edit_id.txt")
        url = test_url + "/api/admin/activity/del"
        data = {"store_id":store_id,"operator":"sunny_hong","token":self.token,"id":[edit_id]}
        r = requests.post(url=url,data=data)
        result = r.text
        # print(result)
        self.assertEqual(json.loads(result)["code"],1)

    @classmethod
    def setUpclass(cls):
        pass

if __name__ == '__main__':
    unittest.main()


