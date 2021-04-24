from ..items import PdfUrlsItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re



class PdfUrlSpider(CrawlSpider):


	name ='pdf_url'

	allowed_domains=['adobe.com']

	start_urls=['https://www.adobe.com']

	rules=[Rule(LinkExtractor(allow=''),callback="parse_httpresponse",follow=True)]


	def parse_httpresponse(self,response):

		if response.status !=200:
			return None


		self.logger.info('Got sucessful response from {}'.format(response.url))


		if b'Content-Type' in response.headers.keys():
			links_to_pdf = 'application/pdf' in str(response.headers['Content-Type']) #add this code to
		else:
			links_to_pdf=False


		Content_disposition_exists = b'Content-Disposition' in response.headers.keys()


		if links_to_pdf and Content-disposition_exists:

			filename=re.search('filename=(.+)',str(response.headers['Content-Disposition']))

		elif links_to_pdf:

			filename = response.url.split('/')[-1]


		else:

			return None


		item = PdfUrlsItem()
		item['url']=response.url
		item['filename']=filename
		return item