def v_b(s):
    bracks = {'(':')','{':'}','[':']'}
    stack =[]
    for x in s:
        if x in bracks.keys():
            stack.append(x)   
        else:
            if len(stack)==0 or bracks[stack.pop()]!=x:
                return False
    return len(stack)==0
