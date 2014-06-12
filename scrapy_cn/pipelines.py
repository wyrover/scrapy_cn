#!/usr/bin/env python
#coding:utf-8
#
# Copy right (c) Addbook.cn
# Author:Yuan Lin
#
# Lisence: BSD

import json
import codecs

class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json','w',encoding='utf-8')

        def process_item(self, item, spider):
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line.decode("unicode_escape"))
            return item

class MysqlPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):
    def process_item(self, item, spider):
        return item
