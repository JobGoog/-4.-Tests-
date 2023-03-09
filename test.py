import main
import unittest
import ya





class TestSomething(unittest.TestCase):

    def test_geo_logs(self):
        self.assertEqual(main.geo_filter(main.geo_logs), [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]) 

    def test_geo_id(self):
        self.assertEqual(main.geo_id(main.ids), {98, 35, 15, 213, 54, 119})

    def test_foo(self):
        self.assertEqual(main.foo(main.queries),{3: (4, 50.0), 2: (3, 37.5), 4: (1, 12.5)})

    def setUp(self):
        print('method setUp')

    def test_success_create_folder(self):
        self.assertEqual(ya.create_folder('test'), 201)

    def test_passed_create_folder(self):
        self.assertEqual(ya.create_folder('test_passed'), 401)

    


if __name__ == '__main__':
    unittest.main()