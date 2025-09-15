class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        
        # find the index of x
        index = self.binarySearch(arr, x)
        # print(index)
        left, right = index - 1, index
        # print(left, right)
        for _ in range(k):
            # start: index - 1 and index + 1
            # check |a - x| < |b - x| & |a - x| == |b - x| and a < b
            if self.is_left(arr, x, left, right):
                left -= 1
                print(left)
            
            else:
                right += 1
                print(right)
        
        return arr[left + 1: right]

    
    def binarySearch(self, arr, x) -> int:
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
        
        # if all elements are less than x
        return len(arr)
        
    
    def is_left(self, arr, x, left, right) -> bool:
        if left < 0:
            return False
        
        if right >= len(arr):
            return True
        
        return x - arr[left] <= arr[right] - x





























    #     if not arr:
    #         return []
        
    #     index = self.binarySearch(arr, x)

    #     left, right = index - 1, index

    #     for _ in range(k):
    #         if self.is_most_left(arr, left, right, x):
    #             left -= 1
    #             print(left)
    #         else:
    #             right += 1
    #             print(right)
        
    #     return arr[left + 1: right]
        
    # # Find the position of target(x)
    # def binarySearch(self, arr, x) -> int:
    #     if not arr:
    #          return -1

    #     start, end = 0, len(arr) - 1

    #     while start + 1 < end:
    #         mid = (start + end) // 2

    #         # Find the first position 
    #         if arr[mid] >= x:
    #             end = mid
                
    #         else:
    #             start = mid
            
    #     if arr[end] >= x:
    #         return end
            
    #     if arr[start] >= x:
    #         return start
        
    #     # Since we plane to find the first position, if x < all elements, we could find the end at index: 0
    #     # else: if x > all elements, we could find the end at index: len(arr), out of arr
    #     return len(arr)

    # def is_most_left(self, arr, left, right, x) -> bool:
    #     if left < 0:
    #         return False
            
    #     if right >= len(arr):
    #         return True
            
    #     return x - arr[left] <= arr[right] - x




    #     # find the largest number less than target
    #     # and the smallest number greater than target
    #     # -> find arr[left] < target and arr[right] >= target
    #     right = self.find_upper_closest(arr, x)
    #     left = right - 1

    #     # results = []

    #     for _ in range(k):
    #         if self.is_left_closer(arr, x, left, right):
    #             # results.append(arr[left])
    #             # print(left)
    #             left -= 1
    #         else:
    #             # results.append(arr[right])
    #             # print(right)
    #             right += 1
            
    #     return arr[left + 1: right]

    # def find_upper_closest(self, arr, x):
    #     start, end = 0, len(arr) - 1

    #     while start + 1 < end:
    #         mid = (start + end) // 2

    #         if arr[mid] >= x:
    #             end = mid
            
    #         else:
    #             start = mid
        
    #     # If all num in arr are greater than x, then this condiiton
    #     # [2, 3, 4], x = 1
    #     if arr[start] >= x:
    #         return start
            
    #     # Generally is this
    #     if arr[end] >= x:
    #         return end
            
    #     # All elements are < x, so the insertion index is len(arr)
    #     return len(arr)

    # def is_left_closer(self, arr, x, left, right):
    #     if left < 0:
    #         return False
        
    #     if right >= len(arr):
    #         return True
        
    #     return x - arr[left] <= arr[right] - x



        # left, right = 0, len(arr) - k
        # while left < right:
        #     mid = (left + right) // 2
        #     if x - arr[mid] <= arr[mid + k] - x:
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # return arr[left:left + k]