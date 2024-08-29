class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return n
        if n == 2:
            return n

        #Initializing the base cases
        first = 1
        second = 2

        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current

        return second

solution = Solution()
print(solution.climbStairs(5))
