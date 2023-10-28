# Get the length of the input list
        n = len(nums)

        # Iterate through each element in the list
        for i in range(n):
            # For each element, check all subsequent elements
            for j in range(i + 1, n):
                # If the sum of the current element and a subsequent element equals the target,
                # return the indices of the two elements
                if nums[i] + nums[j] == target:
                    return [i, j]