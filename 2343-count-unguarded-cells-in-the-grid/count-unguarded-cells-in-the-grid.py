class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guard_set = set(map(tuple, guards))
        wall_set = set(map(tuple, walls))
        guarded = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left

        for gr, gc in guards:
            for dr, dc in directions:
                r, c = gr + dr, gc + dc
                while 0 <= r < m and 0 <= c < n:
                    if (r, c) in wall_set or (r, c) in guard_set:
                        break
                    guarded.add((r, c))
                    r += dr
                    c += dc

        total_cells = m * n
        occupied = len(guard_set) + len(wall_set)
        unguarded = total_cells - len(guarded) - occupied
        return unguarded
