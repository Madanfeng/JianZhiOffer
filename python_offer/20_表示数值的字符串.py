"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""


class Solution:
    def __init__(self):
        self.p = 0

    def isNumber(self, s):
        s = s.strip()
        if s == '': return False
        number = self.scanInterger(s)

        if self.p > len(s) - 1:
            return number

        if self.p < len(s) and s[self.p] == '.':
            self.p += 1
            if self.p > len(s) - 1:
                return number
            number = self.scanUnsignedInterger(s) or number

        if self.p < len(s) and s[self.p] in ['e', 'E']:
            self.p += 1
            if self.p > len(s) - 1:
                return False
            number = number and self.scanInterger(s)

        if self.p < len(s):
            return False

        return number

    def scanInterger(self, s):
        if s[self.p] in ['+', '-']:
            self.p += 1
        return self.scanUnsignedInterger(s)

    def scanUnsignedInterger(self, s):
        pre = self.p
        while (self.p < len(s) and s[self.p] >= '0' and s[self.p] <= '9'):
            self.p += 1
        return self.p > pre


s = Solution()
print(s.isNumber("123"))
