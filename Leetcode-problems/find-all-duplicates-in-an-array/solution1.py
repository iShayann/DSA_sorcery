class Solution:
    def findDuplicates(self, nums):
        cop_list = [0] * (len(nums) + 1)
        new_dup_list = []
        if len(nums) <= 1: return []
        for i in range(len(nums)):
            cop_list[nums[i]] += 1
            if cop_list[nums[i]] == 2:
                new_dup_list.append(nums[i])
        return new_dup_list