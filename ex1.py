import sys

mybytes = sys.stdin.buffer.read()

size = len(mybytes)
key = mybytes[size//2]
plain = mybytes[size//2+1:]

xor = bytes(k ^ p for k, p in zip(key, plain))
sys.stdout.buffer.write(xor)