class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Use a dictionary to store the indices of numbers

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in num_indices:
                # If found, return the indices of the two numbers
                return [num_indices[complement], i]

            # If not found, add the current number and its index to the dictionary
            num_indices[num] = i

        # If no solution is found, return an empty list or handle it as needed
        return []
