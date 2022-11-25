"""
def foo(pierwszy, drugi, trzeci, *reszta):
    print ("Pierwszy: %d" % pierwszy)
    print ("Drugi: %d" % drugi)
    print ("Trzeci: %d" % trzeci)
    print ("I cala reszta... %d" % list(reszta))
"""


def foo (x, y, z, *arg):
    suma = sum(list(arg))
    print(x + y + z + suma)
    
foo(1,2,3,4,5,333)   
