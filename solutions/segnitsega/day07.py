
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        slide = []
        max_slide = []
        for i in range(len(nums) - k + 1):
            slide.append(tuple(nums[i:i+k]))
            max_slide.append(max(slide[i]))

        return max_slide