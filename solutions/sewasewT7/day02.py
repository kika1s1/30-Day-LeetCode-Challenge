class Solution(object):
    def containsDuplicate(self, nums):

        number = set()
        for num in nums:
            if num in number:
                return True
            number.add(num)
        return False