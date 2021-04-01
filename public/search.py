#coding=utf-8

import requests,json,random
from config.config import environmental


test_url = environmental()

#中奖列表
def search(api_url,store_id,token):
    # 1.1.获取中奖列表 邮箱  奖品名称  国家
    url = test_url + api_url
    data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": token}
    r = requests.post(url=url, data=data)
    result = r.text
    # print(result)
    # 获取list中邮箱
    account = json.loads(result)["data"]["data"]
    # print(account)
    list1 = []
    list2 = []
    list3 = []
    for i in account:
        list1.append(i["account"])
        list2.append(i["name"])
        list3.append(i["country"])
    # print(list)
    rd_value = list1[random.randrange(0, len(list1))]
    rd_name = list2[random.randrange(0, len(list2))]
    rd_country = list3[random.randrange(0, len(list3))]
    # print(rd_value)
    return rd_value,rd_name,rd_country



def search_email(api_url,store_id,token,email):
    url = test_url + api_url
    data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": token, "email": email}
    r = requests.post(url=url,data=data)
    result = r.text
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["data"]["pagination"]["total"] > 0
    return "search email success"

def search_prize(api_url,store_id,token,prize_name):
    url = test_url + api_url
    data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": token, "name": prize_name}
    r = requests.post(url=url, data=data)
    result = r.text
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["data"]["pagination"]["total"] >= 1
    return "search prize success"


def search_product(api_url,store_id,token,product_name):
    url = test_url + api_url
    data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": token, "country": "",
            "product_name":product_name}
    r = requests.post(url=url, data=data)
    result = r.text
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["data"]["pagination"]["total"] >= 1
    return "search product success"


#活动审核
def search_prize_list(api_url,store_id,token):
    # 1.1.获取中奖列表 邮箱  奖品名称  国家
    url = test_url + api_url
    data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": token}
    r = requests.post(url=url, data=data)
    result = r.text
    print(result)
    if json.loads(result)["data"]["pagination"]["total"] == 0:
        return None
    # 获取list中邮箱
    account = json.loads(result)["data"]["data"]
    # print(account)
    list1 = []
    list2 = []
    list3 = []
    for i in account:
        list1.append(i["account"])
        list2.append(i["audit_status"])
        list3.append(i["country"])
    # print(list)
    rd_value = list1[random.randrange(0, len(list1))]
    audit_status = list2[random.randrange(0, len(list2))]
    rd_country = list3[random.randrange(0, len(list3))]
    # print(rd_value)
    return rd_value,audit_status,rd_country



def search_not_review(api_url,store_id,token):
    #获取未审核状态邮箱
    url = test_url + api_url
    data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": token,"audit_status":0,
            "account":""}
    r = requests.post(url=url, data=data)
    result = r.text
    # print(result)
    if json.loads(result)["data"]["pagination"]["total"] == 0:
        return None
    # 获取list中邮箱
    account = json.loads(result)["data"]["data"]
    # print(account)
    list1 = []
    for i in account:
        if "@chacuo.net" in i["account"]:
            list1.append(i["account"])
        else:
            print("无未审核链接...")
    # print(list1,list2)
    #选取第一个索引
    if len(list1) == 0:
        return None
    frist_email = list1[0]
    # print(rd_value)
    return frist_email

def review(api_url,store_id,token,id):
    #审核为已通过或者未通过 增加经验 经验明细方式 备注
    url = test_url + api_url
    rd_audit_status = random.randint(1,2)
    # print(rd_audit_status)
    data = {"audit_status":rd_audit_status,"add_type":"1","value":"10","action":"other","remarks":"测试审核通过","id[]": id,
            "store_id":store_id,"token":token,"operator":"sunny_hong"}
    r = requests.post(url=url,data=data)
    result = r.text
    print(result)
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["msg"] == "ok"
    return "review success"

