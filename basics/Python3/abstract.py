import abc
import six

@six.add_metaclass(abc.ABCMeta)
class AnalysisComponent():

    def __init__(self):
        self.x = 1

    @abc.abstractproperty
    def from_queue(self):
        return None

class SpecificComponent(AnalysisComponent):
    
    def __init__(self,from_queue):
        # asas initializezi contructorul de la clasa de la care mostenesti
        super(SpecificComponent,self).__init__()
        
    # asta e obligatorie pentru ca ai definit ca propr abstracta from_queue mai sus
    # deci trebuie sa o implementezi
    @property
    def from_queue(self):
        return 5
    
    # fara @property devine o metoda obisnuita, nu o proprietate

if __name__ == "__main__":
    worker = SpecificComponent("scan_fetched")

    print(worker.from_queue)