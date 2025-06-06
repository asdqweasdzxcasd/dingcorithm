finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    find_count = 0

    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
result = is_existing_target_number_binary(1, finding_numbers)
print(result)
result = is_existing_target_number_binary(16, finding_numbers)
print(result)


# def is_existing_target_number_binary(target, array):
#     num = len(array)
#     x = num
#     while num != 0:
#         if x == target:
#             return True
#         if num != 1 and num % 2 != 0:
#             num = num + 1
#         num = num // 2
#         if x > target:
#             x = x - num
#         elif x < target:
#             x = x + num
#     return False
