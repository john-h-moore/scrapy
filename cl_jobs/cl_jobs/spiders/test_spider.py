from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from cl_jobs.items import ClJobsItem

class MySpider(BaseSpider):
	name = 'cljobs'
	allowed_domains = ['craigslist.org']
	start_urls = ['http://raleigh.craigslist.org/search/web?query=+']

	def parse(self, response):
		# hxs = HtmlXPathSelector(response)
		hxs = Selector(response)
		rows = hxs.xpath('//p[@class="row"]')
		for row in rows:
			date = row.xpath('.//span[@class="date"]').xpath('text()').extract()
			link = row.xpath('.//span[@class="pl"]/a')
			loc = row.xpath('.//span[@class="l2"]').xpath('.//span[@class="pnr"]').xpath('.//small/text()').extract()
			title = link.xpath('text()').extract()
			url = link.xpath('@href').extract()
			item = ClJobsItem()
			item['title'] = title
			item['url'] = url
			item['date'] = date
			item['loc'] = loc
			yield item