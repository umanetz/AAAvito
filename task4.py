import json
import keyword


class AttributeSetter:

    def __init__(self, mapping):

        for (name, value) in mapping.items():
            name = self.get_true_name(name)

            if isinstance(value, dict):
                setattr(self, name, AttributeSetter(value))

            else:
                setattr(self, name, value)

    def get_true_name(self, name):
        while keyword.iskeyword(name):
            name = name + '_'
        return name


class BaseAdvert:
    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class ColorizeMixin:
    def __repr__(self):
        string = super().__repr__()
        return f"\033[{self.repr_color_code}m" + string + "\033[0m"


class Advert(AttributeSetter, ColorizeMixin, BaseAdvert):
    repr_color_code = 32  # green

    def __init__(self, mapping) -> None:
        super().__init__(mapping)
        self.check_price()

    def check_price(self):
        price = self.__dict__.get('price')

        if price is None:
            self.price = 0

        elif not isinstance(price, (int, float)):
            raise TypeError('Price has to be int or float')

        elif price < 0:
            raise ValueError('price must be >= 0')


if __name__ == '__main__':
    a1 = """
            {
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"] }
        }
    """
    a2 = """
            {
        "title": "Вельш-корги", "price": 1000, "class": "dogs", "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25",
            "home": {"size" : 9, "floor" : 4}
        }
        }
    """

    advt1 = Advert(json.loads(a1))
    advt2 = Advert(json.loads(a2))

    print(advt1)
    Advert.repr_color_code = 36
    print(advt1)
    advt1.repr_color_code = 31
    print(advt1)
    Advert.repr_color_code = 36
    print(advt2.location.home.size)
