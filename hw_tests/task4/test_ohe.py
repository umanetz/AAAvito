from task4.one_hot_encoder import fit_transform
import pytest


def test_equal1():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_equal2():
    cities = []
    exp_transformed_cities = []
    assert fit_transform(cities) == exp_transformed_cities


def test_equal3():
    cities = ['Tula', 'Orel', 'Habarovsk']
    exp_transformed_cities = [
        ('Tula', [0, 0, 1]),
        ('Orel', [0, 1, 0]),
        ('Habarovsk', [1, 0, 0])
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_notNone():
    cities = []
    assert fit_transform(cities) is not None


def test_exception_type():
    with pytest.raises(TypeError):
        fit_transform(None)


def test_exception_memory():
    with pytest.raises(MemoryError):
        fit_transform(['Moscow'] * int(10e13))
