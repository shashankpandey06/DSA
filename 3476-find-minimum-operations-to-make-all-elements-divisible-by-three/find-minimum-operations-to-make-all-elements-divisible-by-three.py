class Solution:
    def minimumOperations(self, nums):
        ops = 0
        for x in nums:
            if x % 3 != 0:
                ops += 1
        return ops
