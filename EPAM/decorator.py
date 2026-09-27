from datetime import datetime
import time

def logger(function):
    def wrapper(*args):
        print("data laod started at -> {}".format(datetime.now()))
        function(*args)
        time.sleep(10)
        print("data load completed at -> {}".format(datetime.now()))
        return function(*args)
    return wrapper


@logger
def load_table(tableName):
    print("Loading {}".format(tableName))


load_table("dim.product")