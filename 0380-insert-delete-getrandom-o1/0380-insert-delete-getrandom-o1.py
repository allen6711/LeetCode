
class RandomizedSet:

    def __init__(self):
        # O(n)
        # O(n)
        # self.nums = []
        # O(1)
        # O(n)
        # nums stores the actual values
        self.nums = []
        # pos maps value -> index in nums
        self.pos = {}

    def insert(self, val: int) -> bool:
        # O(n)
        # O(n)
        # if val in self.nums:
        #     return False
        # self.nums.append(val)
        # return True
        # O(1)
        # O(n)
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        # O(n)
        # O(n)
        # if val not in self.nums:
        #     return False
        # self.nums.remove(val)
        # return True
        # O(1)
        # O(n)
        if val not in self.pos:
            return False
        
        remove_idx = self.pos[val]
        last_val = self.nums[-1]

        # Move the last element into the position of the element to remove
        self.nums[remove_idx] = last_val
        self.pos[last_val] = remove_idx

        # Remove the last element from the list
        self.nums.pop()

        # Remove the deleted value from the map
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        # O(1)
        # O(n)
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()