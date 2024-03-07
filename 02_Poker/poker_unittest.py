import main
import unittest


class TestPokerMethods(unittest.TestCase):

    @main.timer
    def test_royal_flush(self):
        self.assertFalse(main.royal_flush([1, 2, 3, 4, 5], {main.royal_flush.__name__: 0}))

    @main.timer
    def test_pair(self):
        self.assertTrue(main.pair([10, 1, 5, 4, 1], {main.pair.__name__: 0}))

    @main.timer
    def test_highcard(self):
        self.assertTrue(main.high_card({main.high_card.__name__: 0}))


if __name__ == '__main__':
    unittest.main()
