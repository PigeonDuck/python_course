def Get_nextLineColor(row):
    DIC_ROW ={  
    'GG': 'G',  'BB': 'B','RR': 'R',
    'GB': 'R',  'BG': 'R', 'GR': 'B',
    'RG': 'B',  'BR': 'G','RB': 'G'
    } 
    reduce=[3**i+1 for i in range(11) if 3**i<=100000][::-1]
    new_row=''
    str=[]
    
    if len(row) in reduce:
        print(True)
        str.append(row[0])  #每两个数据为一组
        str.append(row[-1])
        str_temp = ''.join(str) 
        new_row = DIC_ROW[str_temp]
        return new_row
    
    for duce in reduce:
        if len(row) >= duce:
            str=[]
            for i in range(0,len(row)):
                str = []
                str.append(row[i])     
                if i+duce <= len(row):
                    str.append(row[i+duce-1])
                    str_temp = ''.join(str)
                    new_row = new_row + DIC_ROW[str_temp]
                else:
                    break
            row = new_row       
            break 
    return new_row
def triangle(row):
    while len(row) > 1:
        row = Get_nextLineColor(row)
    return row

print(triangle('RGB'),'结果')
# length of row not in the reduce:
# closest reduce-1 is 9: 
# row=[COLOR[row[i] + row[i+length-1]] for i in range(len(row)-length+1)]
# for i in range(12 - 10 + 1 =1) 
# for i in range(1)
# COLOR[row[0] + row[0+12-1]] 
# e.g.    RGGBBRRGGGRG
# B B G
#  B R
#   G 
#R G B
# B R
#  G