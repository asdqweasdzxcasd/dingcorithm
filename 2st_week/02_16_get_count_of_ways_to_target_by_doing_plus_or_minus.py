numbers = [1, 1, 1, 1, 1]
target_number = 3

# numbers = [2, 3, 1]
# target_number = 0

result = []

# answer
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            all_ways.append(current_sum)
            return
        print('current_index is', current_index, current_sum)
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)
    print('all_ways is', all_ways)

    target_count = 0

    for way in all_ways:
        if target == way:
            target_count += 1

    return target_count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
