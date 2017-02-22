.PHONY: default
default:
	$(MAKE) scrape
	$(MAKE) html

install:
	pip install scrapy==1.3.2 python-dateutil==2.6.0

scrape:
	scrapy crawl lgn -o lgn.jsonlines

html:
	python to_html.py lgn.jsonlines

push:
	git add *.html mp3
	git commit -mup
	git reset $(git commit-tree HEAD^{tree} -m "up")
	git push -f

all:
	(MAKE) scrape
	(MAKE) html
	(MAKE) push

help:
	@echo "make [scrape html] - scrape and create lgn.html"
	@echo "make scrape        - get new content, idempotent"
	@echo "make html          - turn new content into lgn.html"
	@echo "make push          - push lgn.html and mp3/"
	@echo "make all           - scrape, html and push"
	@echo "make help          - this help"
