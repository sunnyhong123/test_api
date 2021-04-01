#coding=utf-8
import unittest,time
from test_temporary.mpow import MpowOrder , Brandwtest
from public.reader_csv import reader_text

store_id = reader_text(r"\data\store_id.txt")


class Warranty(unittest.TestCase):
    def setUp(self):
        """store_id = 1 mpow
           store_id = 2 vt """
        if store_id in ["1","2","3","6","8","9","11",'12']:
            self.w = MpowOrder(store_id)
            self.b = Brandwtest(store_id)
            self.email = "alexhong465@gmail.com"
    def test_01add_gift_card(self):
        """后台添加礼品卡类型奖励"""
        self.b.add_gift_card()

        order_list = [ "114-8992647-8065856",    # US  B07BB99WBR
                        "302-2560472-1909157",   # DE  B07JMRNK6L
                        "402-3323194-3365941",   # IT  B06Y5PNMZB
                        "406-1514328-5568326",   # ES  B07JN4K7NL
                        "408-7207795-1474736",   # FR  B06XZ63KY3
                        "250-1879415-6824664"]   # JP  B01LYATOEL
        n = 0
        for order in order_list:
            self.w.login_order(order, self.email)  # 登录延保
            self.w.input_start(order, self.email, 4)  # 评星
            # img_url = a.upload()
            self.w.input_url_picture(self.email, order)  # 提交RV
            result = self.b.audit_award()    #审核通过
            self.assertEqual("success",result)
            n += 1
            time.sleep(2)
        print("====已发送%s 邮件（审核通过%s封其他奖励类型====）" % (2 * n, n))

    def test_02add_coupon(self):
        """添加折扣码类型"""
        self.b.add_coupon()
        order_list = ["113-3128506-9057042",  # US  B0794WBPHK
                      "302-7814785-0113962",  # DE  B07H85W5XL
                      "405-6915276-4057164",  # IT  B07PMXB4MK
                      "405-8715463-0012321",  # ES  B06XRRGL2Z
                      "407-2726492-0969144",  # FR  B07BKS69H8
                      "250-6420282-2030228"]  # JP  B07BL25MRG
        n = 0
        for order in order_list:
            self.w.login_order(order, self.email)  # 登录延保
            self.w.input_start(order, self.email, 4)  # 评星
            # img_url = a.upload()
            self.w.input_url_picture(self.email, order)  # 提交RV  /  折扣码自动审核成功
            n += 1
            time.sleep(2)
        print("====已发送%s 邮件（审核通过%s封其他奖励类型====）" % (2 * n, n))


    def test_03add_reward(self):
        """添加实物奖励类型"""
        asin = "B078NC6Y3J,B07QNV8HW4,B07KWMRL4V,B07H4C631K,B01CL3M1P0,B074Z31VDB"
        country = "US,DE,IT,ES,FR,JP"
        self.b.add_reward(asin,country)

        order_list = ["113-1878931-4408248",  # US  B078NC6Y3J
                      "304-6942937-8772367",  # DE  B07QNV8HW4
                      "408-5427355-6661165",  # IT  B07KWMRL4V
                      "402-6740828-2125902",  # ES  B07H4C631K
                      "406-1067634-3903511",  # FR  B01CL3M1P0
                      "250-5635353-8236660"]  # JP  B074Z31VDB
        n = 0
        for order in order_list:
            self.w.login_order(order, self.email)  # 登录延保
            self.w.input_start(order, self.email, 4)  # 评星
            # img_url = a.upload()
            self.w.input_url_picture(self.email, order)  # 提交RV
            result = self.b.audit_award()  # 审核通过
            self.assertEqual("success", result)
            n += 1
            time.sleep(2)
        print("====已发送%s 邮件（审核通过%s封其他奖励类型====）" % (2 * n, n))

    def test_04add_points(self):
        """添加积分类型"""
        asin = "B01FZ3BR5S,B0798LP725,B01N5KDGGE,B07C1KPYY9,B074W7TLNZ,B07J9ZVY9F"
        country = "US,DE,IT,ES,FR,JP"
        self.b.add_points(asin, country)

        order_list = ["112-9828437-3745050",  # US  B01FZ3BR5S
                      "305-2257952-3584355",  # DE  B0798LP725
                      "404-1212153-0238702",  # IT  B01N5KDGGE
                      "404-3326130-8291540",  # ES  B07C1KPYY9
                      "408-9614849-9450764",  # FR  B074W7TLNZ
                      "503-7501198-0416641"]  # JP  B07J9ZVY9F
        n = 0
        for order in order_list:
            self.w.login_order(order, self.email)  # 登录延保
            self.w.input_start(order, self.email, 4)  # 评星
            # img_url = a.upload()
            self.w.input_url_picture(self.email, order)  # 提交RV
            n += 1
            time.sleep(2)
        print("====已发送%s 邮件（审核通过%s封其他奖励类型====）" % (2 * n, n))

    @unittest.skip(reason="跳过当前测试用例")
    def test_05add_other(self):
        """添加其他奖励"""
        asin = "B01K7OHDKS,B07HCVR5J7,B078VZMH7Y,B07Q365LCH,B07JDZQ4BH,B07C5LWPJN"
        country = "US,DE,IT,ES,FR,JP"
        self.b.add_other(asin, country)

        order_list = ["114-3960790-2451421",  # US  B01K7OHDKS
                      "305-5643828-3109119",  # DE  B07HCVR5J7
                      "405-8133379-9820355",  # IT  B078VZMH7Y
                      "408-8182632-2294735",  # ES  B07Q365LCH
                      "403-2690724-4749925",  # FR  B07JDZQ4BH
                      "249-6053351-9766213"]  # JP  B07C5LWPJN
        n = 0
        for order in order_list:
            self.w.login_order(order, self.email)  # 登录延保
            self.w.input_start(order, self.email, 4)  # 评星
            # img_url = a.upload()
            self.w.input_url_picture(self.email, order)  # 提交RV
            result = self.b.audit_award()  # 审核通过
            self.assertEqual("success", result)
            n +=1
            time.sleep(2)
        print("====已发送%s 邮件（审核通过%s封其他奖励类型====）"%(2*n,n))

    # def tearDown(self):
    #     #数据还原，删除创建的奖励，删除账号
    #     ids = self.b.get_add_id()
    #     self.b.delete_prize(ids)
    #     self.b.delete_email(self.email)
    #     print("====创建奖励与账号已删除====")

if __name__ == '__main__':
    unittest.main()

