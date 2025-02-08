import heapq
class NumberContainers:
    # Your NumberContainers object will be instantiated and called as such:
    # obj = NumberContainers()
    # obj.change(index,number)
    # param_2 = obj.find(number)
    def __init__(self):
        self.res = {}
        self.container = {}

    def change(self, index: int, number: int) -> None:
        self.container[index] = number
        if number not in self.res:
            self.res[number] = [index]
            heapq.heapify(self.res[number]) # Initialize a min-heap.
        else:
            heapq.heappush(self.res[number], index) # Push index into min-heap.

    def find(self, number: int) -> int:
        if number not in self.res: return -1
        while self.res[number]:
            # Return the minimum index maybe contain the number
            index = self.res[number][0]
            if self.container[index] == number:
                return index
            else:
                # If container[index] was changed previously
                # Pop out the index of self.res[number].
                heapq.heappop(self.res[number])
        return -1


