class Queue(object):
    def __init__(self):
        self.vals=[]
    def insert(self, e): 
        self.vals.append(e)
    def remove(self): 
        try:
            # remove first element, expensive operation
            return self.vals.pop(0)
        except:
            raise ValueError()

q=Queue()
q.insert(1)
q.insert(2)
print q.vals

q.remove()
print q.vals

q1 = Queue()
q2 = Queue()
q1.insert(17)
print q1.vals
q2.insert(20)
print q2.vals
q1.remove()
q2.remove()

