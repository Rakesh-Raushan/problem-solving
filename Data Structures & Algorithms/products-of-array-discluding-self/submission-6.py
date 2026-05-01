class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_products, post_products = [], []

        pre_prod = 1
        i=0
        while i < len(nums):
            pre_prod *= nums[i]
            pre_products.append(pre_prod)
            i+=1
         
        post_prod = 1
        i = len(nums)-1
        while i >=0:
            post_prod *= nums[i]
            post_products.append(post_prod)
            i-=1
        
        pre_products = [1] + pre_products
        post_products = [x for x in reversed(post_products)] + [1]

        idx = 1
        result = []
        for i in range(len(nums)):
            result.append(pre_products[idx-1] * post_products[idx])
            idx+=1
        
        return result
        