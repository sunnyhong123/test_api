#coding=utf-8

# import requests,random,json,datetime
#
#
# #活动id
# act_id = 5
# test_url = "https://testapi.patozon.net"
# release_url = "https://brandwtest.patozon.net"
# brand_url = "https://brand.patozon.net"
#
#
# orderno = "112-5385779-2689042"
#
# def register(store_id):
#     #注册官网账号
#     #获取随机邮箱
#     rd_email = "".join(random.sample("abcdefgqweruiopzxcvbn1234678090", 8)) + "@chacuo.net"
#     # print(rd_email)
#     # rd_email = "jlbkvs04789@chacuo.net"
#     rd_ip = "".join(random.sample("1234567890",3))+"."+"".join(random.sample("1234567890",3))+"."+"".join(random.sample("1234567890",3))
#     # rd_email = "sunnyhong1993@yahoo.com"
#     url = release_url + "/api/shop/customer/createCustomer"
#     #"app_env":"sandbox"
#     data = {"platform":"Shopify","action":"register","act_id":act_id,"store_id":store_id,"account":rd_email,"client_access_url":"https://litom.com/pages/black-friday-progress?id=100&type=1&apply_id=2721",
#             "orderno":"","order_country":"US","password":"123456","invite_code":"WJ4b5AV2","ip":rd_ip,"country":"HK",
#             "accepts_marketing":1,"source":2}
#     # print(data)
#     r = requests.post(url, data)
#     result = r.text.encode('utf-8')
#     # print(result)
#     assert json.loads(result)["code"] == 1
#     return rd_email
#
#
# if __name__ == '__main__':
#     # print(register())
#     for i in range(1,6):
#         print(register(6))
#
# import requests
#
# url = "https://release-api.patozon.net/api/admin/reward/add"
#
# payload={'name': '10 gift card',
# 'type': '1',
# 'business_type': '1',
# 'reward_status': '2',
# 'store_id': '11',
# 'operator': 'Sunny_hong(洪磊)',
# 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwYXRvem9uLm5ldCIsImlhdCI6MTYxNDU2MTkxNiwiaWQiOiI3NjgifQ.eRYembKV9CA9pidB0yWtKBWKABt4Aq_IJ89ClTMDUwo',
# 'category_data': '[{"category_code":"AR","category_name":"艺术手工","level":1},{"category_code":"AR01","category_name":"手工制作","level":2},{"category_code":"AR0103","category_name":"胶枪","level":3}]'}
# files = {"file":open("F:\\test_vt_brand\\data\\reward_gift_card_template (1).xlsx","rb")}
# headers = {
#   'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryei32LJjMgzlrJHPh'
# }
# print(1111)
# response = requests.request("POST",url, data=payload, files=files,headers=headers)
# print(response)
#
# print(response.text)

# import xlrd
# class ExcelUtil(object):
#     def __init__(self,execlPath,sheetName):
#         self.data = xlrd.open_workbook(execlPath)
#         self.table = self.data.sheet_by_name(sheetName)
#         #取第一行等于key的值
#         self.keys = self.table.row_values(0)
#         # print(self.keys)
#         #获取总行数
#         self.row_num = self.table.nrows
#         # print(self.row_num)
#         #获取总列数
#         self.col_num = self.table.ncols
#         # print(self.col_num)
#
#
#     def dict_data(self):
#         #判断行数是否小于1
#         if self.row_num <= 1:
#             print("总行数小于1行")
#         else:
#             dice_list = []
#             j = 1
#             for i in range(self.row_num - 1):
#                 s = {}
#                 #从第二行取值
#                 values = self.table.row_values(j)
#                 # print(values)
#                 for x in range(self.col_num):
#                     s[self.keys[x]] = values[x]
#                 dice_list.append(s)
#                 j += 1
#             return dice_list
#
# if __name__ == '__main__':
#     filepath = r"C:\Users\sunny_hong\Desktop\xmind思维导图转化用例工具\2021_02_04_11_12_03_sunny.xls"
#     sheetname = "sheet1"
#     data = ExcelUtil(filepath,sheetname)
#     print(data.dict_data())

import time

print(time.time())
print(time.ctime())
print(time.strftime("%Y_%m_%d %H:%M:%S"))