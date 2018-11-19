class VW():
    def __init__(self, max_power=300):
        self.max_power = max_power
        # un fel de a face variabila privata, i se adauga _NumeClasa in fata __
        self.__factory = 'Bremen'
        # conventie de a face o var privata; de asemenea nu va fi incarcata de import 
        self._bad_gbox = 'True'

    def __delattr__(self, name):
        print("{} is  getting deleted".format(name))
        super.__delattr__(self, name)
