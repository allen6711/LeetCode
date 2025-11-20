class TwoSum:

    def __init__(self):
        self.hash = {}

    def add(self, number: int) -> None:
        self.hash[number] = self.hash.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for num in self.hash:
            if num * 2 == value and self.hash.get(num, 0) >= 2:
                return True

            target = value - num
            if target != num and self.hash.get(target, 0) > 0:
                return True
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)