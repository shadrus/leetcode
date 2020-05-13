from main import Solution


def test_two_sum_solution():
    solution = Solution()
    test_array = [2, 7, 11, 15, 12, 14]
    assert solution.twoSum(test_array, 9) == [0, 1]
    assert solution.twoSum(test_array, 23) == [2, 4]
    assert solution.twoSum(test_array, 16) == [0, 5]
