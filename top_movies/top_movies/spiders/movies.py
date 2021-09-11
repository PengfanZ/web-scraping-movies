import scrapy
from ..items import TopMoviesItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['ssr1.scrape.center']
    start_urls = ['http://ssr1.scrape.center/']
    page_offset = 1

    def parse(self, response):
        # parse single page content
        item = TopMoviesItem()
        list_of_movies = response.xpath(
            '//div[@class = "el-card item m-t is-hover-shadow"]')
        for movie in list_of_movies:
            # title = movie.xpath('//a[@class = "name"]/h2/text()').get()  -- not work, only print one movie info
            detail = movie.xpath(
                './div/div/div[@class = "p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16"]')

            # movie title
            title = detail.xpath(
                './a/h2/text()').get()

            # movie categories
            categories = []
            categories_list = detail.xpath(
                './div[@class = "categories"]/button')
            for c in categories_list:
                categories.append(c.xpath('./span/text()').get())

            # movie info
            info = ""
            info_segments = detail.xpath(
                './div[@class = "m-v-sm info"][1]/span')
            for i in info_segments:
                info += i.xpath('./text()').get()

            # movie release date
            release_date = detail.xpath(
                './div[@class = "m-v-sm info"][2]/span/text()').get()

            # movie score
            score = movie.xpath(
                './div/div/div[@class = "el-col el-col-24 el-col-xs-5 el-col-sm-5 el-col-md-4"]/p[@class = "score m-t-md m-b-n-sm"]/text()').get()

            item['movie_title'] = title
            item['movie_categories'] = categories
            item['movie_info'] = info
            item['movie_release_date'] = release_date
            item['movie_score'] = score
            yield item

        # go to the next 8 pages
        if self.page_offset < 8:
            self.page_offset += 1
            next_page = response.xpath('//a[@class = "next"]/@href').get()
            if next_page:
                next_page_url = response.urljoin(next_page)
                yield scrapy.Request(next_page_url, callback=self.parse)

        pass
