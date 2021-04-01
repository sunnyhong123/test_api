#coding=utf-8

import requests,json
from config.config import environmental


test_url = environmental()



# 2.导出
def export_test(api_url,token,store_id):

    url = test_url + api_url
    # data = {"store_id": store_id, "operator": "sunny_hong", "token": token}
    data = {"store_id":store_id,"page_size":10,"page":1,"start_time":"","end_time":"","operator":"sunny_hong",
            "token":token,"audit_status":"","account":"","country":""}
    r = requests.post(url=url, data=data)
    result = r.text
    # print(result)
    assert json.loads(result)["code"] == 1
    time_out = json.loads(result)["exeTime"].split(".")[0]
    if int(time_out) > 50000:
        return "search time out"
    url2 = test_url + json.loads(result)["data"]["url"]
    # print(url2)
    r2 = requests.get(url=url2)
    results = r2.text
    # print(results)
    if len(results) > 4:
        # print("导出成功")
        return "export success"
    else :
        return "export fail"