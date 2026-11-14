class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # stores indexes, values go from big to small

        for i, n in enumerate(nums):
            # remove smaller numbers from the back (they can never be the max)
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(i)

            # remove the front if it slid out of the window
            if q[0] <= i - k:
                q.popleft()

            # window is full, so save the biggest (the front)
            if i >= k - 1:
                res.append(nums[q[0]])

        return res