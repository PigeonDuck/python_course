
def reverse_words(word):
    string = ''.join(reversed(word))
    return string 

def spin_words(sentence):
    str = []
    str = sentence.split(' ')
    print(str)    
    for i in range(0,len(str)):
        if len(str[i]) >= 5:
            str[i] = reverse_words(str[i])
    string = ' '.join(str)
    return string

print(spin_words("Hey fellow warriors"))