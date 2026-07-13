class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # O(1)
        # O(1)
        s = "123456789"
        answer = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - length):
                num = int(s[i:i + length])
                if low <= num <= high:
                    answer.append(num)
        
        return sorted(answer)


        # O(1)
        # O(1)
        answer = []

        for start in range(1, 9):
            num = start
            for next in range(start + 1, 10):
                num = num * 10 + next
                if low <= num <= high:
                    answer.append(num)
        
        return sorted(answer)