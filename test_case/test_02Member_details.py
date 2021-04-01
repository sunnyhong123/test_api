#coding=utf-8
import unittest
from public.login_test_brand import login_test_brand
from public.search import search_by_email,search_country
from public.export import export_test
from public.search import pages_turning
from public.reader_csv import reader_text


store_id = reader_text(r"\data\store_id.txt")

class MemberList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)

    def test_01search_by_email(self):
        u'''根据邮箱查询'''
        result = search_by_email("/api/admin/customer/detailsList", store_id, self.token)
        self.assertEqual("search email success",result)

    def test_02search_by_country(self):
        '''根据国家查询'''
        result = search_country("/api/admin/customer/detailsList", store_id, self.token)
        self.assertEqual("search country success",result)



    # def test_02pull_out(self):
    #     #3.拉取
    #     pass

    # def test_03export(self):
    #     #4.导出
    #     result = export_test("/api/admin/customer/exportDetailsList", self.token, store_id)
    #     self.assertEqual("export success", result)

    # def test_05edit(self):
    #     #5.编辑
    #     pass

    def test_06page_turning(self):
        #7.翻页
        result = pages_turning("/api/admin/customer/detailsList", store_id, self.token)
        self.assertEqual("pages turning success", result)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()

