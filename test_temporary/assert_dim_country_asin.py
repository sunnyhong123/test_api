#coding=utf-8

import pymysql
from config.config import dba_msg

#数据库域名
dba_ip = "192.168.5.231"
#数据库账号
dba_account = "zb"
#数据库密码
dba_password = "zb&123"
#需要连接的数据库
dba_connect = "db_single_product"


def connect_dba(sql):

    #打开数据库连接
    db = pymysql.connect(dba_ip,dba_account,dba_password,dba_connect)

    #使用cousor方法创建一个游标对象
    cursor = db.cursor()

    #execute方法执行查询语句
    cursor.execute(sql)

    # cursor.execute(sql)

    #fetchone方法获取第一条结果,返回的是一个对象
    data = cursor.fetchone()

    # print(data)
    try:
        if  cursor.rowcount == 1:
            print("三级类目为:%s"%data[9])
        elif cursor.rowcount > 1:
            print("该asin 国家 存在多条数据")
        else:
            #销参数据库没有该订单号
            pass
            # print("三级类目不存在")
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
    # get_order_db("select amazon_order_item_us.amazon_order_id from amazon_order_item_us where amazon_order_item_us.order_status = 'Shipped' limit 10;")
    list_country = ["us","ca","uk","fr","de","ae","au","es","es_071626","in","jp","mx","nl","sg","ae_bak","se"]
    order = "'112-8252215-1661805'"
    for i in list_country:
        print("查询订单国家: "+ i)
        connect_dba("select * from amazon_order_item_%s where amazon_order_id = %s;"%(i,order))

    # connect_dba("select * from dim_country_asin where asin = 'X002OMHG2N' and country = 'US';")

    # 1.读取文件信息  asin  站点
    # num = 0
    # with open(r"C:\Users\Administrator\Desktop\mpowtest.txt") as f:
    #     values = f.readlines()
    #     # print(values)
    #     for i in values:
    #         # print(i)
    #         asin = i.split("-")[0]
    #         country = i.split("-")[1].rstrip()
    #         # print(asin,country)
    #         connect_dba("select * from dim_country_asin where asin = '%s' and country = '%s';"%(asin,country))
    #         num += 1
    # print(num)
