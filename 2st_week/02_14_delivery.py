shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    available = []
    for order in orders:
        min = 0
        max = len(menus) - 1
        while min <= max:
            avg = (min + max) // 2
            if order == menus[avg]:
                available.append(order)
                break
            elif order < menus[avg]:
                max = avg - 1
            elif order > menus[avg]:
                min = avg + 1


    # 이 부분을 채워보세요!
    return available


result = is_available_to_order(shop_menus, shop_orders)
print(result)