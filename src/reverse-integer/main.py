class Solution:
    def reverse(self, x: int) -> int:
        minus = 1
        if x < 0:
            minus = -1
            x = x * minus
        reversed_str = str(x)[::-1]
        result = int(reversed_str) * minus
        if -2 ** 31 < result < ((2 ** 31) - 1):
            return result
        else:
            return 0
