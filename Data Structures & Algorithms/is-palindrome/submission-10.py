class Solution:
    def isPalindrome(self, s: str) -> bool:
        newList = []
     
        for i in range(len(s)): 
            if s[i].isalnum(): 
                newList.append(s[i].lower())
        length = len(newList) - 1
        stop = len(newList) // 2
        for i in range(stop): 
            if newList[i] != newList[length - i]: 
                return False
        return True



        