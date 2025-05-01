all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# try
# def get_absent_student(all_array, present_array):
#     all_set, present_set = set(all_array), set(present_array)
#     return all_set - present_set


# 1. 2중 반복문 O(N^2)
# for student in all_students: O(N)
#     is_present = False
#     for present_student in present_students: O(N-1)
#         if student == present_student:
#             is_present = True
#         if not is_present:
#             return student


# 2. 정렬 O(NlogN)
# 정렬 O(NlogN)
# 원소 순회 O(N)


# 3. Dictionary, Hash Table O(N)
# all_students 를 돌면서, hash_table 에 key 추가 O(N) * O(1)
# present_students 를 돌면서, hash_table 에 key 제거 O(N) * O(1)
# 남은 hash table = 결석한 학생


# answer
def get_absent_student(all_array, present_array):
    dict = {}
    for student in all_array:
        dict[student] = True
    for student in present_array:
        del dict[student]

    for key in dict.keys():
        return key


print("정답 = 지효 / 현재 풀이 값 = ", get_absent_student(all_students, present_students))
print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))