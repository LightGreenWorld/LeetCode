class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """
        My original approach was to extract shortest word in list and then compare each word.
        But, it made logic more complicated than I expected and I failed to solve.
        """
        # shortest = min(strs)
        # lenList = len(strs)
        
        # answer = ""

        # if len(strs) == 1:
        #     answer = ""
        # else:
        #     for i in range(0, lenList-1):
        #         for j in range(len(shortest)):
        #             if strs[i][j] == strs[i+1][j]:
        #                 answer += strs[i][j]
        #             else:
        #                 continue
        # return answer
    
        """
        The below code is Akbar's in "Solution" menu.
        I thought the function "sorted()" was not enough to exclude abnormality
        like a shortest or longest word without common prefix.
        Once descending order is applied by "sorted()", however,
        a word with smallest number of common prefix letters is put at the very front or back
        regardless of word length.
        """

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
