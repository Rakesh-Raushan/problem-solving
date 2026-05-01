class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #so the idea is since we have two sorted arrays and we want to find the median withour merging them, we can do that by looking at the possible
        #contributions from the two sorted arrays that can lead to the sorted array
        #example, for two sorted array of sizes say 4 each, we would expected a sorted array of 8 or we can say that we expect 4 elements to the left of median
        #and these 4 can have contributions from each sorted possible like (0,4) (1,3), (2,2),(3,1)(4,0) or say if we choose to look at one array only
        #it will contribute any number between 0 to 4 and rest from second array
        #the interesting thing is out od 0,1,2,3,4 only one is unique one that can lead to overall sorted array
        #also if we know this number we know that say first n of first array goes to left of median since they are sorted
        #similarly first 4-n from 2nd goes to left of median
        #since we have all the numbers to the left half, we also can say we have all the numbers of the right half
        # we know that max of first half and min of second half are the ones that decide the median as average of the two for even number case
        # for the odd the max or min of the bigger set gives the median
        #we now use this logic to get the median
        #but even to find the number of contribution 0 to 4 we can take this as a search in ordered array and hence binary search can be applied

        #make 1 the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2) #we take smaller to avoid checks for higher contributions as valid ones

        #empty case:
        if not n1:
            if not n2:
                return float("-inf")
            elif n2%2==0:
                return (nums2[n2//2]+nums2[n2//2-1])/2
            else:
                return nums2[n2//2]
        elif not n2:
            if n1%2==0:
                return (nums1[n1//2]+nums1[n1//2-1])/2
            else:
                return nums1[n1//2]


        n = (n1 + n2)//2 #we plan to search in this space
        
        
        #now let's apply binary search with this condition of valid sorted overall array on n but we can further make our binary search efficient
        #using the fact that, if n1 or n2 are less than n then we just need to binary search in that lesser range
        #as we can not have more contribution than that
                
        left, right = 0, n1

        while(left <= right):
            mid = (left + right)//2
            #indices of max on left and min on right
            l1 = mid-1
            r1 = mid
            l2 = n-mid-1
            r2 = n-mid
            #boundary cases,
            #none from 1 or all from 1 valid conditions
            if l1 == -1:
                if nums2[l2] <= nums1[r1]:
                    #valid case, so calculate median
                    #even total
                    if n1==n2:
                        return (nums2[l2] + min(nums1[r1], nums2[r2]))/2
                    # if (n1+n2)%2 == 0:
                    #     return (nums2[l2] + min(nums1[r1], nums2[r2]))/2
                    else:
                        #odd case, left always smaller one due to integer div so min of n2 should decide median
                        # if n1>n2:
                        #     return nums1[0]
                        # else:
                        #     return nums2[-1]
                        return min(nums1[r1], nums2[r2])
                else:
                    #continue search
                    left = mid+1
            elif l1 == n1-1: #n1 is the max contributon possible from first array
                if max(nums1) <= min(nums2):
                    #valid case, so calculate median
                    #even total
                    if (n1+n2)%2 == 0:
                        return (nums1[-1] + nums2[0])/2
                    else:
                        #odd case
                        if n1>n2:
                            return nums1[-1]
                        else:
                            return nums2[0]
                else:
                    right = mid -1
            #some from 1 some from 2 valid conditions
            elif nums1[l1] <= nums2[r2] and nums2[l2] <= nums1[r1]:
                #valid case, so calculate median
                #even total
                if (n1+n2)%2 == 0:
                    return (max(nums1[l1], nums2[l2]) + min(nums1[r1], nums2[r2]))/2
                else:
                    #odd case
                    #since we are doing integer div, always the left one will be smaller
                    return min(nums1[r1], nums2[r2])
            else:
                if nums1[l1] > nums2[r2]:
                    #left search
                    right = mid - 1
                else:
                    left = mid + 1
        
                


        