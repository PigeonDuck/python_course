#设置格式
name = 'Eric'
message = f" Hello,{name} would u like to learn some Python today?"

#设置格式，大小写
famous_person = ' albert einstein '
say = '"A person who never made a mistake never tried anything new."'
message1 = f"{famous_person.strip().title()} once said,{say}"
print(name.upper(),name.lower(),famous_person.title())
print(message1)
print(message)

#删除前缀
url = 'https://pypi.tuna.tsinghua.edu.cn/simple'
url_simple = url.removeprefix('https://')
print( "\n"+ url_simple)


#数组的增删改

#增加: 1末尾追加 2索引插入
motorcycle = ['honda','yamaha','ducati']
motorcycle.append('suzuki') 
motorcycle.insert(4,'haray')
print(motorcycle[4])
print(motorcycle[-1])

#删除: 1索引删除 2直接删除 3值删除
motorcycle = ['honda','yamaha','ducati']
del motorcycle[0]
motorcycle.pop()
motorcycle.remove('yamaha')
print(motorcycle)


#改
motorcycle = ['honda','yamaha','ducati']
motorcycle[0] = 'suzuki'
print(motorcycle[0])





