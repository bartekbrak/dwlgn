# Bartek Brak Deutsche Welle Langsam Gesprochene Nachrichten scraper and archive.

I like **Deutsche Welle Langsam Gesprochene Nachrichten** as a learning resource a lot. I don't like 
visiting their website, it's cluttered and slow as the rest of the modern Internet. So I wrote this 
scraper to just get the data and display it in a minimalist manner. 

What it does:
* Scrape the official [LGN RSS](http://rss.dw.com/xml/DKpodcast_lgn_de) to `lgn.jsonlines`.
* Download the mp3 files, two versions, slow and original tempo.
* Glue the text with metadata and audio into continuous file `lgn.html`. 

It's idempotent, it won't re-download files it already has.

# Install and run

In dedicated Python 3.6+ virtual env:

```
make install
make
# optionally, to store the files in a repository
make push
xdg-open lgn.html
```

# Screenshot

![alt tag](https://raw.githubusercontent.com/bartekbrak/dwlgn/master/screen.png)


# To do
I'd like to be able to control last touched audio player with keyboard, pause, rewind few seconds 
with keyboard.
