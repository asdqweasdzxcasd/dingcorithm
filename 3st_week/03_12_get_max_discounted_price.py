from operator import truediv

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


# 1. 가격이 높은 순으로 정렬
# 2. 할인율이 높은 순으로 정렬
# 3. 순서대로 곱한다.
# def get_max_discounted_price(prices, coupons):
#     result = 0
#     prices = sort_desc(prices)
#     coupons = sort_desc(coupons)
#
#     i = 0
#     while i < len(prices) and i < len(coupons):
#         result = result + prices[i] * (1 - coupons[i] / 100)
#         i = i + 1
#
#     while i < len(prices):
#         result = result + prices[i]
#         i = i + 1
#
#     return int(result)
#
#
# def sort_desc(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-1-i):
#             if array[j] < array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#
#     return array


# answer
def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    price_index = 0
    coupon_index = 0
    max_discount_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        discounted_price = prices[price_index] * (100 - coupons[coupon_index]) / 100
        max_discount_price += discounted_price
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discount_price += prices[price_index]
        price_index += 1

    return max_discount_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))