class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        tuples = sorted(d.items(), key = lambda item: item[1])
        print(tuples)
        output = []
        index = len(tuples) - k
        while index < len(tuples):
            output.append(tuples[index][0])
            index += 1
        return output

