from urllib import request,parse
import requests
# import reques模块
import json,time,random
import hashlib
def md5_jiami(str_data):
    md5_obj = hashlib.md5()
    sign_bytes_data = str_data.encode('utf-8')
    # 调用update()函数，来更新md5_obj值
    md5_obj.update(sign_bytes_data)
    # 返回加密后的str
    sign_str = md5_obj.hexdigest()
    return sign_str

def youdao(word):
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    salt = int(time.time() * 1000 + random.randint(0, 10))
    salt_str = str(salt)
    D = "ebSeFb%=XZ%T[KZ)c(sy!"
    S = "fanyideskweb"
    sign_str = S + word + salt_str + D
    # 调用加密的方法
    sign_md5_str = md5_jiami(sign_str)

    # print(salt)
    data={
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt_str,
        'sign': sign_md5_str,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }
    new_data = parse.urlencode(data)
    # 有道里面的请求头
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        #'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        # 'Content-Length': str(len(new_data)),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-493176930@10.168.8.63; OUTFOX_SEARCH_USER_ID_NCOO=38624120.26076847; SESSION_FROM_COOKIE=unknown; JSESSIONID=aaabYcV4ZOU-JbQUha2uw; ___rl__test__cookies=1534210912076',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',

    }
    req = requests.post(url,data=new_data,headers=headers)
    strs_datas = req.text
    strs_datas = json.loads(strs_datas)
    print(strs_datas['translateResult'][0][0]['tgt'])
    strings = ''
    for i in strs_datas['smartResult']['entries']:
        strings+=i
    print(strings)
if __name__ == '__main__':
    youdao(input("请输入"))