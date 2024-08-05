class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        temp = {}
        freq = [[]for i in range(len(nums)+1)]

        for i in nums:
            temp[i] = 1 + temp.get(i,0)

        for i,j in temp.items():
            freq[j].append(i)

        res = []
        
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res