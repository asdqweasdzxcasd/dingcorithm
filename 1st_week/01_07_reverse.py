# def reverse(string):
#     count0 = 0
#     count1 = 0
#     new_string = ""
#     for i in range(len(string)):
#         char = string[i]
#         if i == 0:
#             new_string = char
#         elif char != new_string[-1]:
#             new_string += char
#
#     for char in new_string:
#         if char == '1':
#             count1 += 1
#         elif char == '0':
#             count0 += 1
#     if count1 > count0:
#         return count0
#     else:
#         return count1
#
#
#
# print("결과 : ", reverse("0001111"))
# print("결과 : ", reverse("0001100"))
# print("결과 : ", reverse("1111111"))
# print("결과 : ", reverse("1010101"))


input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1): # i = 0 ~ len-2
        if string[i] != string[i+1]:
            if string[i+1] == '1':
                count_to_all_zero += 1
            if string[i+1] == '0':
                count_to_all_one += 1

    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)























