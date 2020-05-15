"""
You have given two string source and target. You need to convert soruce string
into target string.

You can acheive this by inserting a char or by deleting a char or by
replacing a char.

Return minimum operation you required to acheive the result.


"""

def editDistance(source, target, m,n): # m soruce string size, n target size
    dp = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            elif source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    return dp[m][n]
str1 = "geek"
str2 = "gesek"
print editDistance(str1, str2, len(str1), len(str2))

#  Time and space complexity O(m*n)
