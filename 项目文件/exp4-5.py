# 假 设 单 位 时  间 长 度为 2 
#"点" - 1个时间单位长。   11   
#"划" - 3个时间单位长。   11 11 11
#字符内点和划之间的暂停 - 1个时间单位长。  00
#单词内字符之间的暂停 - 3个时间单位长。  00 00 00
#单词间的暂停 - 7个时间单位长。   00 00 00 00 00 00 00 

#极端情况
# 10001    二进制码
# 此时单位时间长度为多少？  
# 1 和 0 共同的最小单位长度为 1 
# 所以 ‘000’ 表示3个时间单位长度 对应 单词内字符的暂停 --》 '. .' --->decode-->  EE  
#  1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

# case of min_union() :
# case:  11001100110011000000
# print(min_union(list,bits,word))
# 预期结果为  list[2,2,2,6]   , min == 2 

MORSE_CODE = {'.-': 'A', 
            '-...': 'B',
            '-.-.': 'C', 
            '-..': 'D', 
            '.': 'E', 
            '..-.': 'F', 
            '--.': 'G', 
            '....': 'H', 
            '..': 'I', 
            '.---': 'J', 
            '-.-': 'K',
            '.-..': 'L',
            '--': 'M', 
            '-.': 'N',
            '---': 'O', 
            '.--.': 'P', 
            '--.-': 'Q',
            '.-.': 'R', 
            '...': 'S', 
            '-': 'T', 
            '..-': 'U', 
            '...-': 'V', 
            '.--': 'W',
            '-..-': 'X', 
            '-.--': 'Y',
            '--..': 'Z',
            '-----': '0',
            '.----': '1',
            '..---': '2',  
            '...--': '3', 
            '....-': '4', 
            '.....': '5', 
            '-....': '6', 
            '--...': '7', 
            '---..': '8', 
            '----.': '9', 
            '.-.-.-': '.',
            '--..--': ',', 
            '..--..': '?', 
            '.----.': "'", 
            '-.-.--': '!', 
            '-..-.': '/', 
            '-.--.': '(', 
            '-.--.-': ')', 
            '.-...': '&', 
            '---...': ':',
            '-.-.-.': ';',
            '-...-': '=', 
            '.-.-.': '+', 
            '-....-': '-', 
            '..--.-': '_', 
            '.-..-.': '"',
            '...-..-': '$',
            '.--.-.': '@', 
            '...---...': 'SOS'}

def min_union(lists,bits,word):
    cnt = 0
    for bit in bits:
        if bit == word :
            cnt += 1
        else:
            if cnt !=0 :
                lists.append(cnt)
                cnt = 0
    if cnt!=0:
        lists.append(cnt)      
    print(lists)
    return lists

# zerox_list =[]
# bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
# word = '1'
# print(min_union(zerox_list,bits,word))
def ReturnMinNum(A,B):
    if A >= B:
        return B
    if A <= B :
        return A
# 假 设 单 位 时  间 长 度为 2 
#"点" - 1个时间单位长。   11   
#"划" - 3个时间单位长。   11 11 11
#字符内点和划之间的暂停 - 1个时间单位长。  00
#单词内字符之间的暂停 - 3个时间单位长。  00 00 00
#单词间的暂停 - 7个时间单位长。   00 00 00 00 00 00 00 
def decode_bits(bits): 
    zero_list = []
    one_list  = []
    bits = bits.strip('0')
    #获取列表
    if '0' not in bits:
        minunit = len(bits)
        print(minunit)
    else:
        zero_list = min_union(zero_list,bits,'0')
        one_list =  min_union(one_list,bits,'1')
    #获取两个列表的最小单位
        min_zero = min(zero_list)
        min_one  = min(one_list)
    #求最小单位
        minunit = ReturnMinNum(min_one,min_zero)
            
    print(minunit)
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    return bits.replace('111'*minunit, '-').replace('0000000'*minunit,'/').replace('000'*minunit, ' ').replace('1'*minunit, '.').replace('0'*minunit, '')

#test case of decode_bits
#decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
#expected : ···· · −·−− ·−−− ··− −·· ·
#bits_temp = decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
#print(bits_temp)
#bits_temp = decode_bits('10001')

def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    print(morseCode)
    letter_str = []
    str = []
    if morseCode == '':
        return '' 
    morseCode = morseCode.strip()
    print(morseCode)
    for mcode in morseCode:
        if mcode != ' ':
            letter_str.append(mcode)
        if mcode == ' ':
            str.append(MORSE_CODE[''.join(letter_str)]) #添加到数组里
            #print(letter_str)
            letter_str = []     #然后重置  
        if mcode == '/':
            letter_str[-1] =''
            str.append(MORSE_CODE[''.join(letter_str)])
            str.append(' ')
            #print(letter_str)
            letter_str =[]
    str.append(MORSE_CODE[''.join(letter_str)]) 
    return ''.join(str)

#decode_bits('1001')
morseCode=decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
str = decode_morse(morseCode)
print(str)


