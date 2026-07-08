class Solution:
    def encode_str(self, s: str):
        return str(len(s)) + "." + s
    def decode_str_length(self, s: str):
        res = 0
        power = len(s) - 1
        for c in s:
            res += 10 ** power * int(c)
            power -= 1;
        return res
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + self.encode_str(s)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            num_string = ""
            curr_str = ""
            count = 0
            while s[i] != ".":
                num_string = num_string + s[i]
                i += 1
            i += 1
            print(num_string)
            count = self.decode_str_length(num_string)
            while count > 0:
                curr_str = curr_str + s[i]
                count -= 1
                i += 1
            res.append(curr_str)
        return res
        



"1", "apple"
"1apple"
[1, 5]