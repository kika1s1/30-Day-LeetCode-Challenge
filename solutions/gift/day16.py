class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum == target:
                return [l, r]
            elif current_sum < target:
                l += 1
            else:
                r -= 1
