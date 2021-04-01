#coding=utf-8
import random

def error_email():
    try:
        rd_list = []
        for i in range(5):
            email = "".join(
                random.sample("QWERTYabcdefghjkl1234567890", 8)) + "." + "a" + "_" + "chacuo.net"
            rd_list.append(email)
        # print(rd_list)
        rd_email = rd_list[random.randrange(0, len(rd_list))]
        # print(rd_email)
        return rd_email
    except Exception as e:
        print(e)



if __name__ == "__main__":
    error_email()