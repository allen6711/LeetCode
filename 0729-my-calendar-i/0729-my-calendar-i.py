class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, startTime: int, endTime: int) -> bool:
        # max(startTime, start) < min(endTime, end)
        for start, end in self.calender:
            if startTime < end and endTime > start:
                return False
        self.calender.append((startTime, endTime))

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)