#coding=utf-8
import unittest,json
from public.export import export_test
from public.login_test_brand import login_test_brand
from public.search import pages_turning,search_by_email,get_rd_value,public_post
from public.reader_csv import reader_text

store_id = reader_text(r"\data\store_id.txt")


class MemberList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)

    def test_01search_by_email(self):
        #1.查询
        rd_email = get_rd_value("/api/admin/credit/list", store_id,self.token,"account")
        data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong","token":self.token,"account":rd_email}
        result = public_post("/api/admin/credit/list",data)
        assert len(json.loads(result)["data"]["data"]) > 0
        assert json.loads(result)["msg"] == "ok"


    # def test_02export(self):
    #     #4.导出
    #     result = export_test("/api/admin/credit/export", self.token, store_id)
    #     self.assertEqual("export success", result)

    def test_03page_turning(self):
        #7.翻页
        result = pages_turning("/api/admin/activity/apply/list", store_id, self.token)
        self.assertEqual("pages turning success", result)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()

