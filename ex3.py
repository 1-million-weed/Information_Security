import sys

def xor(a, b):
    return bytes([a ^ b for a, b in zip(a, b)])

def fietsel(mode, left_half, right_half, key):
#encrypt
    if mode == b'\x65':
        for i in range(0, len(key), 4):
            old_left = left_half
            left_half = right_half
            right_half = xor(old_left, key[i:i+4])
        return left_half+right_half
    # decrypt
    else:
        for i in range(len(key)-4, -1, -4):
            old_right = right_half
            right_half = left_half
            left_half = xor(old_right, key[i:i+4])
        return left_half+right_half
    
    
if __name__ == "__main__":
    mybytes = sys.stdin.buffer.read()
    split = mybytes.split(b'\xFF')
    mode = split[0]
    key = split[1]
    plain = split[2]

    eight_bytes = [plain[i:i+8] for i in range(0, len(plain), 8)]
    
    result = []
    for byte in eight_bytes:
        left_half = byte[:4]
        right_half = byte[4:]
        result.append(fietsel(mode, left_half, right_half, key))
        
    sys.stdout.buffer.write(b''.join(result))
    
    