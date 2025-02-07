# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution(object):
    def removeComments(self, source):

        result = []  
        block_comment = False
        buffer = []

        for line in source:
            i = 0
            while i < len(line):
                if block_comment:
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        block_comment = False
                        i += 1
                else:
                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        block_comment = True
                        i += 1
                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break
                    else:
                        buffer.append(line[i])
                i += 1
            if not block_comment and buffer:
                result.append("".join(buffer))
                buffer = []

        return result

        