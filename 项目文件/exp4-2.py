def get_pins(observed):
   PIN_DiCT = {   #1234
   '1':['1','2','4'],
   '2':['2','1','5','3'],
   '3':['3','2','6'] , 
   '4':['4','1','5','7'],
   '5':['5','2','4','8','6'],
   '6':['6','3','5','9'],
   '7':['7','4','8'],
   '8':['8','7','9','5','0'],
   '9':['9','6','8'],
   '0':['0','8'] 
   }
   pins = [""]
   cnt = 0
   
   for obs in observed:
      new_pins = []           
      for adj in PIN_DiCT[obs]:
         for pin in pins: 
            new_pins.append(pin + adj) 
      pins = new_pins   
      print(pins)
   return pins

def get_pins(observed):
   dic={'1':['1','2','4'],
   '2':['1','2','3','5'],
   '3':['2','3','6'],
   '4':['1','4','5','7'],
   '5':['2','4','5','6','8'],
   '6':['3','5','6','9'],
   '7':['4','7','8'],
   '8':['5','7','8','9','0'],
   '9':['6','8','9'],
   '0':['8','0']}
   list=['']
   for c in observed:
      new_list=[]
      for k in dic[c]:
         for pin in list:
            new_list.append(pin+k)
      list=new_list
   return list

print(get_pins('1234'))

