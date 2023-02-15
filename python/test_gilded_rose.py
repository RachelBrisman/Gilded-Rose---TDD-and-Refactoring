# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from gilded_rose_mine import Item, GildedRose

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
        self.gilded_rose = GildedRose([self.item_1])

    # does this help? lets say we want to leave some of the initial values, like "foo"
    def set_instance_vars_for_item(self, name, sell_in, quality):
        if name is not None:
            self.item_1.name = name
        if sell_in is not None:
            self.item_1.sell_in = sell_in 
        if quality is not None:
            self.item_1.quality = quality

    # test all items that name doesn't change
    @parameterized.expand([
       ("Bread"),
       ("Aged Brie"),
       ("Backstage passes to a TAFKAL80ETC concert"),
       ("Sulfuras, Hand of Ragnaros"),
    ])
    def test_that_name_doesnt_change(self, name):
        self.set_instance_vars_for_item(name, None, None)

        self.gilded_rose.update_quality()
        
        self.assertEqual(name, self.item_1.name)

    # only relevant for regular items that degrade
    def test_that_quality_is_never_negative(self):
        self.set_instance_vars_for_item(None, 4, 0)

        self.gilded_rose.update_quality()
        
        self.assertGreaterEqual(self.item_1.quality, 0)
        
    def test_that_sulfuras_quality_doesnt_change(self):
        self.set_instance_vars_for_item("Sulfuras, Hand of Ragnaros", None, 80)

        self.gilded_rose.update_quality()
        
        self.assertEqual(80, self.item_1.quality)
    
    def test_that_sulfuras_sell_in_doesnt_change(self):
        self.set_instance_vars_for_item("Sulfuras, Hand of Ragnaros", None, None)

        self.gilded_rose.update_quality()
        
        self.assertEqual(0, self.item_1.sell_in)

    # tests that sell in goes down
    @parameterized.expand([
       ("Bread"),
       ("Aged Brie"),
       ("Backstage passes to a TAFKAL80ETC concert")
    ])
    def test_that_sell_in_decreases(self, name):
        self.set_instance_vars_for_item(name, 4, None)

        self.gilded_rose.update_quality()

        self.assertEqual(3, self.item_1.sell_in)

    def test_regular_item_quality_decreases_by_1_before_sell_in(self):
        self.set_instance_vars_for_item(None, 5, 20)

        self.gilded_rose.update_quality()

        self.assertEqual(19, self.item_1.quality)
    
    @parameterized.expand([
        ("0"),
        ("-2")
    ])
    def test_regular_item_quality_decreases_by_2_after_sell_in(self, sell_in):
        self.set_instance_vars_for_item(None, int(sell_in), 20)

        self.gilded_rose.update_quality()
        
        self.assertEqual(18, self.item_1.quality)
   
    # test that quality increase for brie and backstage passes
    @parameterized.expand([
       ("Aged Brie"),
       ("Backstage passes to a TAFKAL80ETC concert")
    ])
    def test_that_quality_increases(self, name):
        self.set_instance_vars_for_item(name, 30, 30)

        self.gilded_rose.update_quality()

        self.assertEqual(31, self.item_1.quality)

    @parameterized.expand([
       ("Aged Brie"),
       ("Backstage passes to a TAFKAL80ETC concert")
    ])
    def test_that_quality_doesnt_exceed_50(self, name):
        self.set_instance_vars_for_item(name, 3, 50)

        self.gilded_rose.update_quality()

        self.assertEqual(50, self.item_1.quality)

    def test_that_backstage_quality_is_0_when_sell_in_is_less_than_0(self):
        self.set_instance_vars_for_item("Backstage passes to a TAFKAL80ETC concert", 0, 30)

        self.gilded_rose.update_quality()

        self.assertEqual(0, self.item_1.quality)

    
#       if <10 days left, quality increases by 2
#       if <5 days left, quality increases by 3

    @parameterized.expand([
        ("1"),
        ("3"),
        ("5")
    ])
    def test_that_backstage_quality_increases_by_3_when_less_than_5_days(self, sell_in):
        self.set_instance_vars_for_item("Backstage passes to a TAFKAL80ETC concert", int(sell_in), 30)

        self.gilded_rose.update_quality()

        self.assertEqual(33, self.item_1.quality)

    @parameterized.expand([
        ("6"),
        ("8"),
        ("10")
    ])
    def test_that_backstage_quality_increases_by_2_when_less_than_10_days(self, sell_in):
        self.set_instance_vars_for_item("Backstage passes to a TAFKAL80ETC concert", int(sell_in), 30)
        
        self.gilded_rose.update_quality()

        self.assertEqual(32, self.item_1.quality)

    @parameterized.expand([
        ("0"),
        ("-2")
    ])
    def test_that_brie_increase_by_2_after_expiration(self, sell_in):
        self.set_instance_vars_for_item("Aged Brie", int(sell_in), 30)

        self.gilded_rose.update_quality()

        self.assertEqual(32, self.item_1.quality)
        
if __name__ == '__main__':
    unittest.main()
