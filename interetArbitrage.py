import base64
import gzip
import io

import requests

from aes_utils import decryptAES

def Yt(data, key):
    t = decryptAES(base64.b64decode(data), key)
    with gzip.GzipFile(fileobj=io.BytesIO(bytes.fromhex(t))) as f:
        # 解压缩数据
        decompressed_data = f.read()
    return decompressed_data.decode()

def get_interestArbitrage_data():
    headers = {
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "cache-ts": "1742023231182",
        "encryption": "true",
        "language": "zh",
        "origin": "https://www.coinglass.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.coinglass.com/",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    }
    url = "https://capi.coinglass.com/api/fundingRate/interestArbitrage"
    response = requests.get(url, headers=headers)
    data = response.json()['data']
    user = response.headers.get("user")
    # url_key
    n = base64.b64encode("coinglass/api/fundingRate/interestArbitragecoinglass".encode()).decode()
    n = n[:16]
    n = Yt(user, n)
    i = Yt(data, n)
    return i

print(get_interestArbitrage_data())
