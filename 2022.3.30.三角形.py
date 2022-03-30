class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = []
        for i in range(1,rowIndex+2):
            dp.append([1]*i)
        for i in range(2,len(dp)):
            for j in range(len(dp[i])):
                if j != 0 and j != len(dp[i])-1:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        return dp[-1]

