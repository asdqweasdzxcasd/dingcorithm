def summarize(string):
    array = [0] * 26
    sum = ""
    for char in string:
        if char.isalpha():
            array[ord(char) - 97] += 1


    for i in range(len(array)):
        if array[i] != 0:
            if sum == "":
                sum += chr(i + 97) + str(array[i])
            else:
                sum += "/" + chr(i+97) + str(array[i])
    return sum


print("결과 : ", summarize("abc"))
print("결과 : ", summarize("aaabbbc"))
print("결과 : ", summarize("abbbc"))
print("결과 : ", summarize("ahhhhz"))
print("결과 : ", summarize("acccdeee"))