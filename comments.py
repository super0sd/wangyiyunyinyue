import requests
import json

from Crypto.Cipher import AES
from base64 import b64encode

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 请求的方式是post
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1417862046",
    "threadId": "R_SO_4_1417862046"
}

# 服务于d的
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
e = "010001"
i = "wJMyWbI7NrR7humA" # 手动固定的  ->别人的函数中是随机的


def get_encSecKey():    # 由于i是固定的，所以encSecKey就是固定的，c()函数的结果就是固定的
    return "27826f6cb48b5879df7aa738fe6a389af9d798bfac0dff3688aa74935af7d3c75465a1daae82eae5ac8ebe1a39bdb295f4009d38a44d84522dc86296294b0b1ccefa3756ab091f0935bdf878a400cf32a560026ee543f27b710b57d5c21431b121fc76855868155957b51e61cf1d22fd49191db01c63596fc394b32ea3e4c6bd"

# 转化成16的倍数，为下方的加密算法服务
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

# 加密过程
def enc_params(data, key):  # 加密过程
    iv = "0102030405060708" # 偏移量
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)  # 创建加密器
    bs = aes.encrypt(data.encode("utf-8"))  # 加密 加密的内容的长度必须是16的倍数
    ans = str(b64encode(bs), "utf-8")
    return ans  # 转换成字符串返回

# 把参数进行加密
def get_params(data):  # 默认这里接收到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second  # 返回的是params

# 发送请求，
resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})

print(resp.text)