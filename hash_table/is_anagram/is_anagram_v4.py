from collections import Counter

def is_anagram(word1: str, word2: str):

    counter1 = Counter(word1)
    counter2 = Counter(word2)

    return counter1 == counter2