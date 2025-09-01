# wrapper.py

def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

if __name__ == '__main__':
    print(mul(3)(10))
    print(mul(5)(10))