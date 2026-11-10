class Solution:
    def simplifyPath(self, path: str) -> str:
        # n: length of input path
        # O(n)
        # O(n)
        stack = []

        for directory in path.split("/"):
            if directory == "..":
                if stack:
                    stack.pop()
            
            elif directory and directory != ".":
                stack.append(directory)
        
        return "/" + "/".join(stack)














        stack = []

        for directory in path.split("/"):
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory and directory != ".":
                stack.append(directory)
        
        return "/" + "/".join(stack)