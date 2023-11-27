def find_outlier(integers):
    cnt = 0
    N =0
    print(integers)
    for integer in integers:
        if integer % 2  ==  0:
            cnt+=1 
        else :
            cnt-=1
    print(cnt)
    if cnt < 0:
        for integer in integers:
            if integer % 2 == 0 :
                N = integer
    if cnt >0:
        for integer in integers:
            if integer % 2 != 0 or integer == 1:
                N = integer
    print(N)
    return N