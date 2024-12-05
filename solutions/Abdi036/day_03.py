 class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1,nums2 = sorted(nums1),sorted(nums2)
        ptr1,ptr2 = 0,0

        while(ptr1 < len(nums1) and ptr2 < len(nums2)):
            if(nums1[ptr1] > nums2[ptr2]):
                ptr2 += 1
            elif(nums1[ptr1] < nums2[ptr2]):
                ptr1 += 1
            else:
                res.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
        return res