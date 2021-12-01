from task2.morse import encode
import pytest


@pytest.mark.parametrize('s', [
    6,
    -5,
    None
    ])
def test_exception(s):
    with pytest.raises(TypeError):
        encode(s)


@pytest.mark.parametrize('s,exp', [
    ('SOS', '... --- ...',),
    ('NASA', '-. .- ... .-'),
    ('HELLO-WORLD', '.... . .-.. .-.. --- -....- .-- --- .-. .-.. -..')
])
def test_equal(s, exp):
    assert encode(s) == exp
