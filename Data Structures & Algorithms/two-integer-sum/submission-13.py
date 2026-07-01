class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def indexOfExclusive(nums, target, i):
            for j, num in enumerate(nums):
                if num == target and i != j:
                    return j
            return -1
        s = set(nums)
        for i, num in enumerate(nums):
            if target - num in s:
                j = indexOfExclusive(nums, target - num, i)
                if j != -1:
                    return [i, j]