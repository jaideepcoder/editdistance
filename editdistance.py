def editdistance(s1, s2):
    """Method to calculate Damerau-Levenshtein Minimum Edit Distance between two strings.
Usage:
>>> editdistance('brilliant', 'briliant')
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
"""
    s1 = '#' + s1.upper()
    s2 = '#' + s2.upper()
    m=len(s1)
    n=len(s2)
    i=False
    d=False
    s=False
    r=False
    D = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            D[i][0]=i
            D[0][j]=j


    for i in range(m):
        for j in range(n):
            dis=[0]*4
            if i == 0 or j == 0:
                continue
            dis[0] = D[i-1][j] + 1
            dis[1] = D[i][j-1] + 1
            if s1[i] != s2[j]:
                dis[2] = D[i-1][j-1] + 2
            else:
                dis[2] = D[i-1][j-1]
            if s1[i] == s2[j-1] and s1[i-1] == s2[j]:
                if s1[i] != s1[i-1] and s2[j] != s2[j-1]:
                    dis[3] = D[i-1][j-1] - 1
            if dis[3] != 0:
                D[i][j] = min(dis[0:4])
            else:
                D[i][j] = min(dis[0:3])

    print '  ',
    for l in s2:
        print l+'  ',
    print '\n'

    for i in range(m):
        print s1[i],'',
        for j in range(n):
            print (D[i][j]),' ',
        print('\n')

    print "Damerau-Levenshtein Minimum Distance:",D[m-1][n-1]
    return D[m-1][n-1]

help(editdistance)
