from collections import Counter, defaultdict


def build_counter(word: str)  -> dict:
    counter = defaultdict(int)

    for char in word:
        counter[char] += 1
    return counter


def is_anagram(word1: str, word2: str):

    counter1 = build_counter(word1)
    counter2 = build_counter(word2)

    return counter1 == counter2