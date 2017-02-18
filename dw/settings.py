SPIDER_MODULES = ['dw.spiders']

# Sadly, I need to parse some popups, sorry DW.
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    'dw.pipelines.DwMP3Pipeline': 100,
}
FILES_STORE = 'mp3'

LOG_FORMAT = '%(levelname)s [%(name)s]: %(message)s'
