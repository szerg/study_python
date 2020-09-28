nr_legs=4

def get_legs():
    global nr_legs
    nr_legs+=1
    # nu poti accesa variabila aia pt ca e in alt scope; trebuie initializata mai intai
    # nr_legs=nr_legs+1
    print(nr_legs)

get_legs()
