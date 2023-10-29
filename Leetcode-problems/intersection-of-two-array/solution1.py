class Solution():
    def intersection(self, nums1, nums2):
            new_set_1=set(nums1)
            new_set_2=set(nums2)
            duplicates=[]
            for element in new_set_1:
                if element in new_set_2:
                    duplicates.append(element)
            return duplicates
