class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join(c for c in s if c.isalnum()).lower()

        i = 0
        j = len(s2) - 1
        print(s2)
        while i < j:
            if s2[i] != s2[j]:
                return False
            i += 1
            j -= 1
        return True