class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        c = Counter(nums1)
        for num in nums2:
            if c[num] > 0:
                answer.append(num)
                c[num] -= 1
        return answer
    