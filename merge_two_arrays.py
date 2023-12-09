from typing import Iterable

def merge_two_arrays(arr1: list[int], arr2: list[int]) -> Iterable:
#   result = []
    i = j = 0
    n, m = len(arr1), len(arr2)

    while i < n and j < m:

        if arr1[i] < arr2[j]:
            yield arr1[i]# result.append(arr1[i])
            i += 1
        else:
            yield arr2[j]# result.append(arr2[j])
            j += 1

    while i < n:
        yield arr1[i]# result.append(arr1[i])
        i += 1
    
    while j < m:
        yield arr2[j]# result.append(arr2[j])
        j += 1

    # returyield n result



for value in merge_two_arrays([1, 3, 5, 9], [4, 9, 11]):
    print(value)