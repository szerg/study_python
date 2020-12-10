# o metoda normala , fara decorator afecteaza starea obiectului, chipurile
# o metoda cu decoratorul @classmethod , afecteaza clasa; e folosita in general ca o factory method
# o metoda cu @staticmethod nu afecteaza starea clasei sau a obiectului, exista in clasa respectiva doar pt ca face sens
# dar nu are vreo proprietate anume; e mai mult un element stilistic

class Pizza:
    def __init__(self, *args,**kwargs):
        self.ingredients = args
        self.chef = kwargs['chef']
    @classmethod
    def house_pizza(cls):
        return cls('salam','pepperoni','mozarella',chef='Puf')

    @staticmethod
    def furnizor_blat():
        return 'brutaria de la colt'

pizza_pt_sergiu = Pizza.house_pizza()
print(pizza_pt_sergiu.ingredients)
print(Pizza.furnizor_blat())