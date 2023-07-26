import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        dataPoint = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)
        self.assertEqual(getDataPoint(quote), dataPoint)
        self.assertEqual(1, 1)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       dataPoint = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
       self.assertEqual(getDataPoint(quote), dataPoint)
       self.assertEqual(1, 1)

  """ ------------ Add more unit tests ------------ """


  def test_getRatio_normalCase(self):
     price_a = 10.0
     price_b = 5.0
     expected_ratio = price_a / price_b
     self.assertEqual(getRatio(price_a, price_b), expected_ratio)

  def test_getRatio_priceBisZero(self):
     price_a = 10.0
     price_b = 0.0
     # When price_b is zero, the ratio should return None to avoid division by zero.
     self.assertIsNone(getRatio(price_a, price_b))

  def test_getRatio_priceAisZero(self):
   price_a = 0.0
   price_b = 5.0
  # When price_a is zero, the ratio should be 0.
   self.assertEqual(getRatio(price_a, price_b), 0)

if __name__ == '__main__':
    unittest.main()
