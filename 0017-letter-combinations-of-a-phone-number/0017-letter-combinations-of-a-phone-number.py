class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        path = []
        result = []

        def dfs(index: int) -> None:
            if index == len(digits):
                result.append("".join(path))
                return
            
            digit = digits[index]
            for ch in phone[digit]:
                path.append(ch)
                dfs(index + 1)
                path.pop()
        
        dfs(0)
        return result

                