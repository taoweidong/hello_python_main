# -*- coding: utf-8 -*-
# 学习链接：https://mp.weixin.qq.com/s/3RHRathfd-xapBlVgFfL7w
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from loguru import logger

# 生成密钥
key = get_random_bytes(16)
# 创建加密器
cipher = AES.new(key, AES.MODE_EAX)
# 加密数据
data = b"Hello World"
ciphertext, tag = cipher.encrypt_and_digest(data)
logger.info(f"加密数据：{tag}")
logger.info(f"加密数据：{ciphertext}")
# 解密数据
cipher_decrypt = AES.new(key, AES.MODE_EAX, cipher.nonce)
decrypted_data = cipher_decrypt.decrypt_and_verify(ciphertext, tag)
logger.info(decrypted_data)
