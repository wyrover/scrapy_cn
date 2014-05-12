#!/usr/bin/env python
#coding:utf-8
#
# Copy right (c) Addbook.cn
# Author:Yuan Lin
#
# Lisence: BSD

class JsonPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):
    def process_item(self, item, spider):
        return item