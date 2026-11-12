class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}      # how many of each letter are in the window
        left = 0
        max_freq = 0    # biggest count of any one letter we've seen
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # window too big to fix with k changes? shrink it
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result