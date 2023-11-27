list1 = [
        { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
        { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
        { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
        { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
        ]

# def count_developers(lst):
#     cnt = 0
#     #print(len(lst))
#     for i in range(0,len(lst)):
#         if lst[i]['continent'] == 'Europe' and lst[i]['language'] == 'JavaScript' :
#             cnt += 1
#     return cnt

#print(count_developers(list1))

def count_developers(lst):
    dev = list(filter(lambda d: d['continent'] =='Europe' and d['language'] == 'JavaScript' ,lst))
    #print(dev)
    return len(dev)

#print(count_developers(list1))

