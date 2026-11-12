class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = [0] * 26  # letter counts for s1
        c2 = [0] * 26  # letter counts for current window in s2

        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1

        # how many of the 26 letters have the same count
        matches = 0
        for i in range(26):
            if c1[i] == c2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # add the new letter on the right
            i = ord(s2[r]) - ord('a')
            c2[i] += 1
            if c1[i] == c2[i]:
                matches += 1
            elif c1[i] + 1 == c2[i]:
                matches -= 1

            # remove the old letter on the left
            i = ord(s2[l]) - ord('a')
            c2[i] -= 1
            if c1[i] == c2[i]:
                matches += 1
            elif c1[i] - 1 == c2[i]:
                matches -= 1
            l += 1

        return matches == 26