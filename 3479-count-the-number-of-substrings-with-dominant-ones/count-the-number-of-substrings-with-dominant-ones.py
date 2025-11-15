class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros_pos = [i for i,ch in enumerate(s) if ch == '0']
        ans = 0

        # Z = 0: all-ones substrings
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                L = j - i
                ans += L * (L + 1) // 2
                i = j
            else:
                i += 1

        # If there are no zeros, we're done
        if not zeros_pos:
            return ans

        m = len(zeros_pos)
        import math
        Zmax = int(math.sqrt(n)) + 2

        # Precompute prefix sums of ones for quick ones_inside calculation if needed.
        # But we can compute ones_inside from positions: ones_inside = (z[r] - z[l] + 1) - Z
        for Z in range(1, Zmax + 1):
            if Z > m:
                break
            # iterate windows of Z zeros: zeros_pos[i] ... zeros_pos[i+Z-1]
            for i in range(0, m - Z + 1):
                left_zero_idx = i - 1
                right_zero_idx = i + Z
                zL = zeros_pos[i]
                zR = zeros_pos[i + Z - 1]

                prev_zero_pos = zeros_pos[left_zero_idx] if left_zero_idx >= 0 else -1
                next_zero_pos = zeros_pos[right_zero_idx] if right_zero_idx < m else n

                Lleft = zL - prev_zero_pos - 1   # number of ones available to the left
                Lright = next_zero_pos - zR - 1  # number of ones available to the right

                # ones present inside the span [zL .. zR] excluding the Z zeros:
                span_len = zR - zL + 1
                ones_inside = span_len - Z

                need = Z * Z - ones_inside
                total_pairs = (Lleft + 1) * (Lright + 1)
                if need <= 0:
                    # all pairs (left_expand, right_expand) valid
                    ans += total_pairs
                    continue

                # Count pairs (a,b) with 0<=a<=Lleft, 0<=b<=Lright and a + b <= need-1 (these are invalid)
                cap = need - 1
                # If cap >= Lleft + Lright then all pairs are invalid
                if cap >= Lleft + Lright:
                    # all pairs invalid -> add 0
                    continue

                # Compute count_bad = number of (a,b) with a+b <= cap
                # For a from 0..Lleft, b can be 0..min(Lright, cap - a)
                # sum_{a=0..Lleft} max(0, min(Lright, cap - a) + 1)
                # We can compute by splitting ranges where cap - a >= Lright and where it's <0 etc.
                # Let A = Lleft, B = Lright
                A = Lleft
                B = Lright
                c = cap

                # a values with (cap - a) >= B  => a <= cap - B
                t = max(-1, c - B)  # largest a where min(Lright, cap-a) == B
                count_bad = 0
                if t >= 0:
                    # for a in [0..t], b has (B+1) choices each
                    count_bad += (t + 1) * (B + 1)

                # remaining a in [t+1 .. min(A, c)] have b choices = (cap - a + 1)
                start = t + 1
                end = min(A, c)
                if start <= end:
                    # sum_{a=start..end} (cap - a + 1) = (end-start+1)*(cap+1) - sum_{a=start..end} a
                    cnt = end - start + 1
                    s_a = (start + end) * cnt // 2
                    count_bad += cnt * (c + 1) - s_a

                # a > cap => cap - a < 0 => zero choices (no contribution)
                valid = total_pairs - count_bad
                if valid > 0:
                    ans += valid

        return ans
