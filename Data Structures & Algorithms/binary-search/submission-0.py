class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftI = 0
        rightI = len(nums) - 1

        while leftI <= rightI:
            mid = (leftI + rightI) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                leftI = mid + 1
            else:
                rightI = mid - 1

        return -1

            
        