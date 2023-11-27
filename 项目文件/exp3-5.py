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
