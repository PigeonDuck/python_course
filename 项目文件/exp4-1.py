def naughty_or_nice(data):
    nice = 0
    
    for month in data:
        for day in data[month]:
            if data[month][day] == "Nice":
                nice = nice +1
            else :
                nice = nice -1
    return "Nice!" if nice >=0 else "Naughty!" 