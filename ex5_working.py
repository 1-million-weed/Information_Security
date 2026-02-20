from collections import Counter
from math import sqrt
import sys

def split_vectors(text, k) -> list:
    text_l = len(text)
    vectors = [[] for x in range(k)]
    
    for idx in range(text_l):
        key = idx % k
        vectors[key].append(text[idx]) 
    
    return vectors

# gets the frequencies
def step1(vectors:list):
    frequencies = []
    for v in vectors:
        frequency = Counter(v)
        frequencies.append(frequency)
    return list(frequencies)

# this function will calculate the SD using the formula in the assignemnt
def step2(frequencies:list) -> float:
    # sd calculationn
    sd = 0
    for f in frequencies:
        freqs = list(f.values())
        first = sum(x**2 for x in freqs)/26
        second = (sum(freqs)/26)**2
        sd += sqrt(first - second)
    return sd

def key_guessser(k, frequencies:list):
    #ascii table-based
    e = ord('e')
    a = ord('a')   
    
    win_key = ""
    #im omitting uppercase cuz the input is only lowercase
    for f in frequencies:
        highest_fr = max(f, key=f.get)
        shift = (ord(highest_fr) - e)%26
        win_key += chr(shift + a)
    
    return win_key

def input_handler():
    min_k = int(input())
    max_k = int(input())
    encrypted_text = ""
    try:
        while True:
            text = input()
            if text != "":
                encrypted_text += text
    except EOFError:
        pass
        
    # i hate this, but it MUST be lowercase
    lowertext = "".join(ch.lower() for ch in encrypted_text if ch.isalpha())
    return min_k, max_k, lowertext


if __name__ == "__main__":
    min_k, max_k, text = input_handler()
    win_k = 0
    max_sd = 0
    
    for k in range(min_k, max_k+1):
        sds = []
        sd_calc = step2(step1(split_vectors(text, k)))
        if sd_calc > max_sd:
            max_sd = sd_calc
            win_k = k
        sds.append(sd_calc)
        print(f"The sum of {k} std. devs: {sum(sds):.2f}")
        
    win_frequencies = step1(split_vectors(text, win_k))
    win_key = key_guessser(win_k, win_frequencies)
    print("\nKey guess:")
    print(win_key)
        
    
        
    
