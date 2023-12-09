# Bad practice

def is_anagram(word1: str, word2: str) -> bool:
    counter1 = dict()
    counter2 = dict()

    for char in word1:
        if char not in counter1:
            counter1[char] = 1
            continue

        counter1[char] += 1

    for char in word2:
        if char not in counter2:
            counter2[char] = 1
            continue

        counter2[char] += 1

    return counter1 == counter2


