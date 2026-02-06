class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if matrix[mid // n][mid % n] <= target:
                start = mid
            
            else:
                end = mid
            
        if matrix[start // n][start % n] == target:
            return True
            
        if matrix[end // n][end % n] == target:
            return True
            
        return False
    















        # if not matrix or not matrix[0]:
        #     return False
        
        # m, n = len(matrix), len(matrix[0])
        # length = m * n
        # start, end = 0, length - 1
        # # [0, 1, 2, 3]
        # # [4, 5, 6, 7]
        # # [8, 9, 10, 11]

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if matrix[mid // n][mid % n] <= target:
        #         start = mid
            
        #     else:
        #         end = mid
        
        # if matrix[end // n][end % n] == target:
        #     return True
        
        # if matrix[start // n][start % n] == target:
        #     return True
        
        # return False
        
        # if not matrix or not matrix[0]:
        #     return False
        
        # m, n = len(matrix), len(matrix[0])
        # length = m * n
        # start, end = 0, length - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if matrix[mid // n][mid % n] <= target:
        #         start = mid
            
        #     else:
        #         end = mid

        # if matrix[start // n][start % n] == target:
        #     return True

        # if matrix[end // n][end % n] == target:
        #     return True
        
        # return False