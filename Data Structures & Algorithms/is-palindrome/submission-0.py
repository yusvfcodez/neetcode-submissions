class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # skip anything that's not a letter or number
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # compare (lowercase so "A" equals "a")
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True