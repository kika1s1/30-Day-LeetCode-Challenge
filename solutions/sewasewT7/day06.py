class Solution(object):
    def longestPalindrome(self, s):
        nw=""
        for i in range(len(s)):
            wrd=''
            for j in range(i,len(s)):
                wrd+=s[j]
                if wrd==wrd[::-1]:
                    if len(wrd)>len(nw):
                        nw=wrd
        return nw