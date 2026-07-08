class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1]
        i = 1
        cum_product = 1
        while i < len(nums):
            cum_product *= nums[i - 1]
            prefix_arr.append(cum_product)
            i += 1
        suffix_arr = [1]
        i = len(nums) - 2
        cum_product = 1
        while i >= 0:
            cum_product *= nums[i + 1]
            suffix_arr.append(cum_product)
            i -= 1
        res = []
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            res.append(prefix_arr[i] * suffix_arr[j])
            i += 1
            j -= 1
        return res
            