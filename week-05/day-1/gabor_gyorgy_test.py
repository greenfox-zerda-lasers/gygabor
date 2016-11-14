import gabor_gyorgy_work
import unittest

class Test_your_name_work(unittest.TestCase):

    def test_anagramm_true(self):
        self.assertTrue(gabor_gyorgy_work.anagramm('alma', 'mala'))

    def test_anagramm_uppercase_true(self):
        self.assertTrue(gabor_gyorgy_work.anagramm('Alma', 'mala'))

    def test_anagramm_notstr_true(self):
        self.assertRaises(TypeError, gabor_gyorgy_work.anagramm, 123, 'alma')

    def test_count_letters(self):
        self.assertEqual(gabor_gyorgy_work.count_letters('alma'), {'a': 2, 'm': 1, 'l': 1})

    def test_count_letters_uppercase(self):
        self.assertEqual(gabor_gyorgy_work.count_letters('Alma'), {'a': 2, 'm': 1, 'l': 1})

    def test_count_letters_character(self):
        self.assertRaises(TypeError, gabor_gyorgy_work.count_letters, 'Alma#2%!œ', {'a': 2, 'm': 1, 'l': 1})

if __name__ == '__main__':
    unittest.main()
