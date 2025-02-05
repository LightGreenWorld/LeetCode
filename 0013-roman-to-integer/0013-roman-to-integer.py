# The below code is based on "Bijoy Sing" on the "Solutions" board.

class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        n = len(s)

        i = 0
        while i < n:
            if i < n - 1 and mp[s[i]] < mp[s[i+1]]:
                ans += mp[s[i+1]] - mp[s[i]]
                i += 2
            else:
                ans += mp[s[i]]
                i += 1

        return ans

# My previous code was stuck in "CMLII". And I have to consider data structure of Dictionary to solve algorithm problem later.

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         self.s = s;

#         lst = []
#         for i in range(len(s)):
#             if s[i] == "I":
#                 lst.append(1)
#             elif s[i] == "V":
#                 lst.append(5)
#             elif s[i] == "X":
#                 lst.append(10)
#             elif s[i] == "L":
#                 lst.append(50)
#             elif s[i] == "C":
#                 lst.append(100)
#             elif s[i] == "D":
#                 lst.append(500)
#             elif s[i] == "M":
#                 lst.append(1000)

#         for j in range(len(s)//2):
#             if (s.find("IX") != -1 or s.find("IV") != -1) and j == 0:
#                 lst.append(-2)
#             elif (s.find("XC") != -1 or s.find("XL") != -1) and j == 1:
#                 lst.append(-20)
#             elif (s.find("CM") != -1 or s.find("CD") != -1) and j == 2:
#                 lst.append(-200)
  
#         return sum(lst)