#i wrote this bc i was following a lecture slide but didnt need it. 
    def totient(self, n):
        prime_factos = self.prime_factors(n)
        result = n
        for i, x in enumerate(prime_factos):
            result *= (1 - 1/x)
        return int(result)

    def prime_factors(self, n):
        factors = []
    
        # Step 1: remove factor 2
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        
        # Step 2: test odd divisors up to sqrt(n)
        d = 3
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 2
        
        # Step 3: if remainder is prime
        if n > 1:
            factors.append(n)
        
        return factors