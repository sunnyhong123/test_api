#coding=utf-8
import unittest,json
from public.export import export_test
from public.search import pages_turning
from public.login_test_brand import login_test_brand
from public.register import register
from public.connect_dba import get_order_db
from public.warranty_order import add_order,delete_order
from public.search import search_id_by_email,search_by_email,public_post,get_rd_value
from public.reader_csv import reader_text

store_id = reader_text(r"\data\store_id.txt")
# print(store_id)

class MemberList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)
        # 1.新建账号
        cls.email = register(store_id)
        # print(cls.email)

    def test_01add_order(self):
        '''新增订单'''
        #2.连接销参数据库获取订单号
        order_no = get_order_db("select amazon_order_item_ca.amazon_order_id from amazon_order_item_ca where amazon_order_item_ca.order_status = 'Shipped' limit 10;")
        # print(order_no)
        #3.新增订单
        result = add_order("/api/admin/order/bind", self.email, order_no, store_id,self.token)
        self.assertEqual("add order success",result)

    def test_02delete_order(self):
        '''删除订单'''
        #1.获取id
        result = search_id_by_email("/api/admin/order/list",store_id,self.token)
        order_id = json.loads(result)["data"]["data"][0]["id"]
        #删除
        result1 = delete_order("/api/admin/order/unbind",store_id,order_id,self.token)
        self.assertEqual("delete order success",result1)

    def test_03search(self):
        #1.查询
        rd_email = get_rd_value("/api/admin/order/list",store_id,self.token,"account")
        data ={"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong","token":self.token,"orderno":"",
               "country":"","act_id":"","account":rd_email}
        result = public_post("/api/admin/order/list",data)
        assert json.loads(result)["code"] == 1


    # def test_04export(self):
    #     #4.导出
    #     result = export_test("/api/admin/customer/export", self.token, store_id)
    #     self.assertEqual("export success", result)

    def test_05page_turning(self):
        #7.翻页
        result = pages_turning("/api/admin/activity/apply/list", store_id, self.token)
        self.assertEqual("pages turning success", result)

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
