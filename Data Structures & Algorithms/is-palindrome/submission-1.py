class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        frontIndex = 0
        backIndex = len(s) - 1
        print("frontIndex", frontIndex)
        print("backIndex", backIndex)

        while backIndex > frontIndex and frontIndex < len(s) and backIndex > 0:
            print(" in loop")
            if s[frontIndex].isalnum() == False:
                frontIndex += 1
                continue
            if s[backIndex].isalnum() == False:
                backIndex -= 1
                continue
            
            if s[frontIndex] != s[backIndex]:
                print(s[frontIndex],  s[backIndex])
                return False

            print("front ", s[frontIndex])
            print("back ", s[backIndex])
            frontIndex += 1
            backIndex -= 1

        return True
            
