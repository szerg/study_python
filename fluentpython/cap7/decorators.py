# decorator - callable care ia ca parametru o functie
# metaprogramming - change program behaviour at runtime?
# puterea unui decorator consta ca pot schimba ce executa de fapt o functie; se executa imediat ce incarci un modul

# ex1

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    #return func

@register
def f1():
    print('running f1')

@register
def f2():
    print('running f2')


def f3():
    print('running f3')


if __name__ == '__main__':
    print('running main')
    print('registry: {}'.format(registry))
    f1()
    f2()
    f3()

# cand se ruleaza outputul e asa:

# running register(<function f1 at 0x0376AA70>)
# running register(<function f2 at 0x0376AAB0>)
# running main
# registry: [<function f1 at 0x0376AA70>, <function f2 at 0x0376AAB0>]
# running f1
# running f2
# running f3

# deci decoratorul se ruleaza la import;
# cand apelezi functia de fapt tu faci un call catre valoarea de retur a decoratorului, care in acest caz e tot functia aia

# global ?
# nonlocal ?
# closure ?
# unde ai folosi decoratorii
# de ce e mai bine sa ii folosesti ca si clase, nu ca functii?
# decoratori utili din standard library
# decoratori stacked
# decoratori cu parametri
