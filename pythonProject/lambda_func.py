l = ['rasengan','chidori']

def test(kurama,fun):
    for naruto in kurama:
        print(fun(naruto))


# def test2(naruto):
#     return naruto.capitalize()

test(l,lambda naruto:naruto.capitalize())
