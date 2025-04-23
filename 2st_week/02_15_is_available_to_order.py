shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# try
# def is_available_to_order(menus, orders):
#     menus.sort()
#     available = []
#     for order in orders:
#         min = 0
#         max = len(menus) - 1
#         while min <= max:
#             avg = (min + max) // 2
#             if order == menus[avg]:
#                 available.append(order)
#                 break
#             elif order < menus[avg]:
#                 max = avg - 1
#             elif order > menus[avg]:
#                 min = avg + 1
#
#     return available


# answer
def is_available_to_order(menus, orders):
    menus.sort() # O(NlogN)
    for order in orders:
        if not is_exist_target_number_binary(order, menus): # OlogN
            return False
    return True


def is_exist_target_number_binary(target, array):
    find_count = 0

    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)