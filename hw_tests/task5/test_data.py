import pytest
from task5.what_is_year_now import what_is_year_now
from unittest.mock import patch
import urllib.request
from io import StringIO


def test_first_type():
    """Тестируем формат YYYY-MM-DD"""

    date = StringIO('{"currentDateTime": "2021-03-13"}')
    expected = 2021
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual = what_is_year_now()
        assert expected == actual


def test_second_type():
    """Тестируем формат DD.MM.YYYY"""

    date = StringIO('{"currentDateTime": "13.03.2021"}')
    expected = 2021
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual = what_is_year_now()
        assert expected == actual


def test_wrong_format1():
    """Тестируем первый формат даты с  разделителями из второго формата"""

    date = StringIO('{"currentDateTime": "2021.03.13"}')
    with pytest.raises(ValueError):
        with patch.object(urllib.request, 'urlopen', return_value=date):
            what_is_year_now()


def test_wrong_format2():
    """Тестируем второй формат даты с  разделителями из первого формата"""

    date = StringIO('{"currentDateTime": "13-03-2021"}')
    with pytest.raises(ValueError):
        with patch.object(urllib.request, 'urlopen', return_value=date):
            what_is_year_now()


def test_wrong_format3():
    """Тестируем второй формат даты с  разделителями ':'"""

    date = StringIO('{"currentDateTime": "13:03:2021"}')
    with pytest.raises(ValueError):
        with patch.object(urllib.request, 'urlopen', return_value=date):
            what_is_year_now()
