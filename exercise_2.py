class ShiftCipher:
    def __init__(self):
        instructions = input().split()

        text_lines = []
        try:
            while True:
                text_lines.append(input())
        except EOFError:
            pass
        
        text = "\n".join(text_lines)
        self.run(instructions, text)
        

    def _decrypt(self, text, n):
        decoded = []
        
        for c in text:
            if c.islower():
                base = 97
            elif c.isupper():
                base = 65
            else:
                decoded.append(c)
                continue
                
            new_char = chr((ord(c) - base - n) % 26 + base)
            decoded.append(new_char)

        return "".join(decoded)


    def _encrypt(self, text, n):
        encoded = []
    
        for c in text:
            if c.islower():
                base = 97
            elif c.isupper():
                base = 65
            else:
                encoded.append(c)
                continue
                
            new_char = chr((ord(c) - base + n) % 26 + base)
            encoded.append(new_char)
            
        return "".join(encoded)


    def _mapping(self, text, map, encrypt):
        # get the character from the word
        mapped = []
        if not encrypt:
            inv_map = dict(zip(map, range(26)))
        for c in text: 
            if c.islower():
                base = 97
            elif c.isupper():
                base = 65
            else:
                mapped.append(c)
                continue
                
            #get the relative location e.g. 98 - 97 = 1 = B
            rel_loc = (ord(c) - base)
            if encrypt:
                new_char = map[rel_loc]
            else: #decrypt
                lowercase = c.lower()
                inv_loc = inv_map[lowercase]
                new_char = chr(base + inv_loc)
            # need to handle the big chars
            if base == 65:
                new_char = new_char.upper()
            mapped.append(new_char)
            
        return "".join(mapped)


    def run(self, instructions, text):
        shift = 0
        for i, instruction in enumerate(instructions):
            if instruction == "e" and (instructions[i+1]).isdigit():
                shift += int(instructions[i+1])
            elif instruction == "d" and (instructions[i+1]).isdigit():
                shift -= int(instructions[i+1])
            elif instruction in ["e", "d"] and not (instructions[i+1]).isdigit():
                # else the next instruction is a mapping so the preivous stack needs to be applied and then the mapping
                if shift != 0:
                    text = self._encrypt(text, shift) if shift > 0 else self._decrypt(text, -shift)
                    shift = 0
                    
                text = self._mapping(text, instructions[i+1], True if instruction == "e" else False)
                
            # what if there is no mapping after the last instruction? then just apply the shift
            elif shift != 0 and i == len(instructions) - 1:
                text = self._encrypt(text, shift) if shift > 0 else self._decrypt(text, -shift)
        
        print(text)
    
    
if __name__ == "__main__":
    ShiftCipher()

