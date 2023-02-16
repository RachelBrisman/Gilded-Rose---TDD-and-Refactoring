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
        for current_item in self.items:
            # if sulfuras, skip this item (it doesn't change)
            if current_item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # decrease sell in 
            current_item.sell_in -= 1

            # determine which method to call
            match current_item.name:
                case "Aged Brie":
                    UpdateAgedBrie.update(self, current_item)
                case "Backstage passes to a TAFKAL80ETC concert":
                    UpdatePasses.update(self, current_item)
                case "Conjured":
                    UpdateConjured.update(self, current_item)
                case _:
                    UpdateRegular.update(self, current_item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
 
class ItemUpdater():
    def update(self):
        return

class UpdateAgedBrie(ItemUpdater):
    def update(self, item):
        self.increase_quality(item, 1)
        if item.sell_in < 0:
            self.increase_quality(item, 1)        
    
class UpdatePasses(ItemUpdater):
    def update(self, item):
        if item.sell_in < 0:
            item.quality = 0
        else:
            self.increase_quality(item, 1)

            if item.sell_in < 10:
                self.increase_quality(item, 1)

            if item.sell_in < 5:
                self.increase_quality(item, 1)
    
class UpdateConjured(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item, 2)
        if item.sell_in < 0:
            self.decrease_quality(item, 2)

class UpdateRegular(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item, 1)
        if item.sell_in < 0:
            self.decrease_quality(item, 1)
            
class UpdateSulfuras(ItemUpdater):
    def update(item):
        return