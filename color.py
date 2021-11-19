from abc import ABC, abstractmethod


class ComputerColor(ABC):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    @abstractmethod
    def __mul__(self, a):
        pass

    @abstractmethod
    def __rmul__(self, a):
        pass

    def __repr__(self):
        return f'{self.START};{self.r};{self.g};{self.b}{self.MOD}●{self.END}{self.MOD}'


class Color(ComputerColor):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, rgb_2):
        if not isinstance(rgb_2, Color):
            raise TypeError('should be Color')

        return self.r == rgb_2.r and self.g == rgb_2.g and self.b == rgb_2.b

    def __add__(self, rgb_2):
        return Color(self.r + rgb_2.r, self.g + rgb_2.g, self.b + rgb_2.b)

    def __hash__(self):
        return hash(f'{self.g}{self.r}{self.b}')

    def __rmul__(self, a):
        return self * a

    def change_contrast(self, level, a):
        cl = -256 * (1 - a)
        f = 259 * (cl + 255) / (255 * (259 - cl))
        return int(f * (level - 128) + 128)

    def __mul__(self, a):
        return Color(self.change_contrast(self.r, a), self.change_contrast(self.g, a), self.change_contrast(self.b, a))


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [[bg_color] * 19,
                [bg_color] * 9 + [color] + [bg_color] * 9,
                [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
                [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
                [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
                [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
                [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
                [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
                [bg_color] * 19]

    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    print_a(Color(250, 0, 125))
