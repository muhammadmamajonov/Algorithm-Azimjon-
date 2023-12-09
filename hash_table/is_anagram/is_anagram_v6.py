from collections import Counter

def is_anagram(word1: str, word2: str):

    counter = Counter(word1)
    
    for char in word2:
        counter[char] -= 1

    return all(val == 0 for val in counter.values())