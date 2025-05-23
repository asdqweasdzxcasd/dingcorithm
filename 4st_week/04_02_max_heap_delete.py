class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        self.items[-1], self.items[1] = self.items[1], self.items[-1]
        pop_value = self.items.pop()
        index = 1
        while index < len(self.items):
            if len(self.items) - 1 >= 2 * index + 1:  # left, right 존재
                if self.items[2 * index] > self.items[2 * index + 1]:
                    max_index = 2 * index  # left
                else:
                    max_index = 2 * index + 1  # right
            elif len(self.items) - 1 >= 2 * index:  # left 존재
                max_index = 2 * index
            else:  #
                break
            if self.items[index] < self.items[max_index]: # current_index < max_index
                self.items[index], self.items[max_index] = self.items[max_index], self.items[index]
            index = max_index
        return pop_value  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]