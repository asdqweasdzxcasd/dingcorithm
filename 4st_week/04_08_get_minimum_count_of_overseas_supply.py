import heapq

# 1. 현재 재고의 상태에 따라 최고값을 받아야 한다. (동적 상황)
# 2. 제일 많은 값만 가져간다.
# -> maxHeap

# heap 에다가 넣은 다음에 최고로 많은 값들을 꺼내서 stock에 추가할 것
# 현재 재고가 바닥나는 시점 이전까지
def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_date_index = 0
    max_heap = []
    while stock <= k: # stock 이 k 보다 크면 멈출 것이다.
        while last_date_index < len(dates) and dates[last_date_index] <= stock:
            heapq.heappush(max_heap, supplies[last_date_index] * -1)
            last_date_index += 1
        print(stock)
        supply = heapq.heappop(max_heap) * -1
        stock += supply
        answer += 1
    return answer


# 0(4) -> 4(24) -> 15(34)
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
# 0(4) -> 4(24) -> 20(44)
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
# 0(2) -> 1(11)
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))