#coding=utf-8

import pymysql
from config.config import dba_msg

#数据库域名
dba_ip = dba_msg()[0]
#数据库账号
dba_account = dba_msg()[1]
#数据库密码
dba_password = dba_msg()[2]
#需要连接的数据库
dba_connect = dba_msg()[3]


def connect_dba(sql):

    #打开数据库连接
    db = pymysql.connect(dba_ip,dba_account,dba_password,dba_connect)

    #使用cousor方法创建一个游标对象
    cursor = db.cursor()

    #execute方法执行查询语句
    # cursor.execute("select * from amazon_order_au where amazon_order_id = '503-3072604-0940654';")

    cursor.execute(sql)

    #fetchone方法获取第一条结果,返回的是一个对象
    data = cursor.fetchone()
    num = cursor.rowcount
    if num > 0:
        with open(r"C:\Users\Administrator\Desktop\订单号在销参存在.txt","a") as f1:
            f1.write(data[2]+"\n")

    # print(data)
    try:
        if cursor.rowcount > 1:
            print("该订单存在[%d]条产品信息..." % num)
            print("="*40)
        elif cursor.rowcount == 1:
            print("该订单号:%s 在销参数据库存在,状态为:%s" % (data[2], data[30]))
        else:
            # 销参数据库没有该订单号
            print("该订单号:%s 在销参数据库不存在")
            #fetchall 返回全部结果行
            # data = cursor.fetchall()
            # print(data)
    except pymysql.MySQLError as e:
        print(e)
    finally:
        #关闭数据库连接
        db.close()


def connect_dba_only(sql):

    #打开数据库连接
    db = pymysql.connect(dba_ip,dba_account,dba_password,dba_connect)

    #使用cousor方法创建一个游标对象
    cursor = db.cursor()

    #execute方法执行查询语句
    # cursor.execute("select * from amazon_order_au where amazon_order_id = '503-3072604-0940654';")

    cursor.execute(sql)

    #fetchone方法获取第一条结果,返回的是一个对象
    data = cursor.fetchone()
    num = cursor.rowcount
    # print(data)
    try:
        if cursor.rowcount > 1:
            print("该订单存在[%d]条产品信息..." % num)
            print("="*40)
        elif cursor.rowcount == 1:
            print("该订单号:%s 在销参数据库存在,状态为:%s" % (data[2], data[30]))
        else:
            # 销参数据库没有该订单号
            print("该订单号:%s 在销参数据库不存在")
            #fetchall 返回全部结果行
            # data = cursor.fetchall()
            # print(data)
    except pymysql.MySQLError as e:
        print(e)
    finally:
        #关闭数据库连接
        db.close()


def get_order_db(sql):
    db = pymysql.connect(dba_ip,dba_account,dba_password,dba_connect)
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    db.close()
    if cursor.rowcount != 0:
        return data[0]
    else:
        return "get order false"

if __name__ == '__main__':
    # get_order_db("select * from amazon_order_item_uk where amazon_order_item_uk.amazon_order_id = '206-0514125-9237912' ;")

    list_country = ["us","ca","uk","fr","de","ae","au","es","es_071626","in","jp","mx","nl","sg","it"]
    #读TXT文件
    # with open(r"C:\Users\Administrator\Desktop\无标题.txt","r") as f:
    #     values = f.readlines()
    #     print(values)
    #     for i in values:
    #         order_n = i.split(",")[0]
    #         print(order_n)
    #         order = "'%s'"%order_n
    #         for c in list_country:
    #             print("查询订单国家: "+ c)
    #             connect_dba("select * from amazon_order_item_%s where amazon_order_id = %s;"%(c,order))

    order = "'112-8252215-1661805'"
    for c in list_country:
        print("查询订单国家: "+ c)
        connect_dba_only("select * from amazon_order_item_%s where amazon_order_id = %s;"%(c,order))
    # connect_dba1("select * from amazon_order_item_uk where amazon_order_item_uk.amazon_order_id = '206-0514125-9237912' ;")