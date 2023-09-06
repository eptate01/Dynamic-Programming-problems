def LongestCommonSubtring(subStr1,subStr2):
    n = len(subStr1)
    m = len(subStr2)
    suffix = []
    holder = []
    result = 0
    position = [0,0]
    for i in range(0,m+1):
        holder.append(0)
    for x in range(0,n+1):
        suffix.append([i for i in holder])

    for i in range(1,n+1):
        for x in range(1,m+1):
            if subStr1[i-1] == subStr2[x-1]:
                suffix[i][x] = suffix[i-1][x-1] + 1
                temp = result
                result = max(result, suffix[i][x])
                if temp != result:
                    position = [i, x]
    
    subStr = subStr1[position[0]-result:position[0]]
    return subStr

def subsequence(arr):
    n = len(arr)
    lis = [0]*n
    result = []

    for i in range(1,n):
        for j in range(0,i):
            if arr[j] < arr[i] and lis[i] < lis[j] + arr[i]:
                lis[i] = lis[j] + arr[i]

    
    maxPosition = lis.index(max(lis))
    result.append(arr[maxPosition])
    lis = lis[0:maxPosition]
    maxPosition = lis.index(max(lis))
    while maxPosition > 0 and sum(lis) > 0:
        if not(result[-1] > arr[maxPosition]):
            lis[maxPosition] = 0
            maxPosition = lis.index(max(lis))
        else:
            result.append(arr[maxPosition])
            lis = lis[0:maxPosition]
            maxPosition = lis.index(max(lis))

    return result[::-1]

def PatternCount(str, pattern):
    strLength = len(str)
    patternLength = len(pattern)
    countTable = [[0]*(patternLength+1) for i in range(strLength+1)]
    for i in range(strLength+1):
        countTable[i][0] = 1

    for i in range(1,strLength + 1):
        for j in range(1,patternLength+1):
            if str[i-1] == pattern[j-1]:
                countTable[i][j] = countTable[i-1][j-1] + countTable[i-1][j]
            else:
                countTable[i][j] = countTable[i-1][j]
    return countTable[-1][-1]

def DiffUtility(str1, str2):
    n = len(str1)
    m = len(str2)
    suffix = []
    holder = []
    result = 0
    for i in range(0,m+1):
        holder.append(0)
    for x in range(0,n+1):
        suffix.append([i for i in holder])

    for i in range(1,n+1):
        for x in range(1,m+1):
            if str1[i-1] == str2[x-1]:
                suffix[i][x] = suffix[i-1][x-1] + 1
            else:
                suffix[i][x] = max(suffix[i-1][x], suffix[i][x-1])
    
    result = max(max(x) for x in suffix)
    LCS = ""
    temp_n = n #length str1
    temp_m = m #length str2
    while temp_n > 0 and temp_m > 0:
        if str1[temp_n-1] == str2[temp_m-1]: 
            LCS += str1[temp_n-1]
            temp_n -= 1
            temp_m -= 1
        elif suffix[temp_n -1][temp_m] > suffix[temp_n][temp_m-1]:
            temp_n -= 1
        else:
            temp_m -= 1
    LCS = LCS[::-1]

    index_str1 = 0 
    index_str2 = 0 
    LCSindex = 0
    diffUtility = ""
    while LCSindex < len(LCS) and index_str1 < n and index_str2 < m:
        if str1[index_str1] != LCS[LCSindex]:
            diffUtility += "-"
            diffUtility += str1[index_str1]
            index_str1 += 1
        elif str2[index_str2] != LCS[LCSindex]:
            diffUtility += ("+")
            diffUtility += str2[index_str2]
            index_str2 += 1
        else:
            diffUtility += LCS[LCSindex]
            index_str1 += 1
            index_str2 += 1 
            LCSindex += 1
    while index_str1 < n:
        diffUtility += "-"
        diffUtility += str1[index_str1]
        index_str1 += 1
    while index_str2 < m:
        diffUtility += ("+")
        diffUtility += str2[index_str2]
        index_str2 += 1
    return diffUtility



    
    

print(LongestCommonSubtring("ABABC","BABCA"))
print(subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]))
print(PatternCount("subsequence", "sue"))
print(DiffUtility("ZNDGT", "XZDGST"))