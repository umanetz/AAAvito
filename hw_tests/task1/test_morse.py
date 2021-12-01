import doctest
from task1.morse import encode


def test_morse(string):
    """
    >>> test_morse('MAI-PYTHON-2019')
    '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
    >>> test_morse('HELLO-WORLD')
    '.... . .-.. .-.. --- -....- .-- --- .-. .-.. -..'
    >>> test_morse('SOS')
    '... --- ...'
    >>> test_morse('????????????')
    '..--.. ... ..--..'
    >>> test_morse('NASA') # doctest: -ELLIPSIS
    '-. .- ... .-'
    >>> test_morse(3)
    Traceback (most recent call last):
        ...
    TypeError: Only string is available
    """

    if not isinstance(string, str):
        raise TypeError("Only string is available")

    return encode(string)


if __name__ == '__main__':
    doctest.testmod(optionflags=doctest.ELLIPSIS)
