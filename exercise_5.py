import math
import sys

class CalculateSD:
    def __init__(self, encrypted, k):
        self.encrypted = encrypted
        self.k = k

    @staticmethod
    def make_steams(encrypted, k) -> list:
        return [encrypted[i::k] for i in range(k)]

    @staticmethod
    def count_frequencies(steams) -> list:
        frequencies = []
        for steam in steams:
            frequency = {}
            for char in steam:
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1
            frequencies.append(frequency)
        return frequencies

    @staticmethod
    def sum_frequencies(frequencies) -> list:
        totals = []
        for frequency in frequencies:
            total = sum(frequency.values())
            totals.append(total)
        return totals

    @staticmethod
    def sum_squares(frequencies) -> list:
        squares = []
        for frequency in frequencies:
            square = sum(count ** 2 for count in frequency.values())
            squares.append(square)
        return squares

    def calculate_sd(self):
        streams = self.make_steams(self.encrypted, self.k)
        frequencies = self.count_frequencies(streams)
        x = self.sum_frequencies(frequencies)
        a = sum(self.sum_squares(frequencies)) /26
        b = sum(x)/26
        result = math.sqrt(a) -math.sqrt(b)
        return result


class BreakVigenere:
    def __init__(self):
        self.min_k = int(input())
        self.max_k = int(sys.stdin.readline().rstrip("\n"))
        self.encrypted_texts = []
        text = sys.stdin.readline().rstrip("\n")
        while text != "":
            self.encrypted_texts.append(text)
            text = sys.stdin.readline().rstrip("\n")


    def break_vigenere(self):
        for k in range(self.min_k, self.max_k+1):
            sds = []
            for text in self.encrypted_texts:
                sd_calc = CalculateSD(text, k)
                sds.append(sd_calc.calculate_sd())
            print(f"The sum of {k} std. devs: {sum(sds)}")

if __name__ == "__main__":
    breaker = BreakVigenere()
    breaker.break_vigenere()
    