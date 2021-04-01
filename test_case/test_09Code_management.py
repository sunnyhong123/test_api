#coding=utf-8
import unittest,json
from public.search import pages_turning
from public.login_test_brand import login_test_brand
from public.search import get_rd_value,public_post
from public.reader_csv import reader_text


store_id = reader_text(r"\data\store_id.txt")

class CodeManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)

    def test_01search_by_asin(self):
        '''查询asin'''
        rd_asin = get_rd_value("/api/admin/coupon/dealList", store_id, self.token, "asin")
        # print(rd_asin)
        if rd_asin is None:
            return  "list is null"
        data = {"store_id": store_id, "page_size": 10,"page": 1,"operator":"sunny_hong",
                "token": self.token, "account": "", "code_type": 1, "asin": rd_asin, "receive": ""}
        result = public_post("/api/admin/coupon/dealList",data)
        assert json.loads(result)["msg"] == "ok"
        assert len(json.loads(result)["data"]["data"]) > 0

    def test_02search_by_code(self):
        '''code查询'''
        rd_code = get_rd_value("/api/admin/coupon/dealList", store_id, self.token, "code")
        # print(rd_code)
        if rd_code is None:
            return "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "account": "", "code_type": 1, "asin": "", "receive": "", "code": rd_code}
        result = public_post("/api/admin/coupon/dealList", data)
        assert json.loads(result)["msg"] == "ok"
        assert len(json.loads(result)["data"]["data"]) > 0

    def test_03search_by_country(self):
        '''国家查询'''
        rd_country = get_rd_value("/api/admin/coupon/dealList", store_id, self.token, "country")
        # print(rd_country)
        if rd_country is None:
            return "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "account": "", "code_type": 1, "asin": "", "receive": "",
                "code": "", "country": rd_country }
        result = public_post("/api/admin/coupon/dealList", data)
        assert json.loads(result)["msg"] == "ok"
        assert len(json.loads(result)["data"]["data"]) > 0

    def test_04search_by_ctime(self):
        '''创建时间查询'''
        rd_ctime = get_rd_value("/api/admin/coupon/dealList", store_id, self.token, "ctime")
        # print(rd_ctime)
        if rd_ctime is None:
            return "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "account": "", "code_type": 1, "asin": "", "receive": "",
                "code": "", "country": "", "start_time": rd_ctime , "end_time": rd_ctime}
        result = public_post("/api/admin/coupon/dealList", data)
        assert json.loads(result)["msg"] == "ok"
        assert len(json.loads(result)["data"]["data"]) > 0


    def test_05import(self):
        """导入"""
        if store_id in ["9"]:
            return "list is null"
        with open(r"F:\test_1_brand\data\deal_coupon_template (1).xlsx", "rb") as f:
            file = {"file": f.read()}
            data = {"store_id": store_id, "operator": "sunny_hong", "token": self.token, "use_type": 1}
            result = public_post("/api/admin/coupon/importDeal", data, file)
            # print(result)
            assert json.loads(result)["code"] == 1


    def test_page_turning(self):
        """翻页"""
        result = pages_turning("/api/admin/coupon/dealList", store_id, self.token)
        self.assertEqual("pages turning success", result)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
