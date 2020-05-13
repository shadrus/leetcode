from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {v: k for k, v in enumerate(nums)}
        for idx, num in enumerate(nums):
            needed_value = target - num
            second_idx = hash_map.get(needed_value)
            if second_idx and second_idx != idx:
                return [idx, second_idx]
