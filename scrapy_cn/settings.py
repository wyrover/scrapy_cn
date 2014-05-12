#!/usr/bin/env python
#coding:utf-8
#
# Copy right (c) Addbook.cn
# Author:Yuan Lin
#
# Lisence: BSD

BOT_NAME = 'scrapy_cn'

SPIDER_MODULES = ['scrapy_cn.spiders']
NEWSPIDER_MODULE = 'scrapy_cn.spiders'

BOT_NAME = 'reminder'

SPIDER_MODULES = ['reminder.spiders']
NEWSPIDER_MODULE = 'reminder.spiders'

#Sets spider pipes
ITEM_PIPELINES = {
                  'scrapy_cn.pipelines.JsonPipeline':200,
                  'scrapy_cn.pipelines.MysqlPipeline':300,
#                  'scrapy.contrib.pipeline.images.ImagesPipeline': 1
                  }
#Sets delay
DOWNLOAD_DELAY = 0.05

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_cn (+http://www.yourdomain.com)'
