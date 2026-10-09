class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        #default to 0 when length is 0
        longest = 0
        
        for num in numset:
            # makes sure that counting wont start in the middle of a sequence
            if (num - 1) not in numset:
                length = 1
                # sees if there is a num+1 in the set first
                while (num + length) in numset:
                    length += 1
                longest = max(length, longest)
        return longest

        