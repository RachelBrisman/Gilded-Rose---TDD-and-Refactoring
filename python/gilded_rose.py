# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:

            # skip sulfuras, don't account for it
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # UPDATE QUALITY
            # regular item
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    # decrease
                    item.quality -= 1
            else:
                # not sulfuras
                if item.quality < 50:
                    # increase
                    item.quality += 1
                    # backstage passes
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        # determine how to increase
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality += 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality += 1

            # DECREASE SELL IN
            item.sell_in -= 1

            # FOR EXPIRED ITEMS, continue to update the quality    
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    if item.quality < 50:
                        item.quality += 1
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                else: # regular item
                    if item.quality > 0:
                        item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
