#coding=utf-8

import unittest,json
from public.login_test_brand import login_test_brand
from public.export import export_test
from public.search import pages_turning,invite_search,search_email,search_country,product_search,search_product,get_rd_value,public_post
from public.reader_csv import reader_text


store_id = reader_text(r"\data\store_id.txt")

class ProductReferral(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)

    def test_01search_by_email(self):
        """review收集活动邮箱查询"""
        rd_email = get_rd_value("/api/admin/activity/apply/list",store_id, self.token,"account" )
        if rd_email is None:
            return "list is null"
        data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong",
                "token":self.token,"audit_status":"","account":rd_email,"country":"","sku":""}
        result = public_post("/api/admin/activity/apply/list",data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["data"]["pagination"]["total"] > 0

    def test_02search_by_sku(self):
        """产品sku查询"""
        rd_sku = get_rd_value("/api/admin/activity/apply/list", store_id, self.token, "sku")
        if rd_sku is None:
            return "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "audit_status": "", "account": "", "country": "", "sku": rd_sku}
        result = public_post("/api/admin/activity/apply/list", data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["data"]["pagination"]["total"] > 0

    def test_03search_by_country(self):
        """站点查询"""
        rd_country = get_rd_value("/api/admin/activity/apply/list", store_id, self.token, "country")
        if rd_country is None:
            return "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "audit_status": "", "account": "", "country": rd_country, "sku": ""}
        result = public_post("/api/admin/activity/apply/list", data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["data"]["pagination"]["total"] > 0

    def test_04search_by_audit_status(self):
        """审核状态查询"""
        rd_audit_num =  None
        rd_audit_status_txt = get_rd_value("/api/admin/activity/apply/list", store_id, self.token, "audit_status")
        # print(rd_audit_status_txt)
        if rd_audit_status_txt is None:
            return "list is null"
        if rd_audit_status_txt == "未审核":
            rd_audit_num = "0"
        elif rd_audit_status_txt == "已通过":
            rd_audit_num = "1"
        elif rd_audit_status_txt == "未通过":
            rd_audit_num = "2"
        elif rd_audit_status_txt == "其他":
            rd_audit_num = "3"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "audit_status": rd_audit_num, "account": "", "country": "", "sku": ""}
        result = public_post("/api/admin/activity/apply/list", data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["data"]["pagination"]["total"] > 0



    def test_02import(self):
        """邀请关系列表导出"""
        result = export_test("/api/admin/activity/apply/export", self.token, store_id)
        self.assertEqual("export success", result)

    def test_03page_turning(self):
        """邀请关系列表翻页"""
        result = pages_turning("/api/admin/activity/apply/list", store_id, self.token )
        self.assertEqual("pages turning success", result)


    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
