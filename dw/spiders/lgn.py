# -*- coding: utf-8 -*-
import logging
import os
from urllib.parse import urljoin

from dateutil.parser import parse
from scrapy import Request
from scrapy.spiders import XMLFeedSpider

from dw.items import DwItem

logger = logging.getLogger(__name__)


class LgnSpider(XMLFeedSpider):
    name = "lgn"
    allowed_domains = ['dw.com']
    start_urls = ['http://rss.dw.com/xml/DKpodcast_lgn_de']

    def parse_node(self, response, node):
        item = DwItem()
        item['date'] = self.normalize_date(node.xpath('//item/pubDate/text()').extract_first())
        item['langsam_filename'] = '%s.mp3' % item['date']
        item['originaltempo_filename'] = 'orig/%s.mp3' % item['date']
        if os.path.exists(os.path.join(self.settings['FILES_STORE'], item['langsam_filename'])):
            logger.debug('%r skipped', item['langsam_filename'])
            return
        item['url'] = node.xpath('//item/link/text()').extract_first()
        item['langsam_url'] = node.xpath('//enclosure/@url').extract_first()
        item['file_urls'] = [item['langsam_url']]
        return Request(item['url'], callback=self.add_html, meta={'item': item})

    def add_html(self, response):
        item = response.meta['item']
        item['html'] = response.xpath('//div[@class="longText"]').extract_first()
        originaltempo_page_url = urljoin(
            response.url,
            response.xpath('//h2[contains(text(),"Originaltempo")]/../@href').extract_first()
        )
        return Request(originaltempo_page_url, callback=self.add_originaltempo, meta={'item': item})

    def add_originaltempo(self, response):
        item = response.meta['item']
        item['originaltempo_url'] = response.xpath('//a[contains(@href, ".mp3")]/@href').extract_first()
        item['file_urls'].append(item['originaltempo_url'])
        return item

    def normalize_date(self, value):
        date_object = parse(value)
        return date_object.strftime('%Y-%m-%d')
