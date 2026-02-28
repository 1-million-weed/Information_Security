
class EllipticCurveDH:
    def __init__(self):
        x_str, y_str = input().strip("(").strip(")").split(", ")
        self.G = (int(x_str), int(y_str))  # Base point
        self.a, self.b, self.p = map(int, input().split())
        self.m, self.n = map(int, input().split())

    def gcd(self,a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    def modular_inverse(self, a, m):
        gcd, x, _ = self.gcd(a, m)
        if gcd != 1:
            0/0
        return x % m

    def point_add(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        
        x1, y1 = P
        x2, y2 = Q
        
        if x1 == x2:
            if y1 == y2:
                s = (3 * x1 * x1 + self.a) * self.modular_inverse(2 * y1, self.p) % self.p
            else:
                return None
        else:
            s = (y2 - y1) * self.modular_inverse(x2 - x1, self.p) % self.p
        
        x3 = (s * s - x1 - x2) % self.p
        y3 = (s * (x1 - x3) - y1) % self.p
        
        return (x3, y3)

    def scalar_mult(self, k, P):
        if k == 0:
            return None
        if k == 1:
            return P
        
        result = None
        addend = P
        
        while k:
            if k & 1:
                result = self.point_add(result, addend)
            addend = self.point_add(addend, addend)
            k >>= 1
        
        return result

    def calculate(self):
        # Compute shared secret: m*n*G
        shared_secret = self.scalar_mult(self.m * self.n, self.G)
        
        if shared_secret is None:
            print("(infinity)")
        else:
            x, y = shared_secret
            print(f"({x}, {y})")

    
if __name__ == "__main__":
    ecdh = EllipticCurveDH()
    ecdh.calculate()