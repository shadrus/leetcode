class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        for idx, char in enumerate(str_x):
            if char != str_x[-1*(idx+1)]:
                return False
        return True