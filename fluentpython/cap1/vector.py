from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
     #   return 'Vector(%r,%r)'% (self.x,self.y)
     # folosit pt printare si pt reprezentare obiectului in general;
     # ar fi bine daca outputul ar fi un string care ar semana cu instantierea unui obiect
        return 'Vector({!r},{!r})'.format(self.x, self.y)

    def __add__(self, other):
        # overwrite la +
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, n):
        # asta face overwrite la *
        return Vector(self.x*n, self.y*n)

    # asta e folosita cand faci abs(v)
    def __abs__(self):
        return hypot(self.x, self.y)

    # asta e folosita cand faci bool(v) si e ca si cum ai apela v.__bool__
    def __bool__(self):
        return bool(abs(self))


if __name__ == '__main__':
    v = Vector(1, 2)
    w = Vector(3, 4)
    print(v)
    print(v+w)
    print(v*3)
