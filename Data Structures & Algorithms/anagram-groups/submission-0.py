class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for str in strs:
            str_sorted = "".join(sorted(str))
            if str_sorted in d:
                d[str_sorted].append(str)
            else:
                d[str_sorted] = [str]
        return list(d.values())