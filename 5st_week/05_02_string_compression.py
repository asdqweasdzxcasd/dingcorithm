input = "abcabcabcabcdededededede"

# n= len(input)
#
# for split_size in range(1, n//2+1):
#     splitted = [
#         input[i:i+split_size] for i in range(0, n, split_size)
#     ]
#     print('splitted', splitted)



# 모든 경우에서 가장 압축을 많이 시킨 문자열의 길이를 반환해야 한다.
# 문자열의 길이가 n 이라면, 1부터 n개까지 길이로 쪼갤 수 있다.
# 1 ~ n//2 까지만 쪼개는 의미가 있다.
def string_compression(string):
    n = len(string)
    result = n
    for split_size in range(1, n // 2 + 1):
        splitted = [
            string[i:i+split_size] for i in range(0, n, split_size)
        ]
        compressed = ""



        count = 1
        for i in range(0, len(splitted)-1):
            cur, next = splitted[i], splitted[i+1]

            if cur == next:
                count += 1
            else:
                if count == 1:
                    compressed += cur
                else:
                    compressed += f"{count}{cur}"
                count = 1
        if count == 1:
            compressed += splitted[-1]
        else:
            compressed += f"{count}{splitted[-1]}"
        # print('splitted', splitted)
        # print('compressed', compressed)
        result = min(len(compressed), result)

    return result


print("정답 = 14 / 현재 풀이 값 = ", string_compression(input))
print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))