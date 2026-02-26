m, n = input().split()

m = int(m)
n = int(n)

def check_relative_primes(a, b):
    while b:
        a, b = b, a % b
    return a == 1

if not check_relative_primes(n, m):
    print('-1')
    exit()

private_key = input().split()
public_key = input().split()

private_key_sum = 0
for num in private_key:
    current = int(num)
    if current <= private_key_sum: 
        print('-1')
        exit()
    private_key_sum += current

if n <= private_key_sum:
    print('-1')
    exit()

constructed_public_key = []

if len(private_key) > len(public_key):
    print('0')
    exit()

for i, num in enumerate(private_key):
    key = (int(num) * m) % n
    constructed_public_key.append(key)
    if str(key) != public_key[i]:
        print('0')
        exit()

print("1")