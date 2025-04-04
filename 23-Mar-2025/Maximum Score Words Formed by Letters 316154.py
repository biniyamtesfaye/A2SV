# Problem: Maximum Score Words Formed by Letters - https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def dp(n,letter):
            ans=0
            if n==len(words):
                return 0
            ans=0
            m=letter
            for i in words[n]:
                if i not in m:
                    return dp(n+1,letter)
                m=m.replace(i,'',1)
                ans+=score[ord(i)-97]
            return max(dp(n+1,letter),ans+dp(n+1,m))
        return dp(0,''.join(letters))        