#coding=utf-8

import random

def get_rd_email():
    try:
        rd_list = []
        for i in range(5):
            register_email = "".join(random.sample("ABCDEFGHIJKabcdefghijklmnopqrst1234567890", 8)) + "." +"a"+ "_" + "@chacuo.net"
            rd_list.append(register_email)
        # print(rd_list)
        rd_email = rd_list[random.randrange(0, len(rd_list))]
        # print(rd_email)
        return rd_email

    except Exception as e:
        print(e)


def get_rd_url():
    try:
        rd_list = []
        for i in range(5):
            random_url = "http://www.baidu.com/"+"".join(random.sample("abcdefghijklmnopqrstqweoiafvnkahovkb",8))
            rd_list.append(random_url)
        rd_url = rd_list[random.randrange(0,len(rd_list))]
        # print(rd_url)
        return  rd_url

    except Exception as e:
        print(e)
if __name__ == '__main__':
    get_rd_email()