import first_b, two, three
import unittest

class Test_your_name_work(unittest.TestCase):

    def test_null_divide(self):
        self.assertEqual(first_b.divide_ten(0), 'fail')

    def test_string(self):
       self.assertEqual(first_b.divide_ten('sgsfg'), 'Number please!')

    def test_file_exists(self):

        self.assertEqual(two.text_lines('fil.txt'), 0)

    def test_wrong_birthdate(self):
        self.assertRaises(ValueError, three.Person,'Jozsi', 2017)

    def test_vaild_birtdate(self):
        i = three.Person('Jozsi', 2016)
        self.assertEqual(i.name, 'Jozsi')
        self.assertEqual(i.birth_date, 2016)

if __name__ == '__main__':
    unittest.main()
