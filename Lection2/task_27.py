# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
# Пример
# "12 346 62 34 9 25623 42 34" -> 25623, 9
 
# test_data = [
#     ["12 346 62 34 9 25623 42 34", [25623, 9]],
#     ["7 346 1 34 9 6 42 -2 6", [346, -2]],
# ]
 
# for nums, expected in test_data:
#     assert find_max_min(map(int, nums.split(" "))) == expected

def find_max_min(lst):
    result = [float("-inf"), float("inf")]
    for el in lst:
        if result[0] < el:
            result[0] = el
        if result[1] > el:
            result[1] = el
    return result

source_str = "12 346 62 34 9 25623 42 34"
print(find_max_min(*[map(int, source_str.split())]))