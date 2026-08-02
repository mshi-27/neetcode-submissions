class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l = 0
        r = 0
        res = 1
        chars = set()
        chars.add(s[l])
        while (r < len(s) - 1):
            r += 1
            if s[r] in chars:
                while(s[l] is not s[r]): 
                    chars.remove(s[l])
                    l += 1
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res


