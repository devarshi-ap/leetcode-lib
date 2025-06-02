class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = {}
        for chr in magazine:
            magazineDict[chr] = magazineDict.get(chr, 0) + 1

        for chr in ransomNote:
            print(chr, magazineDict)
            if chr in magazineDict:
                if magazineDict[chr] == 1:
                    del magazineDict[chr]
                else:
                    magazineDict[chr] -= 1
            else:
                return False
        
        return True