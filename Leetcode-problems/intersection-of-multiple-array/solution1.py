class Solution:
    def intersection(self, nums):
        new_set = set(nums[0])
        for i in range(1, len(nums)):
            new_set &= set(nums[i])
        new_set = list(new_set)
        new_set.sort()
        return new_set