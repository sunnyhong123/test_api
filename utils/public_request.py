#coding=utf-8
import requests,json

from config.config import TEST_HOST,RELEASE_HOST
from public.reader_csv import reader_csv


#读取接口测试用例数据
datas = reader_csv(r"\data\register_testcase.csv")
# print(datas)


def public_request(url_path,data_value,email):

    # url = TEST_HOST +datas[0]["path"]
    # #测试环境地址
    # url = TEST_HOST + url_path
    # print(url)
    #预发布环境
    url = RELEASE_HOST +url_path

    # data = json.loads(datas[0]["data"])

    #获取随机邮箱替换
    data_value["account"]=email
    # print(data)
    # print(type(data))
    r  = requests.post(url,data=data_value)

    #获取响应
    return r.text

def public_request_json(url_path,data_value,email):
    try:
        # url = TEST_HOST + url_path
        # 预发布环境
        url = RELEASE_HOST + url_path

        data_value["account"]=email

        r = requests.post(url,json=data_value)

        return  r.text


    except Exception as e:
        print(e)


def binding_order_request(url_path,data_value,email,orderno):
    try:
        # url = TEST_HOST +datas[0]["path"]
        # url = TEST_HOST + url_path

        # 预发布环境
        url = RELEASE_HOST + url_path

        # print(url)
        # data = json.loads(datas[0]["data"])
        # 获取随机邮箱替换
        data_value["account"] = email
        data_value["orderno"] = orderno
        # print(data)
        # print(type(data))
        r = requests.post(url, data=data_value)
        # 获取响应
        return r.text
    except Exception as e:
        print(e)


def submit_url_request(url_path,data_value,email,url_value):
    try:
        # url = TEST_HOST +datas[0]["path"]

        # 预发布环境
        url = RELEASE_HOST + url_path
        # print(url)
        # data = json.loads(datas[0]["data"])
        # 获取随机邮箱替换
        data_value["account"] = email
        data_value["url"] = url_value
        # print(data)
        # print(type(data))
        r = requests.post(url, data=data_value)
        # 获取响应
        return r.text
    except Exception as e:
        print(e)





if __name__ == "__main__":
    email = "idhazg012391@chacuo.net"
    result = public_request(datas[0]["path"],json.loads(datas[0]["data"]),email)
    print(result)
