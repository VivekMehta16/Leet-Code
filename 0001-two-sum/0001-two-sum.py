class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevmap = {}
        
        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevmap:
                return[prevmap[diff],i]
            prevmap[n] = i
        return
        