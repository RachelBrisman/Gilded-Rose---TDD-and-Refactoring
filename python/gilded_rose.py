# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # UPDATE QUALITY
            # regular item
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        # decrease
                        item.quality = item.quality - 1
            else:
                # not sulfuras
                if item.quality < 50:
                    # increase
                    item.quality = item.quality + 1
                    # backstage passes
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        # determine how to increase
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1

            # DECREASE SELL IN
            # not sulfuras
            if item.name != "Sulfuras, Hand of Ragnaros":
                # decrease
                item.sell_in = item.sell_in - 1


            # FOR EXPIRED ITEMS    
            if item.sell_in < 0:
                # not brie
                if item.name != "Aged Brie":
                    # not backstage passes
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        # has quality
                        if item.quality > 0:
                            # not sulfuras
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                # decrease quality - regular item, 2nd decrease
                                item.quality = item.quality - 1
                    # backstage passes            
                    else:
                        # quality is 0
                        item.quality = item.quality - item.quality
                else:
                # is brie
                    if item.quality < 50:
                        # increase while less than 50
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
