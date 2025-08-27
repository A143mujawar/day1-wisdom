def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 1:
        return s
    
    start, max_len = 0, 1  
    
    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1  
    
    for i in range(n):
     
        l1, r1 = expand(i, i)
        if r1 - l1 + 1 > max_len:
            start, max_len = l1, r1 - l1 + 1
        
  
        l2, r2 = expand(i, i + 1)
        if r2 - l2 + 1 > max_len:
            start, max_len = l2, r2 - l2 + 1
    
    return s[start:start + max_len]



print(longestPalindrome("babad"))  
print(longestPalindrome("cbbd"))
