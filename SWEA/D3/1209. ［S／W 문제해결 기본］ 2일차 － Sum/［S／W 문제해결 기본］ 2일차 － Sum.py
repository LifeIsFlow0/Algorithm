for tc in range(1, 11):
    
    howmany = int(input())
    Data = [list(map(int, input().split())) for i in range(100)]
    res = maxNum = 0

    for i in range(0,100):
        res = 0
        for j in range(0,100):
            res += Data[i][j]
            if maxNum < res:
                maxNum = res
            
    for i in range(0,100):
        res = 0
        for j in range(0,100):
            res += Data[j][i]
            if maxNum < res:
                maxNum = res

    res = 0
    for i in range(0,100):
        res += Data[i][i]

        if maxNum < res:
            maxNum = res

    res = 0
    for i in range(0,100):
        res += Data[i][99-i]

        if maxNum < res:
            maxNum = res


    print(f"#{tc} {maxNum}")