class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        array = self.store[key]
        if not array:
            return ""
        
        left, right = 0, len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid][1] <= timestamp:
                left = mid
            else:
                right = mid
        
        if array[right][1] <= timestamp:
            return array[right][0]
        if array[left][1] <= timestamp:
            return array[left][0]
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)