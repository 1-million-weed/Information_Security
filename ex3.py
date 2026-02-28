

class RSA:
    def __init__(self):
        self.crypt = input()
        self.p, self.q, self.e = map(int, input().split())
        self.n = self.p * self.q
        
        if self.crypt == "e":
            self.encrypt()
        elif self.crypt == "d":
            self.decrypt()

    def encrypt(self):
        try:
            while True:
                m = int(input())
                c = pow(m, self.e, self.n)
                print(c)
        except EOFError:
            pass
    
    def decrypt(self):
        phi_n = (self.p - 1) * (self.q - 1)
        self.d = self.modular_inverse(self.e, phi_n)
        
        try:
            while True:
                c = int(input())
                m = pow(c, self.d, self.n)
                print(m)
        except:
            pass

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
    
if __name__ == "__main__":
    rsa = RSA()