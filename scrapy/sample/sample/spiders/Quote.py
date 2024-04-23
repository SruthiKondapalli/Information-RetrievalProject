import scrapy

class QuoteSpider(scrapy.Spider):
    name = "Quote"
    
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # Extracting quotes
        for quote in response.css("div.quote"):
            yield {
                "url": response.url,
                "title": quote.css("span.text::text").get(),
                "content": quote.css("span small.author::text").get(),
            }

        # Follow pagination link
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
