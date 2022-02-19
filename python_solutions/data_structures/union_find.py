class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        [self.push(i) for i in items]

    def push(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap)-1)


    def peek(self):
        if len(self.heap) > 1:  # ignore default `0`
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, _index):
        if _index <= 1:
            return

        parent = _index // 2
        if self.heap[_index] > self.heap[parent]:
            self.__swap(_index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, _index):
        largest_index, left_child_index, right_child_index = _index, _index*2, _index*2+1

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_index]:
            largest_index = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_index]:
            largest_index = right_child_index

        if largest_index != _index:
            self.__swap(_index, largest_index)
            self.__bubbleDown(largest_index)



if __name__ == '__main__':
    heap = MaxHeap([-1, 95, 3, 21])
    print("peek: %s" % heap.peek())
    heap.push(96)
    print("peek after push: %s" % heap.peek())
    heap.pop()



