import scrapy
class QuoteTutorialItem(scrapy.Item):
    Name = scrapy.Field()
    Link = scrapy.Field()

class QuoteSpider(scrapy.Spider):


    name = 'quotes'

    # celeb

    start_urls = [
        'https://www.bollywoodlife.com/celeb/'
    ]
    def parse(self, response):

        item = QuoteTutorialItem()


        all_celebs = response.css('a.img_alink').extract()


        #To select only the first 50 elements
        for i in range(0,50):
            celeb = all_celebs[i]
            celeb = celeb.split("=")
            name = celeb[2]


            start = '"'
            end = '"'
            s = name
            name = s[s.find(start) + len(start):s.rfind(end)]


            img = celeb[5]
            img = img.split()

            img = img[0]
            final_name = name
            final_img = img[1:-1]
            # print(final_name)
            # print(final_img)

            item['Name'] = final_name
            item['Link'] = final_img
            yield item
