import time

def elapsed(func): # 경과시간
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"함수 수행시간 : {end-start}초")
        return result
    return wrapper

def myfunc():
    print('함수가 실행됩니다.')

elapsed(myfunc)()