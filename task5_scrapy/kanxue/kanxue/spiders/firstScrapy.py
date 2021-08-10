import scrapy
import json
from kanxue.items import KanxueItem

# 爬取看雪论坛的精华帖
# 注：由于精华帖共620页，故没有让程序爬完，爬一部分即Ctrl C了
class FirstscrapySpider(scrapy.Spider):
    name = 'firstScrapy'
    start_urls = ['https://bbs.pediy.com/new-digest-1.htm']

    def parse(self, response):
        # 首先处理目的数据
        essences = response.xpath('//*[@id="body"]/div/div[1]/div[2]/table/tbody/tr')
        for essence in essences:
            essence_item = KanxueItem()
            # 文章名称
            title =  essence.xpath('./td/div[1]/a[2]/text()').extract()[0]
            essence_item['title'] = title
            # print(title)
            # 文章评论：包括精华、优秀、关注等几种
            rank = essence.xpath('./td/div[1]/span/i/@title')[0].extract()
            essence_item['rank'] = rank
            # print(rank)
            # 文章发表作者
            username = essence.xpath('./td/div[2]/div[1]/a/text()').extract()[0]
            essence_item['username'] = username
            # print(username)
            # 文章发表时间
            upDate = essence.xpath('./td/div[2]/div[1]/span[1]/text()').extract()[0]
            essence_item['upDate'] = upDate
            # print(upDate)
            # 文章浏览数
            eyeNum = essence.xpath('./td/div[2]/div[2]/span[1]/text()').extract()[0]
            essence_item['eyeNum'] = eyeNum
            # print(eyeNum)
            # 文章评论数
            commentNum = essence.xpath('./td/div[2]/div[2]/span[2]/text()').extract()[0]
            essence_item['commentNum'] = commentNum
            # print(commentNum)
            yield essence_item
        
        # 然后处理后续request
        nextPages = response.xpath('//*[@id="body"]/div/nav/ul/li')
        # print(nextPages)
        # endFlag作用是确定是最后一个链接，即下一页。
        # 处理原因：分页栏在每个页面都是从第一页开始，故下一页链接寻找下一页那个按钮，
        #          为什么不直接解析下一个按钮？ 因为第一页的下一页是' li[12] '，而第二页及以后都是' li[13] '
        #          故判断是最后一页。
        endFlag = 1
        for nextPage in nextPages:
            if endFlag==len(nextPages):
                nextUrl = 'https://bbs.pediy.com/' + nextPage.xpath('./a/@href')[0].extract()
            else:
                endFlag += 1
        # print(nextUrl)
        yield scrapy.Request(url=nextUrl,callback=self.parse)

