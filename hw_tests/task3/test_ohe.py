from task3.one_hot_encoder import fit_transform
import unittest


class TestTf(unittest.TestCase):

    def test_ohe_eq1(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_ohe_eq2(self):
        cities = ['Tula', 'Orel', 'Habarovsk']
        exp_transformed_cities = [
            ('Tula', [0, 0, 1]),
            ('Orel', [0, 1, 0]),
            ('Habarovsk', [1, 0, 0])
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_ohe_notNone(self):
        cities = []
        self.assertIsNotNone(fit_transform(cities))

    def test_excep(self):
        cities = None
        with self.assertRaises(TypeError):
            fit_transform(cities)


if __name__ == '__main__':
    unittest.main(verbosity=True)
