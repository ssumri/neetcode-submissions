class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        setNums = set(numbers)
        ind1 = 0;
        ind2 = 0;


        while ind1 < len(numbers):
            if( target - numbers[ind1] in setNums ):
                ind2 = ind1 + 1
                break
            ind1 += 1
        
        while ind2 < len(numbers):
            if( target - numbers[ind1] == numbers[ind2]):
                break
            ind2 += 1
        
        return [ind1 + 1, ind2 + 1]
