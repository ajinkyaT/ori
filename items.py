# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Amazon1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	Item_name = scrapy.Field()
	Item_href = scrapy.Field()
	Model= scrapy.Field()
	Brand=scrapy.Field()
	Energy_Efficiency = scrapy.Field()
	Capacity = scrapy.Field()
	Noise_Level=scrapy.Field()
	Installation_Type=scrapy.Field()
	Part_Number=scrapy.Field()
	Color=scrapy.Field()
	Control_Console=scrapy.Field()
	Voltage=scrapy.Field()
	Wattage=scrapy.Field()
	ASIN=scrapy.Field()
	Best_Sellers_Rank_Category_home_kitchen=scrapy.Field()
	Best_Sellers_Rank_Category_AC=scrapy.Field()
	Offer_Price=scrapy.Field()
	No_of_Reviews=scrapy.Field()
	MRP=scrapy.Field()
	Average_Rating=scrapy.Field()
	Review_1=scrapy.Field()
	Review_2=scrapy.Field()
	Review_3=scrapy.Field()
	Review_4=scrapy.Field()
	Review_5=scrapy.Field()
	Review_6=scrapy.Field()
	Review_7=scrapy.Field()
	Review_8=scrapy.Field()


    
