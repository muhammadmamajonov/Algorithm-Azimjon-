
def build_counter(word: str)  -> dict:
    counter = dict()
    for char in word:
        if char not in counter:
            counter[char] = 1
            continue
        counter[char] += 1
    return counter


def is_anagram(word1: str, word2: str):

    counter1 = build_counter(word1)
    counter2 = build_counter(word2)

    return counter1 == counter2
