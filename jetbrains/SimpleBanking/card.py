# IIN = 400000
# random account id number de  lungime 9
# random Luhn number pt moment
# treb sa ii generezi si un pin asociat cardului
# un cont poate avea mai multe carduri
# cardurile pot sta intr-o lista 
# user-ul se poate loga cu oricare cont

import random

class Card:
    IIN = 400000
    acc_number_len = 9
    pin_len = 4
    def __init__(self):
        self.account_number = self._generate_random_number(Card.acc_number_len)
        self.luhn = random.randint(0,9)
        self.card_number = str(Card.IIN)+str(self.account_number)+str(self.luhn)
        self.pin = self._generate_random_number(Card.pin_len)
    
    def _generate_random_number(self, nr_len = 9):
        nr=''
        for _ in range(nr_len):
            nr+=str(random.randint(0,9))
        return nr
    
    


if __name__ == "__main__":
    my_card = Card()
    print(my_card.card_number)
    print(my_card.pin)