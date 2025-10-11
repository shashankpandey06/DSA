class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        freq = Counter(power)
        
        
        unique = sorted(freq.keys())
        n = len(unique)
        
        
        dp = [0] * n
        dp[0] = unique[0] * freq[unique[0]]
        
        for i in range(1, n):
            curr_damage = unique[i] * freq[unique[i]]
            
            
            j = bisect.bisect_right(unique, unique[i] - 3) - 1
            
            if j >= 0:
                dp[i] = max(dp[i - 1], dp[j] + curr_damage)
            else:
                dp[i] = max(dp[i - 1], curr_damage)
        
        return dp[-1]
        