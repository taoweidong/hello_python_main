# -*- coding: utf-8 -*-
# 学习链接：https://mp.weixin.qq.com/s/3RHRathfd-xapBlVgFfL7w

import jwt
from loguru import logger

# 生成令牌
payload = {"user_id": 1234, "username": "john.doe"}
secret_key = "secret_key"
token = jwt.encode(payload, secret_key, algorithm="HS256")
# 验证令牌
decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
logger.info(decoded_token)
