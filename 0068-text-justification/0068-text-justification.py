class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # O(n+L)
        # O(L)
        res = []
        n = len(words)
        i = 0

        while i < n:
            # Step 1: greedily choose words for the current line
            line_len = len(words[i])
            j = i + 1
            
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            line_words = words[i:j]
            num_words = j - i
            total_letters = sum(len(word) for word in line_words)

            # Step 2: build the line
            # Case 1: last line or only one word -> left-justified
            if j == n or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth -  total_letters
                gaps = num_words - 1
                base_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                parts = []
                for k in range(gaps):
                    parts.append(line_words[k])
                    spaces = base_spaces
                    if k < extra_spaces:
                        spaces += 1
                    parts.append(" " * spaces)
                
                parts.append(line_words[-1])
                line = "".join(parts)
            
            res.append(line)
            i = j
        return res