def Get_nextLineColor(row):
    DIC_ROW ={  
    'GG': 'G',
    'BB': 'B',
    'RR': 'R',
    'GB': 'R',
    'BG': 'R',
    'GR': 'B',
    'RG': 'B',
    'BR': 'G',
    'RB': 'G'
    } 
    new_row =''
    #print("==================")
    for i in range(0,len(row)):
        str = []
        if i!= len(row) -1 :
            str.append(row[i])  #每两个数据为一组
            str.append(row[i+1])
            str_temp = ''.join(str) 
            #print(str_temp)            
            new_row = new_row + DIC_ROW[str_temp]
            #print("new_row="+new_row)    #print("new_row="+new_row)
    return new_row
    

def triangle(row):

    #所有比100000小的幂次
    reduce=[3**i+1 for i in range(11) if 3**i<=100000][::-1]
    
    print(reduce)
    #if len(row) in reduce:
    DIC_ROW ={  
    'GG': 'G',
    'BB': 'B',
    'RR': 'R',
    'GB': 'R',
    'BG': 'R',
    'GR': 'B',
    'RG': 'B',
    'BR': 'G',
    'RB': 'G' } 
    print(len(row))
    for i in reduce:
        while len(row)>=i:
            str=[]
            if len(row) == i:
                str.append(row[0])  #每两个数据为一组
                str.append(row[-1])
                str_temp = ''.join(str) 
                row = DIC_ROW[str_temp]
                return row 
            row = Get_nextLineColor(row)
    return row 

print(triangle('RGGBBRRGGGRGGRGRGG'))