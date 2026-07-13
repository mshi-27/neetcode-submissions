class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = 0

        curr_streak = 0
        longest_streak = 0
        i = 0
        while i < len(nums):
            curr = nums[i]
            while curr in d and d[curr] == 0:
                if curr - 1 in d:
                    curr = curr - 1
                else:
                    break
            while curr in d and d[curr] == 0:
                d[curr] = 1
                curr_streak += 1
                curr += 1
            if curr_streak > longest_streak:
                longest_streak = curr_streak
            curr_streak = 0
            i += 1
        return longest_streak
