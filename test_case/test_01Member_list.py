#coding=utf-8
import unittest
from public.login_test_brand import login_test_brand
from public.search import customer_search,search_email,search_country,search_invite,search_vip,search_source,search_test_email
from public.register import register
from public.export import export_test
from public.search import pages_turning
from public.vip_list import VipList
from public.reader_csv import reader_text


store_id = reader_text(r"\data\store_id.txt")
# print(store_id)

class MemberList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录会员系统后台获取token
        cls.token = login_test_brand(store_id)
        cls.ad = VipList()

        # print(cls.token)

    def test_01search(self):
        #1.查询
        #1.1获取列表数据
        # global rd_num
        r_email = customer_search("/api/admin/customer/list",store_id,self.token)[0]
        # print(rd_email)
        # rd_country = customer_search("/api/admin/customer/list",store_id,self.token)[1]
        rd_vip = customer_search("/api/admin/customer/list",store_id,self.token)[2]
        rd_time = customer_search("/api/admin/customer/list",store_id,self.token)[3]
        # 1.2查询邮箱
        result1 = search_email("/api/admin/customer/list", store_id, self.token, r_email)
        self.assertEqual("search email success", result1)
        # 1.3查询国家
        result2 = search_country("/api/admin/customer/list", store_id, self.token)
        self.assertEqual("search country success", result2)
        # 1.4查询注册时间
        result3 = search_invite("/api/admin/customer/list", store_id, self.token, rd_time, rd_time)
        self.assertEqual("search invite success", result3)
        #1.5查询会员等级
        result4 = search_vip("/api/admin/customer/list", store_id, self.token, rd_vip)
        self.assertEqual("search vip success", result4)
        # # #1.6查询数据来源
        # result5 = search_source("/api/admin/customer/list", store_id, self.token,rd_num)
        # self.assertEqual("search sourch success", result5)

    # def test_02subscribe_import(self):
    #     #2.订阅导出
    #     result = export_test("/api/admin/pub/export", self.token, store_id)
    #     self.assertEqual("export success", result)

    # def test_03pull_out(self):
    #     #3.拉取
    #     pass

    # def test_04export(self):
    #     #4.导出
    #     result = export_test("/api/admin/customer/export", self.token, store_id)
    #     self.assertEqual("export success", result)



    def test_05integral(self):
        #5.积分
        #创建测试账号
        register(store_id)
        # print(test_email)
        #1.查询测试邮箱 @chacuo.net
        test_email = search_test_email("/api/admin/customer/list",store_id, self.token)
        # print(test_email)
        #2.查询当前customer_id 积分
        result = self.ad.get_integral("/api/admin/customer/list",store_id, self.token,test_email)
        integral = result[0]
        customer_id =result[1]
        # print(integral,customer_id)
        #3.增加10积分
        result1 = self.ad.add_integral("/api/admin/credit/edit",store_id, self.token,customer_id)
        self.assertEqual("add integral success",result1)
        #4.再次查询当前customer_id 积分
        result2 = self.ad.get_integral("/api/admin/customer/list", store_id, self.token, test_email)
        next_integral = result2[0]
        # print(next_integral)
        assert int(next_integral) == int(integral) + int(10)


    def test_06experience(self):
        #6.经验
        # 1.查询测试邮箱 @chacuo.net
        test_email = search_test_email("/api/admin/customer/list", store_id, self.token)
        # print(test_email)
        # 2.查询当前customer_id 经验值
        result = self.ad.get_exp("/api/admin/customer/list", store_id, self.token, test_email)
        exp = result[0]
        customer_id = result[1]
        # print(exp,customer_id)
        # 3.增加10经验值
        result1 = self.ad.add_experience("/api/admin/exp/edit", store_id, self.token, customer_id)
        self.assertEqual("add exp success", result1)
        # 4.再次查询当前customer_id 经验值
        result2 = self.ad.get_exp("/api/admin/customer/list", store_id, self.token, test_email)
        next_exp = result2[0]
        # print(next_exp)
        assert int(next_exp) == int(exp) + int(10)

    def test_07page_turning(self):
        #7.会员列表翻页
        result = pages_turning("/api/admin/customer/list", store_id, self.token)
        self.assertEqual("pages turning success", result)

    # @classmethod
    # def tearDownClass(cls):
    #     pass

if __name__ == '__main__':
    unittest.main()


