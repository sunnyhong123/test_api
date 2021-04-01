import requests,json
import random

def get_24email():

    url = "http://24mail.chacuo.net"

    payload = {'data': 'zirolt91468',
                'type': 'renew',
                 'arg': 'd=chacuo.net_f='}
    files = []
    USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
        "Mozilla /5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML, likeGecko) Chrome/75.0.3770.100Safari/537.36"
        ]
    useragent = random.choice(USER_AGENTS)
    headers = {
        "User - Agent": useragent,
        "Cookie":"__cfduid=d4498c8304c1cf096307be1722ccd45131566372939; bdshare_firstime=1566379624679; Hm_lvt_4183351950d6f3ac05fb254f4eec5518=1566614886; cf_clearance=95188eed7fea7df2e73d7465389fb0eb1a21ce3a-1569555894-31536000-150; __gads=Test; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1575018471,1575858720,1576118188; yjs_id=fDE1NzcwODQ0MTQwMjk; ctrl_time=1; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1577153831; mail_ck=56; sid=e715607f6a8def5ffec7d40d82f4614cbd8de42b"
    }

    response = requests.request("POST", url, headers=headers, data = payload, files = files,)

    value = json.loads(response.text.encode('utf8'))["data"][0]
    return value +"@chacuo.net"



if __name__ == "__main__":

    print(get_24email())
    print(type(get_24email()))

