class Solution:
    def maxSumDivThree(self, nums):
        total = sum(nums)
        
        # Lists to keep the numbers with remainders 1 and 2
        rem1, rem2 = [], []
        
        for x in nums:
            if x % 3 == 1:
                rem1.append(x)
            elif x % 3 == 2:
                rem2.append(x)
        
        rem1.sort()
        rem2.sort()
        
        # If already divisible by 3
        if total % 3 == 0:
            return total
        
        # Option sums
        ans = 0
        if total % 3 == 1:
            option1 = total - (rem1[0] if rem1 else float('inf'))
            option2 = total - (rem2[0] + rem2[1] if len(rem2) >= 2 else float('inf'))
            ans = max(option1, option2)
        
        else:  # total % 3 == 2
            option1 = total - (rem2[0] if rem2 else float('inf'))
            option2 = total - (rem1[0] + rem1[1] if len(rem1) >= 2 else float('inf'))
            ans = max(option1, option2)
        
        return ans
