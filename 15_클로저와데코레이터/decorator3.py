# decorator3.py
import time

def elapsed(func): # 경과시간
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"함수 수행시간 : {end-start}초")
        return result
    return wrapper

@elapsed
def myfunc(msg, dict):
    print(f'{msg}, {dict}를 출력합니다.')

myfunc("You need python", {1:'python', 2:'js'})
myfunc("Error", {1:'python', 2:'js'})
