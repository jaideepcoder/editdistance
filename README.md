editdistance
============

A program to calculate the Damerau-Levenshtein distance between two strings using dynamic programming.

editdistance(s1, s2)  
    Method to calculate Damerau-Levenshtein Minimum Edit Distance between two strings.  
    Usage:  
    >>> editdistance('brilliant', ''briliant')  
       #   B   R   I   L   I   A   N   T  
    #  0   1   2   3   4   5   6   7   8   
    
    B  1   0   1   2   3   4   5   6   7   
    
    R  2   1   0   1   2   3   4   5   6   
    
    I  3   2   1   0   1   2   3   4   5   
    
    L  4   3   2   1   0   1   2   3   4   
    
    L  5   4   3   2   1   2   3   4   5   
    
    I  6   5   4   3   1   1   2   3   4   
    
    A  7   6   5   4   2   2   1   2   3   
    
    N  8   7   6   5   3   3   2   1   2   
    
    T  9   8   7   6   4   4   3   2   1   
    
    Damerau-Levenshtein Minimum Distance: 1

