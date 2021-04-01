#coding=utf-8
import unittest,json
from public.export import export_test
from public.search import pages_turning,get_rd_value,public_post
from public.login_test_brand import login_test_brand
from public.reader_csv import reader_text


store_id = reader_text(r"\data\store_id.txt")

class Email(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)

    def test_01search_by_email(self):
        '''邮箱查询'''
        rd_to_email = get_rd_value("/api/admin/email/list",store_id,self.token,"to_email")
        data = {"store_id": store_id,"page_size": 10,"page": 1,"operator":"sunny_hong",
                "token": self.token, "account": rd_to_email}
        result = public_post("/api/admin/email/list", data)
        # print(result)
        assert json.loads(result)["msg"] == "ok"
        # assert len(json.loads(result)["data"]["data"]) > 0

    def test_02search_by_ctime(self):
        '''邮件发送时间查询'''
        rd_ctime = get_rd_value("/api/admin/email/list", store_id, self.token, "ctime")
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "account": "", "start_time": rd_ctime, "end_time": rd_ctime}
        result = public_post("/api/admin/email/list", data)
        # print(result)
        assert json.loads(result)["msg"] == "ok"
        # assert len(json.loads(result)["data"]["data"]) > 0

    # def test_03export(self):
    #     '''导出'''
    #     result = export_test("/api/admin/email/export", self.token, store_id)
    #     self.assertEqual("export success", result)

    def test_04page_turning(self):
        '''翻页'''
        result = pages_turning("/api/admin/email/list", store_id, self.token)
        self.assertEqual("pages turning success", result)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
