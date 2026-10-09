class Solution:
    # 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        # iterate through each element on the list
        for i in range(len(nums)):
            # for each element, multiply everything else
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j]
            products.append(product)
        return products


        