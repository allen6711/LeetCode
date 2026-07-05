class ValidWordAbbr:
    # n = number of word in dictionary
    # L = average length of word
    # q = number of isUnique calls

    def __init__(self, dictionary: List[str]):
        self.abbr_map = defaultdict(set)

        for word in dictionary:   # O(n)
            abbr = self.get_abbr(word)
            self.abbr_map[abbr].add(word)


    # O(logn)
    def isUnique(self, word: str) -> bool:
        abbr = self.get_abbr(word)
        if abbr not in self.abbr_map:
            return True
        
        return self.abbr_map[abbr] == {word}
    
    # O(logn)
    def get_abbr(self, word: str) -> str:
        if len(word) <= 2:
            return word
        
        return word[0] + str(len(word) - 2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)