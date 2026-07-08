class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        product_without_zeros = 1
        zero_indices = []
        for i, num in enumerate(nums):
            total_product *= num
            if num == 0:
                zero_indices.append(i)
            else:
                product_without_zeros *= num
        res = []
        for i, num in enumerate(nums):
            new_num = 1
            if (i in zero_indices):
                if len(zero_indices) > 1:
                    new_num = 0
                else:
                    new_num = product_without_zeros
            else:
                new_num = total_product / num
            res.append(int(new_num))
        return res