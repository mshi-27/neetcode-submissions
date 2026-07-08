class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1]
        i = 1
        cum_product = 1
        while i < len(nums):
            cum_product *= nums[i - 1]
            prefix_arr.append(cum_product)
            i += 1
        i = len(nums) - 2
        cum_product_post = 1
        while i >= 0:
            cum_product_post *= nums[i + 1]
            prefix_arr[i] *= cum_product_post
            i -= 1
        return prefix_arr
            