# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        duplicateFiles=[]
        for filePath in paths:
            fileNames = filePath.split() 
            directoryPath = fileNames[0]
            for file in fileNames[1:]:
                fileName,fileContent = file[:file.index('(')],file[file.index('('):-1]
                if fileContent not in dic:
                    dic[fileContent] = []
                dic[fileContent].append(directoryPath+'/'+fileName)
        for value in dic.values():
            if len(value)>1: 
                duplicateFiles.append(value)
        return duplicateFiles[::-1]