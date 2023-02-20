# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for current_item in self.items:

            updater = self.get_updater(current_item)

            updater.update(current_item)

    def get_updater(self, current_item):
        name = current_item.name
        if name == ItemName.aged_brie:
            return UpdateAgedBrie()
        if name == ItemName.passes:
            return UpdatePasses()
        if name == ItemName.conjured:
            return UpdateConjured()
        if name == ItemName.sulfuras:
            return UpdateSulfuras()
        return UpdateRegular()
    
class ItemName:
    aged_brie = "Aged Brie"
    passes = "Backstage passes to a TAFKAL80ETC concert"
    conjured = "Conjured"
    sulfuras = "Sulfuras, Hand of Ragnaros"
        
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
 
class ItemUpdater:
    def update(self, current_item):
        pass

    def increase_quality(self, item, times):
        for x in range(times):
            if item.quality < 50:
                item.quality += 1
    
    def decrease_quality(self, item, times):
        for x in range(times):
            if item.quality > 0:
                item.quality -= 1

    def update_sell_in(self, item):
        item.sell_in -= 1

class UpdateAgedBrie(ItemUpdater):
    def update(self, item):
        self.update_sell_in(item)
        self.increase_quality(item, 1)        
        if item.sell_in < 0:
            self.increase_quality(item, 1)        
    
class UpdatePasses(ItemUpdater):
    def update(self, item):
        self.update_sell_in(item)
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
        self.update_sell_in(item)
        self.decrease_quality(item, 2)
        if item.sell_in < 0:
            self.decrease_quality(item, 2)

class UpdateRegular(ItemUpdater):
    def update(self, item):
        self.update_sell_in(item)
        self.decrease_quality(item, 1)
        if item.sell_in < 0:
            self.decrease_quality(item, 1)

class UpdateSulfuras(ItemUpdater):
    def update(self, item):
        pass