from main import Solution


def test_two_sum_solution():
    solution = Solution()
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(10) == False
    assert solution.isPalindrome(12154045121) == True
    assert solution.isPalindrome(1154045121) == False

