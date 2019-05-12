# -*- coding: utf-8 -*-
import json
from scrapy import Spider, Request
from Cart_Trip.items import CartTripItem


class CartTSpider(Spider):
    name = 'cart_t'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    def start_requests(self):
        for page in range(30000):
            yield Request(
                'https://you.autohome.com.cn/summary/getsearchresultlist?ps=20&pg={}&type=3&tagCode=&tagName=&sortType=3'.format(
                    page), self.parse)

    def parse(self, response):
        result = json.loads(response.text).get('result').get('hitlist')
        item = CartTripItem()
        for page in result:
            item['title'] = page.get('title')
            item['author'] = page.get('author')
            item['authorId'] = page.get('authorId')
            item['publishDate'] = page.get('publishDate')
            item['updateDate'] = page.get('updateDate')
            item['topicId'] = page.get('topicId')
            item['viewCount'] = page.get('viewCount')
            item['replyCount'] = page.get('replyCount')
            item['url'] = 'https://you.autohome.com.cn/' + page.get('url')
            item['content'] = page.get('content')
            yield item
