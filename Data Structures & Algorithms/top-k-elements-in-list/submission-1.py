class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countnums = {}
        for i in range(len(nums)):
            countnums[nums[i]] = countnums.get(nums[i], 1) + 1
            #i += 1
        sort_countnums = dict(sorted(countnums.items(), key=lambda item:item[1], reverse=True))

        fin = list(sort_countnums.keys())[:k]

        return fin
        

        