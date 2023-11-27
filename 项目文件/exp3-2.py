def duplicate_encode(word):
    #your code here
    #提前处理大小写
    word = word.lower()
    list_num = []
    for i in range(0,len(word)):
        list_num.append('(')   

    for i in range(0,len(word)):
        for j in range(0,len(word)):
            if word[j] == word[i] and j!=i :
                list_num[j]=')'
    str1 = ''.join(list_num)
    return str1