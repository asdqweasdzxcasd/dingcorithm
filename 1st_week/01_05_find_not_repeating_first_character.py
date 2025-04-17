input = "abadabac"


def find_not_repeating_first_character(string):
    array = find_alphabet_occurrence_array(string)

    alpha_array = []
    for i in range(len(array)):
        if array[i] == 1:
            alpha_array.append(chr(i + 97))

    for char in string:
        if char in alpha_array:
            return char

    return "_"



def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if char.isalpha():
            index = ord(char) - ord('a')
            alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))