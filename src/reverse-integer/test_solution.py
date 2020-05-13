from main import Solution


def test_two_sum_solution():
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21

