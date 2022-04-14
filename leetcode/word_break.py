class Solution:              
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        dp = [i == 0 for i in range(len(s)+1)]
        for i in range(1, len(s) + 1):
            #print(dp)
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]
      
solution = Solution()
print(solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

#dp