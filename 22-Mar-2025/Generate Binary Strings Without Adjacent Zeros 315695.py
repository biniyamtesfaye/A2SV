# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=["0","1"]
        while (n>0):
            if n==1:
                return ans
            else:
                for i in range(len(ans)): 
                    if ans[i][len(ans[i])-1]=="0":       
                        ans[i]=ans[i]+"1"
                    else: 
                        ans.append(ans[i]+"1")
                        ans[i]=ans[i]+"0"
            n-=1

                        

            
            