import scrapy
class QuoteTutorialItem(scrapy.Item):
    Full_Name = scrapy.Field()
    Image_Link = scrapy.Field()
    Biography = scrapy.Field()

import re
import pandas as pd
class BioSpider(scrapy.Spider):

    name = 'bio'

    # celeb
    names = pd.read_csv(r"C:\Users\rohit\PycharmProjects\Bollywood_Celebs\bollywood\celeb-names.csv")
    start_urls = [
        'https://www.bollywoodlife.com/celeb/ananya-panday/'
    ]

    # next_name = names.iloc[1][1]
    # next_name = next_name.replace(" ","-")
    i = 0
    def parse(self, response):

        item = QuoteTutorialItem()


        celeb = response.css('#profile p').extract()
        # if celeb[1]:
        #     s= celeb[1]
        # else:
        #     s = []
        if len(celeb) == 1:
            s = celeb[0]
        elif celeb!= []:
            s = celeb[1]
        else:
            s = ""
        start = '<p>'
        end = '</p>'
        if s != "":
            Biography = s[s.find(start) + len(start):s.rfind(end)]
        else:
            Biography = ""
        Image_link = BioSpider.names.iloc[BioSpider.i][0]
        Full_name = BioSpider.names.iloc[BioSpider.i][1]
        next_name = BioSpider.names.iloc[BioSpider.i+1][1]
        next_name = next_name.replace(" ", "-")
        next_page = 'https://www.bollywoodlife.com/celeb/'+next_name

        item['Full_Name'] = Full_name
        item['Image_Link'] = Image_link
        item['Biography'] = Biography
        yield item

        if BioSpider.i <= 50:
            BioSpider.i += 1
            yield response.follow(next_page, callback=self.parse)

