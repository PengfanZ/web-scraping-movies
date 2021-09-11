# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TopMoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_title = scrapy.Field()
    movie_categories = scrapy.Field()
    movie_info = scrapy.Field()
    movie_release_date = scrapy.Field()
    movie_score = scrapy.Field()
    pass
