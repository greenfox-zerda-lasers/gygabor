import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_3_and_3_is_6(self):
        self.assertEqual(extend.add(3, 3), 6)

    def test_add_4_and_9_is_13(self):
        self.assertEqual(extend.add(4, 9), 13)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 6, 3), 6)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(7, 11, 5),11)

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,7]), 6)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5,6,7]), 4)

    def test_is_vovel_a(self):
        self.assertFalse(extend.is_vovel('b'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('ú'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('úri'), 'úvúrivi')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kata'), 'kavatava')

if __name__ == '__main__':
    unittest.main()
