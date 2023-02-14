# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def decrease_sell_in(self, item):
        item.sell_in = item.sell_in - 1

    def decrease_quality(self, item):
        item.quality = item.quality - 1

    def increase_quality(self, item):
        item.quality = item.quality + 1

    def update_brie(self, item):
        self.increase_quality(item)
    
    def update_passes(self, item):
        self.increase_quality(item)

    def update_regular_item(self, item):
        if item.quality > 0:
            self.decrease_quality(item)
        
        if 

    def update_quality(self):
        for current_item in self.items:
            # if sulfuras, skip this item (it doesn't change)
            if current_item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # decrease sell in 
            self.decrease_sell_in(current_item)

            # determine which method to call
            match current_item.name:
                case "Aged Brie":
                    self.update_brie(current_item)
                case "Backstage passes to a TAFKAL80ETC concert":
                    self.update_passes(current_item)
                case _:
                    self.update_regular_item(current_item)

            # DETERMINE QUALITY
            # regular item, decrease
            if current_item.name != "Aged Brie" and \
               current_item.name != "Backstage passes to a TAFKAL80ETC concert" and \
               current_item.name != "Sulfuras, Hand of Ragnaros":
                if current_item.quality > 0:
                    current_item.quality = current_item.quality - 1
            else:
                # not sulfuras
                if current_item.quality < 50:
                    # increase
                    current_item.quality = current_item.quality + 1
                    # backstage passes
                    if current_item.name == "Backstage passes to a TAFKAL80ETC concert":
                        # determine how to increase
                        if current_item.sell_in < 11:
                            if current_item.quality < 50:
                                current_item.quality = current_item.quality + 1
                        if current_item.sell_in < 6:
                            if current_item.quality < 50:
                                current_item.quality = current_item.quality + 1

            


            # FOR EXPIRED ITEMS    
            if current_item.sell_in < 0:
                # not brie
                if current_item.name != "Aged Brie":
                    # not backstage passes
                    if current_item.name != "Backstage passes to a TAFKAL80ETC concert":
                        # has quality
                        if current_item.quality > 0:
                            # not sulfuras
                            if current_item.name != "Sulfuras, Hand of Ragnaros":
                                # decrease quality - regular item, 2nd decrease
                                current_item.quality = current_item.quality - 1
                    # backstage passes            
                    else:
                        # quality is 0
                        current_item.quality = current_item.quality - current_item.quality
                else:
                # is brie
                    if current_item.quality < 50:
                        # increase while less than 50
                        current_item.quality = current_item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
