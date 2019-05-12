# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CartTripItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    updateDate = scrapy.Field()
    publishDate = scrapy.Field()
    author = scrapy.Field()
    authorId = scrapy.Field()
    tagName = scrapy.Field()
    url = scrapy.Field()
    topicId = scrapy.Field()
    viewCount = scrapy.Field()
    replyCount = scrapy.Field()



