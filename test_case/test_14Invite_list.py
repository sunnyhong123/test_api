#coding=utf-8

import unittest,json
from public.login_test_brand import login_test_brand
from public.export import export_test
from public.search import pages_turning,get_rd_value,public_post
from public.reader_csv import reader_text


store_id = reader_text(r"\data\store_id.txt")

class InviteList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)

    def test_01search_by_email(self):
        """邀请关系列表邮箱查询"""
        # 1.1随机获取list邮箱
        rd_email = get_rd_value("/api/admin/invite/list",store_id,self.token,"account")
        if rd_email is None:
            return  "list is null"
        data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong","token":self.token,"account":rd_email,
                "country":"","invite_code":"","source":"","order_by_data":""}
        result = public_post("/api/admin/invite/list",data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["data"]["pagination"]["total"] > 0

    def test_02search_by_country(self):
        """国家查询"""
        rd_country = get_rd_value("/api/admin/invite/list", store_id, self.token, "country")
        if rd_country is None:
            return "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong", "token": self.token,
                "account": "", "country": rd_country, "invite_code": "", "source": "", "order_by_data": ""}
        result = public_post("/api/admin/invite/list", data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["data"]["pagination"]["total"] > 0

    def test_03search_by_invite_code(self):
        """邀请码查询"""
        rd_invite_code = get_rd_value("/api/admin/invite/list", store_id, self.token, "invite_code")
        if rd_invite_code is None:
            return "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong", "token": self.token,
                "account": "", "country": "", "invite_code":rd_invite_code , "source": "", "order_by_data": ""}
        result = public_post("/api/admin/invite/list", data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["data"]["pagination"]["total"] > 0

    def test_04search_by_invite_time(self):
        """邀请时间查询"""
        rd_invite_time = get_rd_value("/api/admin/invite/list", store_id, self.token, "ctime")
        if rd_invite_time is None:
            return "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong", "token": self.token,
                "account": "", "country": "", "invite_code":"" , "source": "", "order_by_data": "","start_at":rd_invite_time,"end_at":rd_invite_time}
        result = public_post("/api/admin/invite/list", data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["data"]["pagination"]["total"] > 0

    def test_02import(self):
        """邀请关系列表导出"""
        result = export_test("/api/admin/invite/export", self.token, store_id)
        self.assertEqual("export success", result)

    def test_03page_turning(self):
        ""'邀请关系列表翻页'""
        result = pages_turning("/api/admin/invite/list", store_id, self.token )
        self.assertEqual("pages turning success", result)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
