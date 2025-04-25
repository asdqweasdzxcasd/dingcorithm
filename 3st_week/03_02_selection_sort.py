input = [4, 6, 2, 9, 1]


# try
# def selection_sort(array):
#     size = len(array)
#     new_array = []
#
#     for i in range(size): # 0 ~ 4
#         min_value = array[i]
#         position = i
#         for j in range(size - i): # 0 ~ 4, 1 ~ 4, 2 ~ 4
#             if array[i+j] < min_value:
#                 min_value = array[i+j]
#                 position = i+j
#         array[i], array[position] = array[position], array[i]
#         new_array.append(min_value)
#
#     return new_array


# answer
def selection_sort(array):
    size = len(array)

    for i in range(size):
        min_index = i
        for j in range(size - i):
            if array[i+j] < array[min_index]:
                min_index = i+j
        array[i], array[min_index] = array[min_index], array[i]

    return array


selection_sort(input)
# print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))