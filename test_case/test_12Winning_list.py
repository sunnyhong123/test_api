#coding=utf-8

import unittest,requests,json,random
from public.login_test_brand import login_test_brand
from config.config import environmental
from public.search import search,search_email,search_prize,search_country,pages_turning
from public.export import export_test
from public.reader_csv import reader_text


store_id = reader_text(r"\data\store_id.txt")

#测试环境地址
test_url = environmental()


class WinningList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)

    def test_01search(self):
        """查询"""
        # 1.1随机获取list邮箱
        rd_email  = search("/api/admin/activity/winning/list",store_id,self.token)[0]
        rd_prize = search("/api/admin/activity/winning/list", store_id, self.token)[1]
        rd_country = search("/api/admin/activity/winning/list", store_id, self.token)[2]
        # print(rd_email,rd_prize,rd_country)
        # 1.2根据邮箱查询
        result1 = search_email("/api/admin/activity/winning/list",store_id,self.token,rd_email)
        self.assertEqual("search email success", result1)
        # print(result1)
        # 1.3根据奖品名称查询
        result2 = search_prize("/api/admin/activity/winning/list",store_id,self.token,rd_prize)
        self.assertEqual("search prize success", result2)
        # print(result2)
        # 1.4根据国家查询
        result3 = search_country("/api/admin/activity/winning/list", store_id, self.token)
        self.assertEqual("search country success", result3)


    def test_02import(self):
        """中奖列表导出"""
        result = export_test("/api/admin/activity/winning/export", self.token, store_id)
        self.assertEqual("export success", result)

    def test_03page_turning(self):
        """中奖列表翻页"""
        result = pages_turning("/api/admin/activity/winning/list", store_id, self.token )
        self.assertEqual("pages turning success", result)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
