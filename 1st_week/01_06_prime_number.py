# def prime_number(number):
#     array = []
#     for i in range(number):
#         num1 = i + 1  # 1 ~ 20
#         flag = True
#         if num1 == 1:
#             continue
#         for j in range(i):
#             num2 = j + 1
#             if num2 == 1:
#                 continue
#             if num1 % num2 == 0:
#                 flag = False
#         if flag:
#             array.append(num1)
#     return array
#
#
# print("정답 : ", prime_number(20))


# 소수는 자기 자신과 1 외에 는 아무 것도 나눌 수 없다.
def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):  # 2 ~ number

        # n보다 작은 모든 소수에 대해서
        for i in prime_list:
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)
    return prime_list



print("정답 : ", find_prime_list_under_number(20))









