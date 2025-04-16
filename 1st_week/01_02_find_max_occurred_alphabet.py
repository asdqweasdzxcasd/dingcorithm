def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for i, occurrence in enumerate(alphabet_occurrence_array):
        if max_occurrence < occurrence:
            max_occurrence = occurrence
            max_alphabet_index = i
    return chr(max_alphabet_index + 97)
    # array = find_alphabet_occurrence_array(string)
    # max_number = 0
    # max_index = 0
    # for i, count in enumerate(array):
    #     if max_number < count:
    #         max_number = count
    #         max_index = i
    # return chr(max_index + 97)


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if char.isalpha():
            index = ord(char) - ord('a')
            alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array





result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


# print("정답 = [1, 0, 2, 2, 2, 0, 2, 1, 3, 0, 0, 2, 2, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
#       find_alphabet_occurrence_array("hello my name is dingcodingco"))
# print("정답 = [1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0] \n현재 풀이 값 =",
#       find_alphabet_occurrence_array("we love algorithm"))
# print("정답 = [0, 3, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
#       find_alphabet_occurrence_array("best of best youtube"))

