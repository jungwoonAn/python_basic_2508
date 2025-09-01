# closure2.py

class Mul:
    def __init__(self, m):
        self.m = m

    # def mul(self, n):
    def __call__(self, n):
        return n*self.m

if __name__ == '__main__':
    mul3 = Mul(3)
    mul5 = Mul(5)
    mul7 = Mul(7)

    # print(mul3.mul(10))
    # print(mul5.mul(10))
    # print(mul7.mul(10))

    print(mul3(10))
    print(mul5(10))
    print(mul7(10))