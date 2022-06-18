import logging
from typing import Dict, NewType

from scrapy import Item
from scrapy.pipelines.files import FilesPipeline

Url = NewType('Url', str)

logger = logging.getLogger(__name__)


class DwMP3Pipeline(FilesPipeline):
    """ Download two files per item, name them according to the date of the scraped item.
    LGN is daily so no filename conflicts are expected.

    """
    EXPIRES = 1000  # never
    items: Dict[Url, Item] = {}

    def get_media_requests(self, item, info):
        """ Store item objects so that item.date can be accessed from self.file_path """
        for url in item.get(self.files_urls_field, []):
            self.items[url] = item
        return super().get_media_requests(item, info)

    def file_path(self, request, response=None, info=None, *, item=None):
        """ Name the file after the date """
        url = request.url
        item = self.items[url]

        if url == item['langsam_url']:
            file_name = item['langsam_filename']
        elif url == item['originaltempo_url']:
            file_name = item['originaltempo_filename']
        else:
            raise Exception(
                "Couldn't match %r to either %r or %r" % (
                    url, item['langsam_url'], item['originaltempo_url']
                )
            )
        logger.debug('url %r to %r', url, file_name)
        return file_name
