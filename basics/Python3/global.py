a = 3
fibs=[1,2,3,5,8,13,21]
def change( var_a):
    var_a =5

def global_change( var_a):
    # asta spune ceva gen : pointeaza catre constanta a
    global a 
    global b
    # aici se face modificarea si altereaza variabila globala
    a = var_a
    # merge si daca b nu e declarat in module scope anterior
    b = var_a

def change_obj(var_obj):
    var_obj=[]
    var_obj.append(100)

print("a={}".format(a))
change(a)
# does not change variable a
print("a={}".format(a))
# 
global_change(5)
print("a={}".format(a))
print("b={}".format(b))
# does not change the list
change_obj(fibs)
print("fibs={}".format(fibs))


