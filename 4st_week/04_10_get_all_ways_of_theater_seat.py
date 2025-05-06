seat_count = 9
vip_seat_array = [4, 7]
memo = {
    1: 1,
    2: 2
} # 3: 3, 4: 5, 5: 8, ...

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


# [1, 2] -> [1, 2], [2, 1] = 2
# [1, 2, 3] -> [1, 2, 3], [2, 1, 3], [1, 3, 2] = 3
# [1, 2, 3, 4] -> [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [2, 1, 3, 4], [2, 1, 4, 3] = 5
# [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5], [1, 2, 3, 5, 4], ... = 8

# n번째 티켓을 가진 사람이 n번째 좌석에 앉았을 때 -> 좌석은 n-1개, 티켓도 n-1까지 남음
# n번째 티켓을 가진 사람이 n-1번째 좌석에 앉았을 때 -> 좌석은 n-2개, 티켓도 n-2까지 남음
# F(N) = F(N-1) + F(N-2) 피보나치 수열
def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways

    return all_ways


# 12가 출력되어야 합니다!
print("정답 = 12 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))