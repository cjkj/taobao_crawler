# -*- coding:utf-8 -*-


class Item:
    """ 商品 """

    def __init__(self, item_id, seller_id, title, area, location, sellerLoc, price, sold, is_crawled):
        self.item_id = item_id
        self.seller_id = seller_id
        self.title = title
        self.area = area
        self.location = location
        self.price = price
        self.sellerLoc = sellerLoc
        self.sold = sold
        self.is_crawled = is_crawled

    def dict(self):
        """ 将数据转化为字典 """
        return {
            'item_id': self.item_id,
            'seller_id': self.seller_id,
            'title': self.title,
            'area': self.area,
            'location': self.location,
            'sellerLoc': self.sellerLoc,
            'price': self.price,
            'sold': self.sold,
            'is_crawled': self.is_crawled
        }


class Rate:
    """ 商品的评论 """

    def __init__(self, rate_id, size_info, rate_content, auctionSku, buyCount, rateDate, useful, anony, item_id):
        self.item_id = item_id
        self.rate_id = rate_id
        self.size_info = size_info
        self.rate_content = rate_content
        self.auctionSku = auctionSku
        self.buyCount = buyCount
        self.rateDate = rateDate
        self.useful = useful
        self.anony = anony

    def dict(self):
        """ 将数据转化为字典 """
        return {
            'rate_id': self.rate_id,
            'size_info': self.size_info,
            'rate_content': self.rate_content,
            'auctionSku': self.auctionSku,
            'buyCount': self.buyCount,
            'rateDate': self.rateDate,
            'useful': self.useful,
            'anony': self.anony,
            'item_id': self.item_id
        }


class FailedUrl:
    """ 用来记录失败的网址 """

    def __init__(self, url):
        self.url = url

    def dict(self):
        """ 将数据转化为字典 """
        return {'url': self.url}
