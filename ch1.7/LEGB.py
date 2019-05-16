#LEGB
#L:loval
##


def f():
    b=1 #inclosing
    def g():
        b=100#Local
        print(b)
        print(__name__)

    b=200
    g()
f()