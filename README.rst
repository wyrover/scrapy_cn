Scrapy project as a chinese tutorial 
====================================
scrapy中文学习项目

requirements::

    scrapy >= 0.22
    pymongo

Glance of project
------------------
Components::

   JsonPipelines
   SQLitePipelines
   MongoPipelines

About utils for scrapy:

1. randomproxy

  This scripts is using as proxy download middleware of scapy.

Uasage:

 * enable your settings.py as follow::
	
	# Retry many times since proxies often fail
	RETRY_TIMES = 10
	# Retry on most error codes since proxies fail for different reasons
	RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

	DOWNLOADER_MIDDLEWARES = {
    	'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    	# Fix path to this module
    	'yourspider.randomproxy.RandomProxy': 100,
    	'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
	}
	PROXY_LIST = '/path/to/proxy/list.txt'

 * the `file of /path/to/proxy/list.txt` should be the format as follow::

	http://host1:port
	http://host2:port
	http://host1:port

if your spider use yield as callback，you may need add option::

	if not hxs.select('//get/site/logo'):
    	    yield Request(url=response.url, dont_filter=True)
    

Lisence
===========
   BSD Lisence
