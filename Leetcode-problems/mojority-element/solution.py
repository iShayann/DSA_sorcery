class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}

        for i in nums:
            mp[i] = mp.get(i,0) + 1

        return max(mp, key= lambda x: mp[x])