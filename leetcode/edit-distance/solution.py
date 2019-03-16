def minDistance(word1, word2):
    dp = [[0] * (len(word1) + 1) for l in range(len(word2) + 1)]

    # first row is from 0 to len(word1) + 1
    for i in range(len(word1) + 1):
        dp[0][i] = i

    # same for first column
    for i in range(len(word2) + 1):
        dp[i][0] = i
    
    for i in range(1, len(word2) + 1):
        for j in range(1, len(word1) + 1):
            # if letters are different we take min from diag, left, top cells and add 1
            if word1[j-1] != word2[i-1]:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            else:
                # we take diagonal val and add 0
                dp[i][j] = dp[i-1][j-1]


    return dp[-1][-1]
