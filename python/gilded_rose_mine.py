# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def decrease_quality(self, item):
        item.quality = item.quality - 1

    def increase_quality(self, item):
        item.quality = item.quality + 1

    def update_brie_quality(self, item):
        self.increase_quality(item)
        if item.sell_in < 0:
            self.increase_quality(item)
        
        if item.quality >= 50:
            item.quality = 50
    
    def update_passes_quality(self, item):
        if item.sell_in < 0:
            item.quality = 0
            return
        
        self.increase_quality(item)

        if item.sell_in < 10:
            self.increase_quality(item)

        if item.sell_in < 5:
            self.increase_quality(item)

        if item.quality >= 50:
            item.quality = 50

    def update_regular_item_quality(self, item):
        self.decrease_quality(item)
        if item.sell_in < 0:
            self.decrease_quality(item)

        if item.quality <= 0:
            item.quality = 0

    def update_quality(self):
        for current_item in self.items:
            # if sulfuras, skip this item (it doesn't change)
            if current_item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # decrease sell in 
            current_item.sell_in -= 1

            # determine which method to call
            match current_item.name:
                case "Aged Brie":
                    self.update_brie_quality(current_item)
                case "Backstage passes to a TAFKAL80ETC concert":
                    self.update_passes_quality(current_item)
                case _:
                    self.update_regular_item_quality(current_item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