def search_audit_status(api_url,store_id,token,audit_status):
    url = test_url + api_url
    data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": token, "audit_status": audit_status}
    r = requests.post(url=url, data=data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["data"]["pagination"]["total"] > 0
    return "search audit status success"

def pages_turning(api_url,store_id,token):
    #翻页
    #1.访问list接口获取总条数 total
    url = test_url + api_url
    data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong",
            "token":token,"audit_status":"","account":"","country":""}
    r = requests.post(url=url, data=data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    #总条数
    total = json.loads(result)["data"]["pagination"]["total"]
    if total == 0:
        return "pages turning success"
    # print(total)
    #分页数
    total_page = json.loads(result)["data"]["pagination"]["total_page"]
    # print(total_page)
    #2.最后一页显示条数
    last_total = int(total) - (int(total_page)-1)*10
    # print(last_total)

    #3.随机翻页,判断是否成功
    rd_num = random.randint(1,total_page)
    # print(rd_num)
    data2 = {"store_id":store_id,"page_size":10,"page":rd_num,"operator":"sunny_hong",
            "token":token,"audit_status":"","account":"","country":""}
    r2 = requests.post(url=url, data=data2)
    result2 = r2.text
    assert json.loads(result2)["code"] == 1

    #4.判断最后一页显示条数是正确
    data3 = {"store_id":store_id,"page_size":10,"page":total_page,"operator":"sunny_hong",
            "token":token,"audit_status":"","account":"","country":""}
    r3 = requests.post(url=url, data=data3)
    result3 = r3.text
    # print(result3)
    data_num = len(json.loads(result3)["data"]["data"])
    # print(data_num)
    assert json.loads(result3)["code"] == 1
    if last_total == data_num:
        return "pages turning success"
    else:
        return "pages turing fail"

def invite_search(api_url,token,store_id):
    #邀请活动列表查询
    url = test_url +api_url
    data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong","token":token,"account":"","country":""}
    r = requests.post(url,data=data)
    result =  r.text
    print(result)
    #1.获取邮箱 , 国家 , 邀请时间
    assert json.loads(result)["code"] == 1
    if json.loads(result)["data"]["pagination"]["total_page"] == 0:
        return None
    account_list = []
    country_list = []
    time_list = []
    datas = json.loads(result)["data"]["data"]
    for account in datas:
        account_list.append(account["account"])
        if account["country"] != "":
            country_list.append(account["country"])
        time_list.append(account["ctime"])
    #
    # print(account_list)
    rd_email = account_list[random.randrange(0,len(account_list))]
    rd_country = country_list[random.randrange(0,len(country_list))]
    rd_time = time_list[random.randrange(0,len(time_list))]
    return rd_email,rd_country,rd_time


def product_search(api_url, token, store_id):
    # 产品申请页面查询
    url = test_url + api_url
    data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong", "token": token,
            "account": "", "country": ""}
    r = requests.post(url, data=data)
    result = r.text
    # print(result)
    # 1.获取邮箱 , 国家 , 邀请时间
    assert json.loads(result)["code"] == 1
    account_list = []
    country_list = []
    product_list = []
    datas = json.loads(result)["data"]["data"]
    for account in datas:
        account_list.append(account["account"])
        if account["country"] != "":
            country_list.append(account["country"])
        product_list.append(account["product_name"])
    #
    # print(account_list)
    rd_email = account_list[random.randrange(0, len(account_list))]
    rd_country = country_list[random.randrange(0, len(country_list))]
    rd_product = product_list[random.randrange(0, len(product_list))]
    return rd_email, rd_country, rd_product

def customer_search(api_url,store_id,token):
    #会员列表查询
    url = test_url +api_url
    data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong","token":token
        ,"source":"","account":"","country":"","vip":"","isactivate":"","is_has_profile":""}
    r = requests.post(url,data=data)
    result =  r.text
    # print(result)
    #1.获取邮箱 , 国家 , 会员等级,注册时间,数据来源
    assert json.loads(result)["code"] == 1
    account_list = []
    country_list = []
    vip_list = []
    time_list = []
    source_list = []
    datas = json.loads(result)["data"]["data"]
    # print(datas)
    for data in datas:
        account_list.append(data["account"])
        if data["country"] != "":
            country_list.append(data["country"])
        else:
            country_list.append("US")
        vip_list.append(data["vip"])
        time_list.append(data["ctime"])
        source_list.append(data["source_value"])

    # print(account_list)
    rd_email = account_list[random.randrange(0,len(account_list))]
    rd_country = country_list[random.randrange(0,len(country_list))]
    rd_vip = vip_list[random.randrange(0,len(vip_list))]
    rd_time = time_list[random.randrange(0,len(time_list))]
    rd_source = source_list[random.randrange(0,len(source_list))]
    # print(rd_email,rd_country,rd_vip,rd_time,rd_source)
    return rd_email,rd_country,rd_vip,rd_time,rd_source

