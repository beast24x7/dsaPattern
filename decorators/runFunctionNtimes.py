def repeate(n):
    def decorateFunction(func):
        def wrapper(*args):
            for i in range(n):
                func(*args)
        return wrapper
    return decorateFunction




@repeate(6)
def sayHello(s):
    print("hello from {}".format(s))


sayHello("Ravi")

