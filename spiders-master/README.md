# 爬虫演示

针对静态、ajax以及HTTP API三种不同技术方案的网站进行抓取演示。

演示的抓取目标为 https://github.com/CUCSec/simple-flask-website

其中对应关系如下：

static_website_spider/simple_spider.py -> simple-flask-website/static_website/

dynamic_website_spider/spider_with_selenium.py -> simple-flask-website/dynamic_website/

dynamic_website_spider/spider_with_api.py -> simple-flask-website/dynamic_website/

后两个的区别详见 [dynamic_website_spider/README.md](dynamic_website_spider/README.md) 。

最后的 [scrapy](scrapy/README.md) 是一个演示如何使用 scrapy 来实现持久化大量数据抓取的例子。