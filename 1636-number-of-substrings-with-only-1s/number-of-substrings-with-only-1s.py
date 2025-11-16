class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        count = 0
        result = 0
        
        for ch in s:
            if ch == '1':
                count += 1
            else:
                result = (result + count * (count + 1) // 2) % mod
                count = 0
        
        # For the last sequence if ends with ones
        result = (result + count * (count + 1) // 2) % mod
        return result
