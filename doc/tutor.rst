scrapy快速指南
==================
安装项目参考： addbook.cn

项目构建过程：
----------------

1. 切换至工作目录，执行命令::

    ./$scrapy startproject <project>

得到一个项目文件夹Output::

    project/
        -scrapy.cfg         # 项目全局配置文件
        -project/
            -__init__.py
            -items.py       # items，用于缓存解析提取的标签，供后续处理
            -pipelines.py   # 管道文件，用于保存抓取下的数据，通常为items
            -settings.py    # 爬虫的设置文件
            -spiders/
                <yourspiderfile.py> #你自己创建的spider文件

 * 说明：我们应该如何创建构建一个具体的抓取项目呢：
    - 首先我们确定我们抓取的网站地址和页面<URL>,然后在spiders文件夹中穿件一个爬虫文件（命名自定），下面文件具备基本的爬虫功能::
        
        #<testspider.py>
        #coding:utf-8
        import scrapy.spider import Spider
        import scrapy.http import Request
        import scrapy.selector import Selector
        import TestItem


        class TestSpider(Spider):
            name = 'test'       #爬虫必须有名，才能用命令启动
            start_urls = ['http:www.addbook.cn/']   #必须有的字段，且为列表

            def parse(self,response):   #继承于Spider的爬虫类实现该接口，爬虫才能启动
                item = TestItem()
                pass
    
    - 这里需要注意我们的TestItem还未定义，因此要在items.py中定义这个类::

        #<items.py>
        #coding:utf-8

        from scrapy.item import Item, Field
        class TestItem(Item):
            title = Field()  #这些字段可以根据需求自定义，但是必须创建为Field类型
            link = Field()
            desc = Field()
    
    - 定义piplelines,用于输出数据

