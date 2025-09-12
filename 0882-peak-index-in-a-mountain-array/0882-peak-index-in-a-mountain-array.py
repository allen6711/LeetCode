class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if not arr:
            return -1
        
        start, end = 0, len(arr) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            # Find the first index on the right slope (descending side)
            if arr[mid] >= arr[mid + 1]:
                end = mid
            
            else:
                start = mid
                
        if arr[start] > arr[end]:
            return start
        else:
            return end
























        # if not arr:
        #     return -1
        
        # start, end = 0, len(arr) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     # 12345 4321  or  1234 54321
        #     # use 1234 54321
        #     if arr[mid] <= arr[mid + 1]:
        #         start = mid
            
        #     else:
        #         end = mid

        # if arr[start] > arr[end]:
        #     return start
        
        # else:
        #     return end


        # if not arr:
        #     return -1
        
        # start, end = 0, len(arr) - 1

        # # find the first i so that arr[i] > arr[i + 1]
        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if arr[mid] > arr[mid + 1]:
        #         # Keep the answer at end
        #         end = mid
            
        #     else:
        #         start = mid
        
        # return end




        # left, right = 1, len(arr) - 2
        # while left < right:
        #     mid = (left + right) // 2
        #     if arr[mid] > arr[mid + 1]:
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # return left