def search_vip(api_url,store_id,token,vip):
    #根据会员等级查询
    url = test_url + api_url
    data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong","token":token
        ,"source":"","account":"","country":"","vip":vip,"isactivate":"","is_has_profile":""}
    r = requests.post(url,data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["data"]["pagination"]["total"] > 0
    return "search vip success"


def search_source(api_url, store_id, token, source):
    # 根据数据来源查询
    url = test_url + api_url
    data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong", "token": token
        , "source": source, "account": "", "country": "", "vip": "", "isactivate": "", "is_has_profile": ""}
    r = requests.post(url, data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    # assert json.loads(result)["data"]["pagination"]["total"] > 0
    return "search sourch success"

def search_test_email(api_url,store_id,token):
    #查询@chacuo.net邮箱
    url = test_url +api_url
    num = 1
    while True:
        data ={"store_id":store_id,"page_size":10,"page":num,"operator":"sunny_hong",
               "token":token,"source":"","account":"","country":"","vip":"","isactivate":"","is_has_profile":""}
        r = requests.post(url,data)
        result = r.text
        # print(result)
        datas = json.loads(result)["data"]["data"]
        # print(datas)
        email = []
        for data in datas:
            # print(data["account"])
            if "@chacuo.net" in data["account"]:
                email.append(data["account"])
            else:
                continue
        # print(len(email))
        if len(email) == 0:
            num += 1
        else:
            return email[random.randrange(0,len(email))]

def search_by_email(api_url,store_id,token):
    #通过邮箱查询
    url = test_url +api_url
    data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong","token":token
        ,"account":"","country":"","interests":[]}
    r = requests.post(url,data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["msg"] == "ok"
    datas = json.loads(result)["data"]["data"]
    email = []
    for data in datas:
        if data["account"]:
            email.append(data["account"])
        else:
            continue
    if len(email) == 0:
        return  None
    rd_email = email[random.randrange(0,len(email))]
    # print(rd_email)
    data2 = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "dev", "token": token
        , "account": rd_email, "country":"" , "interests": []}
    r = requests.post(url, data2)
    result1 = r.text
    # print(result1)
    assert json.loads(result1)["code"] == 1
    assert json.loads(result1)["msg"] == "ok"
    assert  json.loads(result1)["data"]["pagination"]["total"] == 1
    return "search email success"

def search_country(api_url,store_id,token):
    #通过国家查询
    url = test_url + api_url
    url1 = test_url + "/api/common/dict/storeDictSelect"
    data1 = {
    "type": "country",
    "token": token,
    "store_id" : store_id}
    r1 = requests.post(url1,data1)
    result1 = r1.text
    # print(result1)
    datas = (json.loads(result1)["data"])
    t = datas.keys()
    t_list = []
    for value in t:
        t_list.append(value)
    rd_country = t_list[random.randrange(0,len(t_list))]
    # print(rd_country)
    data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": token, "country": rd_country}
    r = requests.post(url=url, data=data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["msg"] == "ok"
    return "search country success"



def search_invite(api_url,store_id,token,start_time,end_time):
    #通过时间段查询
    url = test_url + api_url
    data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong","token":token,
            "account":"","country":"","start_at":start_time,"end_at":end_time}
    r = requests.post(url,data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["data"]["pagination"]["total_page"] > 0
    return  "search invite success"

def search_interests(api_url,store_id,token,interests):
    #通过兴趣查询
    url = test_url + api_url
    data = {"page_size": 10, "page": 1, "store_id": store_id, "operator": "sunny_hong", "token": token,
            "interests[]": interests}
    r = requests.post(url=url, data=data)
    result = r.text
    assert json.loads(result)["code"] == 1
    # assert json.loads(result)["data"]["pagination"]["total"] >= 1
    return "search interests success"

def search_id_by_email(api_url,store_id,token):
    #查询id
    url = test_url + api_url
    data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong", "token": token
        , "account": "", "country": ""}
    r = requests.post(url, data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["msg"] == "ok"
    return result

def get_rd_value(api_url,store_id,token,value):
    #获取随机数据
    url = test_url +api_url
    data = {"store_id":store_id,"page_size":10,"page":1,"operator":"sunny_hong","token":token
        , "account":"","country": "", "code_type":1}
    r = requests.post(url,data)
    result = r.text
    # print(url)
    # print(data)
    # print(result)
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["msg"] == "ok"
    datas = json.loads(result)["data"]["data"]
    # print(len(datas))
    rd_list = []
    for data in datas:
        if data[value]:
            rd_list.append(data[value])
        else:
            continue
    if len(rd_list) == 0:
        return  None
    rd_value = rd_list[random.randrange(0,len(rd_list))]
    return rd_value


def get_frist_value(api_url,store_id,token,value):
    #获取查询结果第一行数据
    url = test_url + api_url
    data = {"store_id": store_id, "page_size": 10, "page": 1, "operator": "sunny_hong", "token": token
        , "account": "", "country": ""}
    r = requests.post(url, data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    assert json.loads(result)["msg"] == "ok"
    if json.loads(result)["data"]["pagination"]["total_page"] == 0:
        return None
    datas = json.loads(result)["data"]["data"]
    return datas[0][value]

def public_post(api_url, data,file= None):
    '''请求公共方法'''
    try:
        url = test_url + api_url
        r = requests.post(url, data ,files= file)
        result = r.text
        if json.loads(result)["code"] == 1:
            return result
        else:
            return "requests is False"
    except Exception as e:
        return e



if __name__ == '__main__':
    pass
