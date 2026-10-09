class Solution:
    # 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProds = []
        rightProds = []

        products_left = [1]
        prod = 1
        # left values
        for i in range(len(nums) - 1):
            prod = prod * nums[i]
            products_left.append(prod)

        #right values
        prod = 1
        products_right = [1]
        for i in range(len(nums) - 2, -1, -1): 
            products_right.insert(0, products_right[0] * nums[i+1])
            # print (products_right, "  ", i)
        
        products = []
        for i in range(len(nums)): 
            products.append(products_right[i] * products_left[i])
        
        
        return products



        