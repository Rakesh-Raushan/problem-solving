class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #obvious solution looks like:
        count_zero = 0
        product_all = 1
        for n in nums:
            if n==0:
                count_zero+=1
            product_all*=n
        
        #i have total product and count of zeros
        # handle one or more zero cases first
        if count_zero>1:
            return [0]*len(nums)
        elif count_zero==1:
            except_zero_prod = 1
            zero_idx = 0
            for i,n in enumerate(nums):
                if n!=0:
                    except_zero_prod*=n
                else:
                    zero_idx = i

            except_zero_product_arr = [0]*len(nums)
            except_zero_product_arr[zero_idx] = except_zero_prod
            return except_zero_product_arr
        else:
            product_except_self_arr = []
            for n in nums:
                product_except_self_arr.append(int(product_all/n))
            return product_except_self_arr

        
        
        