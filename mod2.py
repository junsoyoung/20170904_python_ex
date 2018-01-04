# mod2.py

PI = 3.141592
class Math:
    def sol(self, r):
        return PI*(r**2)
    def sum(self, a, b):
        return a + b

if __name__ == "__main__":
    print( PI )
    m = Math()
    print(m.sol(3))
    print(m.sum(4, 5))


