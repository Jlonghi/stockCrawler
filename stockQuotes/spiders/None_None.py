import scrapy
class QuotesSpider(scrapy.Spider):
	name="None_None"
	start_urls=[
		'http://www.google.ca/finance?q=None%3ANone',
	]
	def parse(self, response):
		yield{
			'price': response.css("span.pr span::text").extract(),
			'change': response.css("div.id-price-change span span::text").extract(),
			'key': response.css("td.key::text").extract(),
			'val':  response.css("td.val::text").extract(),
		}
