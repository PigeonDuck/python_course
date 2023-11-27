bracks =  {'C':'X'}


c = 'C'

print(bracks[c])  
#字典可以通过键值来打印的value元素内容



def v_b(s):
    bracks = {'(':')','{':'}','[':']'}
    stack =[]
    for x in s:
        if x in bracks.keys():
            stack.append(x)   
        else:
            if len(s)==0 or bracks[stack.pop()]!=x:
                return False
    return True
