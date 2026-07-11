class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        mapping = {}
        visited = set()

        def backtrack(pattern_index: int, s_index: int) -> bool:
            if pattern_index == len(pattern) and s_index == len(s):
                return True
            
            if pattern_index == len(pattern) or s_index == len(s):
                return False
            
            ch = pattern[pattern_index]

            if ch in mapping:
                word = mapping[ch]
                if not s.startswith(word, s_index):
                    return False
                
                return backtrack(pattern_index + 1, s_index + len(word))
            
            for end in range(s_index + 1, len(s) + 1):
                candidate = s[s_index:end]

                if candidate in visited:
                    continue

                mapping[ch] = candidate
                visited.add(candidate)

                if backtrack(pattern_index + 1, end):
                    return True
                
                del mapping[ch]
                visited.remove(candidate)
            
            return False
        
        return backtrack(0, 0)
            













        mapping = {}
        used = set()

        def backtrack(pattern_index: int, string_index: int) -> bool:
            # Both pattern and string have been completely matched
            if pattern_index == len(pattern) and string_index == len(s):
                return True
            
            # Only one of them has been completely matched
            if pattern_index == len(pattern) or string_index == len(s):
                return False
            
            ch = pattern[pattern_index]

            # The current pattern character already has a mapping
            if ch in mapping:
                word = mapping[ch]

                if not s.startswith(word, string_index):
                    return False
                
                return backtrack(pattern_index + 1, string_index + len(word))
            
            # Try every possible non-empty substring
            for end in range(string_index + 1, len(s) + 1):
                candidate = s[string_index:end]

                # Different pattern characters cannot map
                # to the same substring
                if candidate in used:
                    continue
                
                mapping[ch] = candidate
                used.add(candidate)

                # Process the next pattern character
                # and continue the next String character, 
                # so it would be end (now is end - 1 since slicing excludes the end index)
                if backtrack(pattern_index + 1, end):
                    return True
                
                # Backtrack
                del mapping[ch]
                used.remove(candidate)
            
            return False
        
        return backtrack(0, 0)