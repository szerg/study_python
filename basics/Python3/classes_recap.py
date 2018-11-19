import cars.sportscar.ferrari
from cars.streetcar import * # aici streetcar e un director dar am suprascris variabila __all__ cu numele  pachetului pe  care il vreau importat si merge


class Showroom():
    def __init__(self, capacity, location):
        self.capacity = capacity
        self.location = location

    def get_cars(self):
        f = cars.sportscar.ferrari.Ferrari('yellow', 780)
        v = cars.streetcar.vw.VW(max_power=150)
        print('One {} ferrari with {} bhp'.format(f.color, str(f.power)))
        print('One vw with a max power of {}'.format(str(v.max_power)))
