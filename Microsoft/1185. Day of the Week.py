class Solution:
    def __init__(self):
        self.dayNames = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        known_start = self.daysSinceStart(22, 2, 2020)
        target = self.daysSinceStart(day, month, year)
        return self.dayNames[(target - known_start) % 7]

    def daysSinceStart(self, day, month, year):
        num_days = 0
        # Year
        for y in range(year - 1, 1970, -1):
            num_days += 365 + self.has_leap_year(y)
        # Month
        num_days += sum(self.daysInMonth[:month - 1])
        if month > 2:
            num_days += self.has_leap_year(year)
        # Day
        num_days += day

        return num_days

    def has_leap_year(self, year):
        return 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0
