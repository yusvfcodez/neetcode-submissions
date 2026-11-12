class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        need = {}  # letters we must collect, and how many
        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}  # letters currently inside our window
        got, want = 0, len(need)  # how many letter types are fully collected
        best = (float("inf"), 0, 0)  # (length, left, right)
        l = 0

        for r, c in enumerate(s):
            have[c] = have.get(c, 0) + 1
            if c in need and have[c] == need[c]:
                got += 1

            # window is valid, so shrink it from the left
            while got == want:
                if r - l + 1 < best[0]:
                    best = (r - l + 1, l, r)
                left_char = s[l]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    got -= 1
                l += 1

        length, l, r = best
        return s[l:r + 1] if length != float("inf") else ""