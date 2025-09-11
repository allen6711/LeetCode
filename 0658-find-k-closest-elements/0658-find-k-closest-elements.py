class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the largest number less than target
        # and the smallest number greater than target
        # -> find arr[left] < target and arr[right] >= target
        right = self.find_upper_closest(arr, x)
        left = right - 1

        # results = []

        for _ in range(k):
            if self.is_left_closer(arr, x, left, right):
                # results.append(arr[left])
                # print(left)
                left -= 1
            else:
                # results.append(arr[right])
                # print(right)
                right += 1
            
        return arr[left + 1: right]

    def find_upper_closest(self, arr, x):
        start, end = 0, len(arr) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if arr[mid] >= x:
                end = mid
            
            else:
                start = mid
        
        if arr[start] >= x:
            return start
        
        if arr[end] >= x:
            return end
        
        return len(arr)

    def is_left_closer(self, arr, x, left, right):
        if left < 0:
            return False
        
        if right >= len(arr):
            return True
        
        return x - arr[left] <= arr[right] - x



























        # left, right = 0, len(arr) - k
        # while left < right:
        #     mid = (left + right) // 2
        #     if x - arr[mid] <= arr[mid + k] - x:
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # return arr[left:left + k]