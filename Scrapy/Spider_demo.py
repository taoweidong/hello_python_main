# -*- coding: utf-8 -*-
import logging

from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class DoubanMovieSpider(CrawlSpider):
    name = 'douban_movie'

    start_urls = ['https://movie.douban.com/top250']

    rules = (
        # 提取每部电影页面链接
        Rule(LinkExtractor(allow=r'.*/subject/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.css('span[property="v:itemreviewed"]::text').get()
        rating = response.css('.rating_num::text').get()
        url = response.url
        logger.info(f"片名：{title}   链接：{url}   评分：{rating}")


# 创建爬虫进程
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

# 启动爬虫进程并开始爬取数据
process.crawl(DoubanMovieSpider)
process.start()