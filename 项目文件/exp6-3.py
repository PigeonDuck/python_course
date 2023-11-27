def shorten_number(suffixes, base):
    # 定义一个函数
    def my_filter(data):
        try:
            # 将函数输入转换为整数
            number = int(data)
        # 如果输入的数据不能转换为整数，直接转换为str返回
        except (TypeError, ValueError):
            return str(data)
        else:
            i = 0
            while number // base > 0 and i < len(suffixes) -1:
                number = number // base
                i += 1
            return  str(number) + suffixes[i] 
    return my_filter

# 可以人为的来定义这个函数如何过滤
filter1 = shorten_number(['','k','m'],1000)  # 返回值为一个函数
print(filter1('23456'))