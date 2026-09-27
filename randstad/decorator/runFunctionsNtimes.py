def repeat(n:int):
    def decorateFunction(func):
        def wrapper(*args):
            for i in range(n):
                func(*args)
        return wrapper
    return decorateFunction


@repeat(10)

def say(s:str):
    print("say hello from {}".format(s))


#say("Ravi")

import datetime

def decorateLogs(function):
    def wrapper(*args):
        print("ETL Load Began At: {}".format(datetime.datetime.now()))
        res = function(*args)
        print("ETL Load ENDED At: {}".format(datetime.datetime.now()))
        return res
    return wrapper


@decorateLogs
def writeETL(tableName:str):
    print("Loading data for {}".format(tableName))


writeETL("plan_State")