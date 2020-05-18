from typing import List


class Solution:

    def find_prefix(self, test_prefix, strs: List[str]):
        for string in strs:
            if string[0:len(test_prefix)] == test_prefix:
                continue
            else:
                return
        return test_prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        strs.sort(key=len)
        for idx, char in enumerate(strs[0]):
            min_prefix = self.find_prefix(strs[0][0:len(strs[0])-idx], strs[1:])
            if min_prefix:
                return min_prefix
        return ""