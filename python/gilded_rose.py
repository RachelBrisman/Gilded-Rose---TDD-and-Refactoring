# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def increase_quality(self, item, times):
        for x in range(times):
            if item.quality < 50:
                item.quality += 1
    
    def decrease_quality(self, item, times):
        for x in range(times):
            if item.quality > 0:
                item.quality -= 1

    def update_quality(self):
        for item in self.items:

            # SKIP SULFURAS
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # UPDATE QUALITY
            if item.name == "Aged Brie":
                self.increase_quality(item, 1)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.increase_quality(item, 1)
                if item.sell_in < 11:
                    self.increase_quality(item, 1)
                if item.sell_in < 6:
                    self.increase_quality(item, 1)
            elif item.name == "Conjured":
                self.decrease_quality(item, 2)
            else: # regular item
                self.decrease_quality(item, 1)
                
            # DECREASE SELL IN
            item.sell_in -= 1

            # FOR EXPIRED ITEMS, continue to update the quality    
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    self.increase_quality(item, 1)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                elif item.name == "Conjured":
                    self.decrease_quality(item, 2)
                else: # regular item
                    self.decrease_quality(item, 1)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    