class Logger:
    # O(n)
    # O(u)
    # u: number of unique messafe
    def __init__(self):
        self.last_printed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_printed:
            self.last_printed[message] = timestamp
            return True
        
        elif timestamp - self.last_printed[message] >= 10:
            self.last_printed[message] = timestamp
            return True
        
        else:
            return False

        # Record Next Allowed Time
        # 
    # def __init__(self):
    #     self.next_allowed = {}
    
    # def shouldPringMessage(self, timestamp: int, message: str) -> bool:
    #     if timestamp < self.next_allowed.get(message, 0):
    #         return False
        
    #     self.next_allowed[message] = timestamp + 10

    #     return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)