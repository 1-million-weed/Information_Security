import sys

mybytes = sys.stdin.buffer.read()
result = []
s = [0] * 256
K = [0] * 256

#idk how else i really cant with the input handling :(
split = mybytes.split(b'\xff', 1)
key = split[0]
plain = split[1]

for i in range(256):
    s[i] = i
    K[i] = key[i % len(key)]
    
# page 56
j = 0
for i in range(256):
    j = (j + s[i] + K[i]) % 256
    s[i], s[j] = s[j], s[i]
    
i = j = 0
#removing the first 256
for ugh in range(256):
    i = (i+1) % 256
    j = (j + s[i]) % 256
    s[i], s[j] = s[j], s[i]
    t = (s[i] + s[j]) % 256
    
for line_of_bytes in plain:
    i = (i+1) % 256
    j = (j + s[i]) % 256
    s[i], s[j] = s[j], s[i]
    t = (s[i] + s[j]) % 256
    xor = s[t] ^ line_of_bytes
    result.append(xor)
    
sys.stdout.buffer.write(bytes(result))
    