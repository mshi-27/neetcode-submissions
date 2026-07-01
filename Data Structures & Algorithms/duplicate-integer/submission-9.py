class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = list(set(nums))
        print(a)
        print(sorted(nums))
        print(nums)
        return sorted(list(set(nums))) != sorted(nums)