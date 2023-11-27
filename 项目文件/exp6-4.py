
list1 = [
{ 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
{ 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
{ 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
{ 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]

def maxAge(lst):
    max_Age =  lst[0]['age']
    for i in range(0,len(lst)):
        if lst[i]['age'] > max_Age:
            max_Age = lst[i]['age'] 
    return max_Age

def find_senior(lst): 
    max_Age = maxAge(lst)
    dev = list(filter(lambda d: d['age']== max_Age ,lst))
    return dev



