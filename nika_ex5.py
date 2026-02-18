from collections import Counter
from math import sqrt
"""
Plaintext: HELLO_WORLD
Key: rob

Stream 1: H L O D each 1
Stream 2: E O R each 1
Stream 3: L W L 2:1 --> (Sum of proportions) / divide by 26, 
where sum of propotions is the individual frequencies / length of the stream.
In the end -> sd --> sum all streams

0.25 + 0.25 + 0.25 + 0.25 + 0.25 +
"""

def split_vectors(text, k) -> list:
    #just split to k parts, lowercase everything
    
    text_l = len(text)
    vectors = [[] for x in range(k)]
    
    for idx in range(text_l):
        key = idx % k
        vectors[key].append(text[idx]) 
    
    return vectors


def step1(vectors:list) -> list:
    frequencies = []
    for v in vectors:
        frequency = Counter(v)
        frequencies.append(frequency)
    return list(frequencies)

def step2(frequencies:list) -> float:
    # sd calculationn
    sd = 0
    for f in frequencies:
        freqs = list(f.values())
        first = sum(x**2 for x in freqs) / 26
        second = (sum(freqs)/26)**2
        sd += sqrt(first - second)
    return sd


if __name__ == "__main__":
    
    k_min = int(input())
    k_max = int(input())
    text = input()
    
    for k in range(k_min, k_max+1):
        print("k:",k)
        result = step2(step1(split_vectors(text, k)))
        print("Result for k =", k, ":", result)
    
    
    #skip all special chars