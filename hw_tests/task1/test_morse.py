import doctest
from task1.morse import encode


def test_morse(string):
    """
    >>> test_morse('SOS')
    '... --- ...'

    >>> test_morse('????????????') # doctest: +ELLIPSIS
    '..--.. ... ..--..'

    >>> test_morse('sos')
    Traceback (most recent call last):
    KeyError: 's'

    >>> test_morse(3)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    """

    return encode(string)


if __name__ == '__main__':
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)
