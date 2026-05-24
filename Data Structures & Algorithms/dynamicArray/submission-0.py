class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nums = []

    def get(self, i: int) -> int:
        return self.nums[i]

    def set(self, i: int, n: int) -> None:
        self.nums[i] = n

    def pushback(self, n: int) -> None:
        if len(self.nums) == self.capacity:
            self.resize()

        self.nums.append(n)

    def popback(self) -> int:
        return self.nums.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.nums)
    
    def getCapacity(self) -> int:
        return self.capacity
