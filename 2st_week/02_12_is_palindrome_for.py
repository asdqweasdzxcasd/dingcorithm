input = "abcba"


# def is_palindrome(string):
#     min = 0
#     max = len(string) - 1
#     while min <= max:
#         print(min, max)
#         if string[min] != string[max]:
#             return False
#         else:
#             min += 1
#             max -= 1
#
#     return True


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]:
            return False

    return True


print(is_palindrome(input))