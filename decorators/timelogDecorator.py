import datetime 

def decorateLogger(func):
    def wrapper(*args):
        print("ETL Loading began at: {}".format(datetime.datetime.now()))
        result = func(*args)
        print("ETL Loading Ended at: {}".format(datetime.datetime.now()))
        return result
    return wrapper

@decorateLogger
def writeETL(table):
    print("loading data from table - {}".format(table))


writeETL("abc")






def decorateL(func):
    def Wrapper(*args):
        print("etl start {}".format(datetime.datetime.date))
        result = func