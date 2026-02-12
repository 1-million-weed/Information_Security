class ShiftCipher:
    def __init__(self):
        instructions = self._read_input()
        instructions = instructions.split(" ")
        self.run(instructions)

    def _read_input(self):
        return input()
    
    def _decrypt(self, text, n):
        decoded = ""
        
        for c in text:
            if c.islower():
                base = 97
            elif c.isupper():
                base = 65
            else:
                decoded += c
                continue
                
            new_char = chr((ord(c) - base - n) % 26 + base)
            decoded += new_char 

        return decoded


    def _encrypt(self,text, n):
        encoded = ""
    
        for c in text:
            if c.islower():
                base = 97
            elif c.isupper():
                base = 65
            else:
                encoded += c
                continue
                
            new_char = chr((ord(c) - base + n) % 26 + base)
            encoded += new_char 
            
        return encoded


    def _mapping(self, text, map):
        # get the character from the word
        mapped = ""
        for c in text: 
            if c.islower():
                base = 97
            elif c.isupper():
                base = 65
            else:
                mapped += c
                continue
                
            #get the relative location 
            rel_loc = (ord(c) - base)
            new_char = map[rel_loc]
            # need to handle the big chars
            if base == 65:
                new_char = new_char.upper()
            mapped += new_char
            
        return mapped
    
    def _is_int(self, char):
        try:
            int(char)
            return True
        except:
            return False

    def run(self, instructions):
        text = self._read_input()
        while text != "":
            for i, instruction in enumerate(instructions):
                if instruction in ["d", "e"] and self._is_int(instructions[i+1]):
                    if instruction == "e":
                        text = self._encrypt(text, int(instructions[i+1]))
                    elif instruction == "d":
                        text = self._decrypt(text, int(instructions[i+1]))
                elif instruction in ["d", "e"] and not self._is_int(instructions[i+1]):
                    text = self._mapping(text, instructions[i+1])
            
            print(text)
            text = self._read_input()
        

                
    
if __name__ == "__main__":
    ShiftCipher()

