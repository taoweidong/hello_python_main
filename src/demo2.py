# -*- coding: utf-8 -*-

import requests as requests
from loguru import logger

if __name__ == '__main__':
    query_data = requests.get("https://douban.uieee.com/v2/movie/in_theaters", params={"start": 1, "count": 200},
                              verify=False)

    logger.info(query_data)
