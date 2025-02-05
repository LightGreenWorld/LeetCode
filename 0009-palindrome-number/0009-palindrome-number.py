class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x;
        strr = str(x);
        l = len(strr);
        result = False;
        if l >= 2:
            for i in range(l//2):
                if strr[i] == strr[-i+l-1]:
                    result = True;
                else:
                    result = False;
                    break;
        elif l == 1:
            result = True;
        else:
            result = False;
        return result
            
                
