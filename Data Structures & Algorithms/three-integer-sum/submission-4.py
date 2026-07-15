class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(int)
        triplets = []
        for num in nums:
            d[num] += 1
        for i, num1 in enumerate(nums):
            d[num1] -= 1
            j = i + 1
            while j < len(nums):
                num2 = nums[j]
                d[num2] -= 1
                target = 0 - num1 - num2
                if target in d and d[target] > 0:
                    isDuplicate = False
                    res = sorted([num1, num2, target])
                    for triplet in triplets:
                        if triplet == res:
                            isDuplicate = True
                    if not isDuplicate:
                        triplets.append(res)
                j += 1
                d[num2] += 1
            d[num1] += 1
        return triplets