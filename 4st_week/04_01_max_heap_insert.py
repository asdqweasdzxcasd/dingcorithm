 #    3
 #  4   2
 # 9

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        index = len(self.items)
        self.items.append(value)
        while index > 1:
            if self.items[index] > self.items[index // 2]:
                self.items[index // 2], self.items[index] = self.items[index], self.items[index // 2]
                index = index // 2
            else:
                return

        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!