def solution(number):
    #pass #直接生成满足条件的列表
    list_number = [x for x in range(0,number) if x%3==0 or x%5==0 ]
    return sum(list_number)