#coding=utf-8

import unittest,json
from public.login_test_brand import login_test_brand
from public.search import search_not_review,review,pages_turning,get_rd_value,public_post
from public.export import export_test
from public.reader_csv import reader_text


store_id = reader_text(r"\data\store_id.txt")

class ActivityReview(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)

    def test_01search(self):
        """审核页面查询"""
        # 1.1随机获取list邮箱
        rd_email = get_rd_value("/api/admin/share/list",store_id,self.token,"account")
        data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong",
                "token":self.token,"audit_status":"","account":rd_email,"country":""}
        result = public_post("/api/admin/share/list",data)
        assert json.loads(result)["code"] == 1

    def test_02export(self):
        """审核页面导出"""
        result = export_test("/api/admin/share/export",self.token,store_id)
        self.assertEqual("export success",result)

    @unittest.skip(reason="不想审核")
    def test_03review(self):
        """审核"""
        # 1.筛选为未审核的邮箱 且为测试邮箱包含@chacuo.net的邮箱
        review_id = search_not_review("/api/admin/share/list", store_id, self.token)
        # 2.审核为已通过或者未通过 增加经验 经验明细方式 备注
        if review_id:
            result = review("/api/admin/share/audit",store_id, self.token,review_id)
            self.assertEqual("review success",result)

    def test_04page_turning(self):
        """翻页"""
        result = pages_turning("/api/admin/share/list",store_id,self.token)
        self.assertEqual("pages turning success",result)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
