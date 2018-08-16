
class SergiuComponent():
    def __init__(self,x,y):
        # la asignarea asta se foloseste setterul definit mai jos
        self.x = x
        self.y = y

    # cand vreau sa accesez x asta e metoda care se va apela;
    # _x inteleg ca e folosit ca sa ascunda the internals of the implementation
    @property
    def x(self):
        return self._x

    # fara setter nu pot sa fac asignarea in __init__ pt x
    @x.setter
    def x(self,x):
        if x<0:
            self._x = 0
        elif x> 100:
            self._x = 100
        else:
            self._x = x
        return self._x
     
    @x.deleter
    def x(self,x):
        del self._x


if __name__ == "__main__":
    worker = SergiuComponent(-4,-1)
    print(worker.y)
    worker.x = 124
    print(worker.x)