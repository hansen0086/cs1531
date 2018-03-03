from datetime import datetime, timedelta


class Item():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.bid_info = BidInfo()


class Electronic(Item):
    def __init__(self, id, name, description, bid_info, brand, voltage):
        super().__init__(id, name, description, bid_info)
        self.brand = brand
        self.voltage = voltage


class Book(Item):
    def __init__(self, id, name, description, bid_info, author, year):
        super().__init__(id, name, description, bid_info)
        self.author = author
        self.year = year


class Furniture(Item):
    def __init__(self, id, name, description, bid_info, age, material):
        super().__init__(id, name, description, bid_info)
        self.age = age
        self.material = material


class ItemList():
    def __init__(self):
        self.items = []

    def add_item(self, item):
        pass

    def print_items(self):
        pass


class Bid_Info():
    def __init__(self, bidder_id, price,item):
        self.bidder_id = bidder_id
        self.price = price
        self._start_time = datetime.now()
        self._end_time = self._start_time + timedelta(days=2)
        self.item = item


class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.posted_items = []
        self.posted_bids = []

    def add_bid(self, bid):
        pass

    def add_item(self, item):
        pass
