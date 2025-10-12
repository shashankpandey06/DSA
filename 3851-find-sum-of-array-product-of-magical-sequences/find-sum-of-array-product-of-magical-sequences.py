from typing import List
from math import comb

MOD = 10**9 + 7

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        # Precompute combination values C(a,b) for a up to m and b up to m
        # Use Python's math.comb for exact integers, then take mod when used.

        # Precompute powers pow(nums[i], t, MOD) for t=0..m
        pow_num = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for t in range(1, m + 1):
                pow_num[i][t] = (pow_num[i][t-1] * nums[i]) % MOD

        # dp[r][carry][ones] = sum contribution after processing some indices
        # where r = number of picks used so far (0..m), carry (0..m), ones (0..k)
        # We'll iterate indices; initialize for zero indices processed:
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1  # no picks used, no carry, zero ones -> coefficient 1

        for idx in range(n):
            ndp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]
            # for all states
            for used in range(0, m + 1):
                for carry in range(0, m + 1):
                    for ones in range(0, k + 1):
                        cur = dp[used][carry][ones]
                        if cur == 0:
                            continue
                        rem = m - used
                        # choose t occurrences of current index (0..rem)
                        for t in range(0, rem + 1):
                            ways = comb(rem, t)  # choose positions among remaining -> builds multinomial
                            add = cur * ways % MOD
                            add = add * pow_num[idx][t] % MOD

                            total = t + carry
                            bit = total & 1
                            new_carry = total >> 1
                            new_used = used + t
                            new_ones = ones + bit
                            if new_ones > k:
                                # prune: already exceed target ones
                                continue
                            ndp[new_used][new_carry][new_ones] = (ndp[new_used][new_carry][new_ones] + add) % MOD
            dp = ndp

        # After processing all indices, consider remaining carry bits (no more nums to multiply)
        ans = 0
        for carry in range(0, m + 1):
            # popcount of carry may add extra ones
            pc = carry.bit_count()
            for ones in range(0, k + 1):
                if dp[m][carry][ones] == 0:
                    continue
                if ones + pc == k:
                    ans = (ans + dp[m][carry][ones]) % MOD

        return ans
