# -*- coding: utf-8 -*-
# 学习链接：https://mp.weixin.qq.com/s/3RHRathfd-xapBlVgFfL7w
from cryptography.fernet import Fernet

# 生成密钥
key = Fernet.generate_key()
# 创建加密器
cipher = Fernet(key)
# 加密数据
data = b"Hello World"
encrypted_data = cipher.encrypt(data)
# 解密数据
decrypted_data = cipher.decrypt(encrypted_data)
print(decrypted_data)
