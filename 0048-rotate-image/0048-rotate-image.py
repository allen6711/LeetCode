class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(n^2)
        # O(1)
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse
        for i in range(n):
            self.reverse(matrix[i])
        
    def reverse(self, arr):
        i, j = 0, len(arr) - 1
        while j > i:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1