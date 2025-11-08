class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        i = n.bit_length() - 1
        return (1 << (i + 1)) - 1 - self.minimumOneBitOperations(n ^ (1 << i))
