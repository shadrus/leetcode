from main import Solution


def test_two_sum_solution():
    solution = Solution()
    assert solution.longestCommonPrefix(["a", "b"]) == ""
    assert solution.longestCommonPrefix(["a"]) == "a"
    assert solution.longestCommonPrefix([]) == ""
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""

