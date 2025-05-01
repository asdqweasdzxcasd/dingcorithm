prices = [1, 2, 3, 2, 3]


# def get_price_not_fall_periods(prices):
#     length = len(prices)
#     result = [0] * length
#     for i in range(length):
#         price = prices[i]
#         for j in range(i+1, length, 1):
#             if price <= prices[j]:
#                 result[i] = result[i] + 1
#             else:
#                 result[i] = result[i] + 1
#                 break
#
#     return result


def get_price_not_fall_periods(prices):
    length = len(prices)
    result = [0] * length
    for i in range(0, length-1, 1):
        price_not_fall_period = 0
        for j in range(i+1, length, 1):
            if prices[i] <= prices[j]:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break
        result[i] = price_not_fall_period

    return result


print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 2, 3, 2, 3]))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))

