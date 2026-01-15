class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        def max_consecutive(arr):
            arr.sort()
            longest = curr = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    curr += 1
                else:
                    curr = 1
                longest = max(longest, curr)
            return longest

        max_h = max_consecutive(hBars) + 1
        max_v = max_consecutive(vBars) + 1
        side = min(max_h, max_v)
        return side * side
