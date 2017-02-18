import scrapy


class DwItem(scrapy.Item):
    date = scrapy.Field()
    url = scrapy.Field()
    html = scrapy.Field()
    file_urls = scrapy.Field()
    langsam_url = scrapy.Field()
    langsam_filename = scrapy.Field()
    originaltempo_url = scrapy.Field()
    originaltempo_filename = scrapy.Field()
