import collections

# asta iti zice ca poti face o subclasa la tuplu in care poti accesa elemntele
# cu argumente pozitionale si pe baza de atribut
# ar putea fi useful la unpacking de chestii dintr-un json citire din baza etc ca sa nu mai folosesti arg pozitionale
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # de ce cu _ in fata variabilei?
        # pt ca o tratam ca o variabila privata, pt internal use
        # cand dai import FrenchDeck variabila asta nu va fi vizibila
        # totodata _ de unul singur e folosit ca sa vezi rezultatul de la ult calcul sau pt eliminarea itemurilor nedorite la unpacking:
        # 'a',_,'b' = [1,2,3]
        self._cards = [Card(rank, suit)
                       for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    # care e treaba cu asta cu namedtuple?
    lucky_card = Card(7, 'spades')
    print(lucky_card)
    print(lucky_card[0])
    print(lucky_card.suit)
    print('#################################')
    mydeck = FrenchDeck()
    # printul de mai jos se foloseste de metodele suprascrise
    print(len(mydeck), mydeck[0], mydeck[-1])
    from random import choice
    print(choice(mydeck))
    # foloseste reversed mai mereu, e mai rapid si nu face sortare in place
    for card in reversed(mydeck):
        print(card.suit)
