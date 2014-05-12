#!/usr/bin/env python
#coding:utf-8
#
# Copy right (c) Addbook.cn
# Author:Yuan Lin
#
# Lisence: BSD

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from urlparse import urljoin
from items import ScrapyCnItem
from scrapy import log
from scrapy.contrib.loader import ItemLoader

class AddbookSpider(Spider):
    name = "Addbook"
    base_domian = "www.addbook.cn/"
    start_urls = ["http://www.addbook.cn"]
    
    def parse(self, response):
        pass
    
    def parse_items(self, response):
        pass
    
    def UrlProcess(self, url):
        pass
    pass