def two_sum(arr: list[int], target: int) -> bool:
    complements = {}

    for index, num in enumerate(arr):
        complements[target - num] = index

    for index, num in enumerate(arr):
        if num in complements and complements[num] != index:
            return True
    
    return False


arr = [2, 4, 5, 4, 6]
target = 9

print(two_sum(arr, target))