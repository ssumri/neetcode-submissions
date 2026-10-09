class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = 0
        prev_num = 0
        count = 1
        seq = sorted(set(nums))
        for i in range(len(seq)):
            if i == 0:
                prev_num = seq[0]
                count = 1
                max_sequence = count
                continue
            if seq[i] == prev_num + 1:
                count += 1
            else:
                count = 1
            
            if count > max_sequence:
                max_sequence = count
            
            prev_num = seq[i]
        return max_sequence

                

        