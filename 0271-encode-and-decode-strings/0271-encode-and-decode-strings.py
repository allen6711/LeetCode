class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = []
        for char in strs:
            result.append(str(len(char)))
            result.append("#")
            result.append(char)
        
        return "".join(result)

        # result = []
        # for char in strs:
        #     result.append(str(len(char)))
        #     result.append("#")
        #     result.append(char)
        # return "".join(result)

        # result = []
        # for char in strs:
        #     result.append(str(len(char)))
        #     result.append("#")
        #     result.append(char)

        # return "".join(result)

        # result = []
        # for char in strs:
        #     result.append(str(len(char)))
        #     result.append('#')
        #     result.append(char)
        
        # return "".join(result)

        # result = []
        # for char in strs:
        #     result.append(str(len(char)))
        #     result.append("#")
        #     result.append(char)

        # return "".join(result)

        # result = []
        # for char in strs:
        #     result.append(str(len(char)))
        #     result.append("#")
        #     result.append(char)
        
        # return "".join(result)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        left = 0
        n = len(s)

        while left < n:
            right = left
            while right < n and s[right] != "#":
                right += 1
            length = int(s[left: right])
            left = right + 1
            word = s[left: left + length]
            result.append(word)
            left = left + length
        return result









        # left = 0
        # results = []
        # n = len(s)
        # while left < n:
        #     right = left
        #     while right < n and s[right] != "#":
        #         right += 1
        #     length = int(s[left: right])
        #     left = right + 1
        #     word = s[left: left + length]
        #     results.append(word)
        #     left = left + length
        
        # return results

        # left = 0
        # result =[]
        # n = len(s)

        # while left < n:
        #     right = left

        #     while right < n and s[right] != "#":
        #         right += 1
            
        #     length = int(s[left: right])
        #     left = right + 1
        #     word = s[left: left + length]
        #     result.append(word)
        #     left = left + length
        
        # return result

        # left = 0
        # n = len(s)
        # answer = []
        
        # while left < n:
        #     right = left

        #     while right < n and s[right] != '#':
        #         right += 1

        #     length = int(s[left: right])
        #     left = right + 1
        #     word = s[left: left + length]
        #     answer.append(word)
        #     left = left + length
        
        # return answer
        

        # result = []
        # left = 0
        # n = len(s)

        # while left < n:
        #     right = left

        #     while right < n and s[right] != "#":
        #         right += 1
            
        #     length = int(s[left: right])
        #     left = right + 1
        #     word = s[left: left + length]
        #     result.append(word)
        #     left = left + length
        
        # return result

        # result = []
        # left = 0
        # n = len(s)

        # while left < n:
        #     right = left

        #     while right < n and s[right] != "#":
        #         right += 1
        #     length = int(s[left: right])
        #     left = right + 1
        #     word = s[left: left + length]
        #     result.append(word)
        #     left = left + length

        # return result
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))