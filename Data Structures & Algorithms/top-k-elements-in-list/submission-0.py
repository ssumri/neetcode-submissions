class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countnums = {}
        for i in range(len(nums)):
            if nums[i] in countnums:
                countnums[nums[i]] = countnums[nums[i]] + 1
            else:
                countnums[nums[i]] = 1
            i += 1
        sort_countnums = dict(sorted(countnums.items(), key=lambda item:item[1], reverse=True))

        fin = list(sort_countnums.keys())[:k]

        return fin
        

        