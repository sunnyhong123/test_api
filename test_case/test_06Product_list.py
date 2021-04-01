#coding=utf-8
import unittest,json,random
from public.export import export_test
from public.search import pages_turning,public_post,get_rd_value,get_frist_value
from public.login_test_brand import login_test_brand
from datetime import datetime
from public.reader_csv import reader_text

store_id = reader_text(r"\data\store_id.txt")

class MemberList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)
        cls.store_product_id = random.randint(0, 9999999999999)
        cls.now_time = datetime.now()

    def test_01search_by_product_id(self):
        '''随机查询产品id'''
        rd_id = get_rd_value("/api/admin/product/list",store_id,self.token,"store_product_id")
        print(rd_id)
        if rd_id is None:
            return "list is null"
        data ={"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong",
               "token":self.token,"store_product_id":rd_id,"sku":""}
        result = public_post("/api/admin/product/list",data)
        print(len(json.loads(result)["data"]["data"]))
        assert len(json.loads(result)["data"]["data"]) > 0

    def test_02search_by_sku(self):
        '''随机查询产品sku'''
        rd_sku = get_rd_value("/api/admin/product/list",store_id,self.token,"sku")
        # print(rd_sku)
        data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong",
                "token": self.token, "store_product_id": "", "sku": rd_sku}
        result = public_post("/api/admin/product/list", data)
        assert len(json.loads(result)["data"]["data"]) > 0


    def test_02add_product(self):
        '''添加产品'''
        data = {"store_product_id":self.store_product_id,"credit":"10","qty":"10",
                "product_status":"0","store_id":store_id,"operator":"sunny_hong","token":self.token}
        result = public_post("/api/admin/product/addedit", data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["msg"] == "ok"

    def test_03edit(self):
        '''编辑'''
        edit_id = get_frist_value("/api/admin/product/list",store_id,self.token,"id")
        data = {"id":edit_id,"store_product_id":self.store_product_id,"credit":"20","qty":"20","sku":"","name":"","status":1,
                "expire_time":self.now_time,"product_status":"下架","store_id":store_id,"operator":"sunny_hong","token":self.token}
        result = public_post("/api/admin/product/edit", data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["msg"] == "ok"

    def test_04delete_product(self):
        '''删除产品'''
        delete_id = get_frist_value("/api/admin/product/list",store_id,self.token,"id")
        # print(delete_id)
        data = {"store_id":store_id,"id":delete_id,"operator":"sunny_hong","token":self.token}
        result = public_post("/api/admin/product/delete", data)
        assert json.loads(result)["code"] == 1
        assert json.loads(result)["msg"] == "ok"

    # def test_05pull_out(self):
    #     #3.拉取
    #     pass

    # def test_06export(self):
    #     #4.导出
    #     result = export_test("/api/admin/activity/product/export", self.token, store_id)
    #     self.assertEqual("export success", result)


    def test_07page_turning(self):
        #6.翻页
        result = pages_turning("/api/admin/product/list", store_id, self.token)
        self.assertEqual("pages turning success", result)




    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()


