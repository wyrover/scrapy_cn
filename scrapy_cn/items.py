#!/usr/bin/env python
#coding:utf-8
#
# Copy right (c) Addbook.cn
# Author:Yuan Lin
#
# Lisence: BSD

from scrapy.item import Item, Field

class ScrapyCnItem(Item):
    title = Field()
    img = Field()
    desc = Field()
    href = Field()
