#coding=utf-8
import unittest
from public.login_test_brand import login_test_brand
from public.delete_email import delete_email
from public.register import register
from public.reader_csv import reader_text

store_id = reader_text(r"\data\store_id.txt")

class MemberList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.token = login_test_brand(store_id)
        cls.email = register(store_id)
        # print(cls.email)

    def test_01detete(self):
        #1.删除邮箱账号
        result = delete_email("/api/admin/customer/forceDelete",store_id,self.token,self.email)
        self.assertEqual("delete email success",result)


    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()

