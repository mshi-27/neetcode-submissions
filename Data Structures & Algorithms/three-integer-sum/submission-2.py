class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(int)
        triplets = set()
        for num in nums:
            d[num] += 1
        for i, num1 in enumerate(nums):
            if i >= len(nums) - 1:
                break
            d[num1] -= 1
            j = i + 1
            while j < len(nums):
                num2 = nums[j]
                d[num2] -= 1
                target = 0 - num1 - num2
                if target in d and d[target] > 0:
                    triplets.add(tuple(sorted((num1, num2, target))))
                j += 1
                d[num2] += 1
            d[num1] += 1
        return [list(triplet) for triplet in triplets]