import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def decryptAES(en_text, key):
    key = key.encode('utf-8') if isinstance(key, str) else key
    en_text = en_text.encode('utf-8') if isinstance(en_text, str) else en_text
    # AES.MODE_ECB 表示模式是ECB模式
    #创建一个aes对象
    aes = AES.new(
        key, 
        AES.MODE_ECB,
    ) 
    den_text = aes.decrypt(pad(en_text, AES.block_size)) # 解密密文
    return den_text.hex()
