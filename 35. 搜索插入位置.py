from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


nums = [1, 3, 5, 6]
target = 5
print(Solution().searchInsert(nums, target))
print("-"*40)
nums = [1, 3, 5, 6]
target = 2
print(Solution().searchInsert(nums, target))
print("-"*40)
nums = [1, 3, 5, 6]
target=7
print(Solution().searchInsert(nums, target))