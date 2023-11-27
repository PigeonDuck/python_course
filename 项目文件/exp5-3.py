ZIMU_DIC=[
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]


def remove_duplicates_using_set(string): #去除重复的元素
    unique_chars = set(string)
    result = ''.join(unique_chars)
    return result

def is_pangram(s):
    s = remove_duplicates_using_set(s).lower()
    print(s)
    string = ''
    for str in s:
        if  str in ZIMU_DIC:
            string += str 
            
    string  = remove_duplicates_using_set(string)        
    print(string)
    if len(string) >= 26 :
        print(len(string))
        return True
    else:
        return False


#print(is_pangram('sklteziuqprcvgbjwhyod1fxnm'))

#print(remove_duplicates_using_set('The quick brown fox jumps over the lazy dog'))