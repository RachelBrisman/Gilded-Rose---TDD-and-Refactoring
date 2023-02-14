# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from gilded_rose import Item, GildedRose

# Items needed to test:
#   name never changes
#   quality never exceeds 50
#   regular item
#       sell in goes down by one
#       quality goes down
#       if sell by passed, quality goes 2x as fast
#       quality is never negative
#   aged brie
#       quality increases, not exceeding 50
#   sulfuras
#       no sell by
#       quality always 80
#   backstage passes
#       quality increases, not exceeding 50
#       if sell in is 0 quality is 0
#       if <10 days left, quality increases by 2
#       if <5 days left, quality increases by 3
#   conjured
#       degrade 2x as fast

class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        self.item_1 = Item("foo", 0, 0)


    # test all items that name doesn't change
    @parameterized.expand([
       ("Bread"),
       ("Aged Brie"),
       ("Backstage passes to a TAFKAL80ETC concert"),
       ("Sulfuras, Hand of Ragnaros"),
    ])
    def test_that_name_doesnt_change(self, name):
        self.item_1.name = name
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        
        self.assertEqual(name, self.item_1.name)

    # only relevant for regular items that degrade
    def test_that_quality_is_never_negative(self):
        self.item_1.sell_in = -1
        self.item_1.quality = 0
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        
        self.assertGreaterEqual(self.item_1.quality, 0)
        
    # tests for sulfuras - violation of SRP?
    def test_that_sulfuras_quality_doesnt_change(self):
        self.item_1.name = "Sulfuras, Hand of Ragnaros"
        self.item_1.quality = 80
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        
        self.assertEqual(80, items[0].quality)
    
    def test_that_sulfuras_sell_in_doesnt_change(self):
        self.item_1.name = "Sulfuras, Hand of Ragnaros"
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].sell_in)

    # tests that sell in goes down
    @parameterized.expand([
       ("Bread"),
       ("Aged Brie"),
       ("Backstage passes to a TAFKAL80ETC concert")
    ])
    def test_that_sell_in_decreases(self, name):
        self.item_1.name = name
        self.item_1.sell_in = 4
        items = [self.item_1]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(3, items[0].sell_in)

    def test_regular_item_quality_decrease_before_sell_in(self):
        self.item_1.sell_in = 5
        self.item_1.quality = 20
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(19, items[0].quality)
    
    def test_regular_item_quality_decrease_after_sell_in(self):
        self.item_1.sell_in = -2
        self.item_1.quality = 20
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        
        self.assertEqual(18, items[0].quality)
   
    # test that quality increase for brie and backstage passes
    @parameterized.expand([
       ("Aged Brie"),
       ("Backstage passes to a TAFKAL80ETC concert")
    ])
    def test_that_quality_increases(self, name):
        self.item_1.name = name
        self.item_1.sell_in = 30
        self.item_1.quality = 30
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(31, items[0].quality)

    @parameterized.expand([
       ("Aged Brie"),
       ("Backstage passes to a TAFKAL80ETC concert")
    ])
    def test_that_quality_doesnt_exceed_50(self, name):
        self.item_1.name = name
        self.item_1.sell_in = 3
        self.item_1.quality = 50
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(50, items[0].quality)

    def test_that_backstage_quality_is_0_when_sell_in_is_0(self):
        self.item_1.name = "Backstage passes to a TAFKAL80ETC concert"
        self.item_1.sell_in = 0
        self.item_1.quality = 30
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].quality)

    
#       if <10 days left, quality increases by 2
#       if <5 days left, quality increases by 3

    def test_that_backstage_quality_increases_by_3_when_less_than_5_days(self):
        self.item_1.name = "Backstage passes to a TAFKAL80ETC concert"
        self.item_1.sell_in = 1
        self.item_1.quality = 30
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(33, items[0].quality)

    def test_that_backstage_quality_increases_by_2_when_less_than_10_days(self):
        self.item_1.name = "Backstage passes to a TAFKAL80ETC concert"
        self.item_1.sell_in = 10
        self.item_1.quality = 30
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(32, items[0].quality)

    def test_that_brie_increase_by_2_after_expiration(self):
        self.item_1.name = "Aged Brie"
        self.item_1.sell_in = -4
        self.item_1.quality = 30
        items = [self.item_1]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(32, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
