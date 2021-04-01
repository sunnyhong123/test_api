#coding=utf-8
import unittest,json, requests
from public.export import export_test
from public.search import pages_turning,get_rd_value,public_post,get_frist_value
from public.login_test_brand import login_test_brand
from public.reader_csv import reader_text

store_id = reader_text(r"\data\store_id.txt")
print(type(store_id))

class MemberList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)
    # @unittest.skip("不想测了")
    def test_01search_by_asin(self):
        """查询asin"""
        rd_asin = get_rd_value("/api/admin/activity/product/list",store_id,self.token,"asin")
        # print(rd_asin)
        if rd_asin is None:
            return  "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "asin": rd_asin}
        result = public_post("/api/admin/product/list", data)
        assert len(json.loads(result)["data"]["data"]) > 0

    # @unittest.skip("不想测了")
    def test_02search_by_country(self):
        """查询国家"""
        rd_country = get_rd_value("/api/admin/activity/product/list", store_id, self.token, "country")
        # print(rd_country)
        if rd_country is None:
            return  "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "country": rd_country}
        result = public_post("/api/admin/product/list", data)
        # print(len(json.loads(result)["data"]["data"]))
        assert len(json.loads(result)["data"]["data"]) > 0

    # @unittest.skip("不想测了")
    def test_03search_by_mb_type(self):
        '''查询模板类型'''
        mb_type = get_rd_value("/api/admin/activity/product/list", store_id, self.token, "mb_type")
        # print(mb_type)
        if mb_type is None:
            return  "list is null"
        if mb_type == 3:
            mb_type+=1
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "mb_type": mb_type}
        result = public_post("/api/admin/product/list", data)
        # print(len(json.loads(result)["data"]["data"]))
        assert len(json.loads(result)["data"]["data"]) > 0

    # @unittest.skip(reason="不想测了")
    def test_04search_by_time(self):
        '''查询上传时间'''
        created_at = get_rd_value("/api/admin/activity/product/list", store_id, self.token, "created_at")
        # print(created_at)
        if created_at is None:
            return "list is null"
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "created_at": created_at}
        result = public_post("/api/admin/product/list", data)
        assert len(json.loads(result)["data"]["data"]) > 0


    def test_05import(self):
        '''导入通用折扣码'''
        if store_id in ["9","10","8","3","5","6"]:
            return "list is null"
        with open(r"F:\test_1_brand\data\deal-common (1).xlsx", "rb") as f:
            file = {"file": f.read()}
            data = {"store_id": store_id, "operator": "sunny_hong","token": self.token,"mb_type": 4}
            result = public_post("/api/admin/activity/product/importUniversal", data, file)
            print(result)
            assert json.loads(result)["code"] == 1

    def test_06edit(self):
        '''编辑产品'''
        id = get_frist_value("/api/admin/activity/product/list", store_id, self.token, "id")
        if id is None:
            return "list is null"
        data = {"product_id":id,"name":"Mpow H16 Noise Cancelling Kopfhörer-test","sku":"BHMPBH372AB-DEAS1-test",
                "asin":"B07SX3YNN1-test","activity_name":"summer-sale2-test",
                "act_type":9,"store_id":store_id,"operator":"sunny_hong","token":self.token}
        result = public_post("/api/admin/activity/product/edit", data)
        # print(result)
        assert json.loads(result)["msg"] == "ok"
        assert json.loads(result)["data"] == 1
    # #
    def test_07action(self):
        '''启用deal产品'''
        id = get_frist_value("/api/admin/activity/product/list", store_id, self.token, "id")
        if id is None:
            return "list is null"
        data ={"store_id":store_id,"operator":"sunny_hong","token":self.token,
               "product_status":"1","mb_type":4,"country":"DE","product_id":id,"act_type":9}
        result = public_post("/api/admin/activity/product/operate", data)
        # print(result)
        assert json.loads(result)["data"] == 1

    def test_08delete_product(self):
        '''删除Deal产品'''
        #1.获取导入的第一个产品id
        id = get_frist_value("/api/admin/activity/product/list", store_id, self.token, "id")
        if id is None:
            return "list is null"
        # print(id)
        data = {"store_id": store_id, "operator": "sunny_hong", "token": self.token, "product_id[]": id}
        result = public_post("/api/admin/activity/product/delete", data)
        # print(result)
        assert json.loads(result)["msg"] == "ok"
        assert json.loads(result)["data"] == 1

    #
    # def test_09export(self):
    #     '''导出'''
    #     result = export_test("/api/admin/activity/product/export", self.token, store_id)
    #     self.assertEqual("export success", result)


    def test_10page_turning(self):
        '''翻页'''
        result = pages_turning("/api/admin/activity/product/list", store_id, self.token)
        self.assertEqual("pages turning success", result)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()

