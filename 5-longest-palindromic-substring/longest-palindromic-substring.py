class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return ""
        
        start, max_length = 0, 1

        for i in range(len(s)):
            # Check for odd-length palindrome
            start, max_length = self.expandAroundCenter(s, i, i, start, max_length)
            # Check for even-length palindrome
            start, max_length = self.expandAroundCenter(s, i, i + 1, start, max_length)

        return s[start:start + max_length]

    def expandAroundCenter(self, s, left, right, start, max_length):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_length = right - left + 1
            if current_length > max_length:
                start = left
                max_length = current_length
            left -= 1
            right += 1
        return start, max_length