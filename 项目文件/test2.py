def bouncing_ball(h, bounce, window):
    times = 0
    if h < window :    
        return -1
    # your code
    if h > window :        # 10 > 5
        times = times + 1    # 1
        h_ball = h * bounce  # h_ball = 6.6
        while True:
            if h_ball > window : # 6.6 > 5 
               h_ball = h_ball * bounce
               times = times + 2
            else:
               break
    return times

print(bouncing_ball(30, 0.75, 1.5))


def solution(number):
    #pass
    sum  =  0
    for num in range(0,number):
        if num%3==0 or num%5==0:
            sum=sum+num
    return sum         
#print(solution(10))

def solution(number):
    #pass
    list_number = [x for x in range(0,number) if x%3==0 or x%5==0 ]
    return sum(list_number)


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

#print(duplicate_encode("sucess"))

def disemvowel(string_):  

    letters = [letter for letter in string_ ]
    new_string = []
    print(letters)
    cnt = 0
    for i in range(0,len(string_)):
        if letters[i]!='i' and letters[i]!='a' and letters[i]!='e' and letters[i]!='o' and letters[i]!='u' and letters[i]!='I' and letters[i]!='A' and letters[i]!='E' and letters[i]!='O' and letters[i]!='U' :
            new_string.append(letters[i])
    print(new_string)
    string_ = ''.join(new_string) 
    return string_


print(disemvowel("This website is for losers LOL!"))



