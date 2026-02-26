class superincreasingknapsack:
    def __init__(self):
        self.crypttype = input()

    def run(self):
        if self.crypttype == "e":
            self.encrypt()
        else:
            self.decrypt()

    def _convert_binary(self, number: int):
        binary = []
        while number > 0:
            binary.append(number % 2)
            number //= 2
        return binary
    
    def _binary_to_decimal(self, binary):
        decimal = 0
        for i, b in enumerate(binary):
            decimal += b * (2 ** i)
        return decimal

    def encrypt(self):
        public_key = input().split()
        try:
            while True:
                number = int(input())
                binary = self._convert_binary(number)
                cipher = 0
                for i , b in enumerate(binary):
                    if b == 1:
                        cipher += int(public_key[i])
                print(cipher)
        except:
            pass

    def decrypt(self):
        m, n = input().split()
        m, n = int(m), int(n)
        private_key = input().split()
        private_key = [int(x) for x in private_key]
        
        m_inverse = self._mod_inverse(m, n)
        
        try:
            while True:
                cipher = int(input())
                cipher_prime = (cipher * m_inverse) % n
                
                binary = [0] * len(private_key)
                for i in range(len(private_key) - 1, -1, -1):
                    if cipher_prime >= private_key[i]:
                        binary[i] = 1
                        cipher_prime -= private_key[i]
                number = self._binary_to_decimal(binary)
                print(number)
        except:            
            pass

    def gcd(self,a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = self.gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
    
    def _mod_inverse(self, a, m):
        gcd, x, _ = self.gcd(a % m, m)
        return (x % m + m) % m

if __name__ == "__main__":
    sk = superincreasingknapsack()
    sk.run()