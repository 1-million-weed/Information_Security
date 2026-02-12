def d_shift(line, d_shift):
    decoded = ""
    
    for c in line:
        if c.islower():
            base = 97
        elif c.isupper():
            base = 65
        else:
            decoded += c
            continue
            
        new_char = chr((ord(c) - base - d_shift) % 26 + base)
        decoded += new_char 

    return decoded

# encryption: E(p) = (x + n) mod 26 (from slides week1)
def e_shift(line, e_shift):
    encoded = ""
    
    for c in line:
        if c.islower():
            base = 97
        elif c.isupper():
            base = 65
        else:
            encoded += c
            continue
            
        new_char = chr((ord(c) - base + e_shift) % 26 + base)
        encoded += new_char 
        
    return encoded


def vigenere(plain, key, encrypt=True):
    result = ""
    idx = 0
    for c in plain:
        if not c.islower() and not c.isupper():
            result += c
            continue
        
        key_letter = key[idx % len(key)]
        if key_letter.islower():
            base_key = 97
        elif key_letter.isupper():
            base_key = 65
        else:
            continue
        
        idx += 1
        position = ord(key_letter) - base_key
        
        if encrypt:
            result += e_shift(c, position)
        else:
            result += d_shift(c, position)
        
    # print("Result:", result)
    return result
        
vigenere("This, you see, is a plaintext that is used for teaching purposes.", "lemon", True)

    