#coding=utf-8
import random

def store():
    # 1 => mpow
    # 2 => vt
    # 3 => holife
    # 5 => ikich
    # 6 => homasy
    # 8 => litom
    # 9 => iseneo
    # 10 => iatmoko
    rd_store_id = [1,2,3,5,6,8,9,10]
    return rd_store_id[random.randrange(0,len(rd_store_id))]


def environmental():
    #环境地址
    return "https://release-api.patozon.net"
# def environmental(type):
#     if type == "test":
#         # 测试环境
#         return "https://testbrand.patozon.net"
#
#     elif type == "release":
#         # 预发布环境
#         return "https://release-api.patozon.net"
#
#     elif type == "brand":
#         #正式环境
#         return "https://brand-api.patozon.net"
#
#     elif type == "24email":
#         #24小时临时邮箱地址
#         return "http://24mail.chacuo.net"
#
#     else:
#         return "unknow error"

def dba_msg():
    return "192.168.5.223","zb","zb&123","apiclean"








