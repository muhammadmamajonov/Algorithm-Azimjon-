from collections import Counter, defaultdict

def is_anagram(word1: str, word2: str):

    counter = Counter(word1)
    
    for char in word2:
        counter[char] -= 1

    for val in counter.values():
        if val != 0:
            return False
    
    return True