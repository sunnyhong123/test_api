#coding=utf-8

import pymysql,random


def connect_mysql(sql,m):
    db = pymysql.connect("47.254.70.94","ptxroot","Ptx@#mpow","ptxcrm_mpow")

    cursor = db.cursor()

    cursor.execute(sql)

    data = cursor.fetchall()
    # print(data)
    db.commit()

    if cursor.rowcount != 0:
        print("数据插入成功:第%s条"%m )


n = 1
while n < 10001:
    num = random.randint(1, 99999999999999)
    sql = 'insert into crm_customer_order (store_id,type,customer_id,orderno,ext_type,platform, country' \
          ',ext_id,amount,currency_code,order_status,order_time,warranty_at,ctime,mtime,status,' \
          'pull_num,review_link,review_time,review_status,review_remark,account,brand,task_no,act_id,warranty_date' \
          ',warranty_des) values ' \
          '(1,platform,360449,%s,"Order","shopify","HK",' \
          '"",12,"USD",1,"2020/6/17 2:26:54","2022/6/17 2:26:54","2020/7/10 4:39:48","2020/7/13 20:12:14",1,' \
          '0,"","2019/1/1 0:00:00",-1,"","Sunny_hong@patazon.net",0,"",0,"+2 years","2 years");' % num
    connect_mysql(sql,n)
    n += 1

