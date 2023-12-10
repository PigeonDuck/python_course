from pathlib import Path
import csv
import matplotlib.pyplot as plt
from  datetime import datetime
# import os
# print(os.getcwd())

#美国旧金山的温度列表
path = Path('CSV/weather_data/San_weather_data.csv')
lines = path.read_text().splitlines() #获取csv列表所有的信息
reader = csv.reader(lines)   #创建一个reader 对象将 lines 中所有的数值赋值给reader对象
header_row = next(reader)    #获取csv列表中的第一行数据（只调用一次为表头）
print(header_row)
for index,column_header in enumerate(header_row):   # enumerate()用于获取每个元素的索引以及值
    print(index, column_header)
#      0        1       2       3       4       5       6
#['STATION', 'NAME', 'DATE', 'TAVG', 'TMAX', 'TMIN', 'TOBS']
# 获取STATION编号"USC00503605"的最高气温：
dates,highs,lows = [],[],[]
station = "USC00503605"
for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    try:  
       if station == row[0]:
          high = int(row[4])
          low = int(row[5])
    except ValueError:
       print(f"Missing data for {current_date}")   
    else:
       if station == row[0]:
         dates.append(current_date)
         highs.append(high)
         lows.append(low)
#print(highs)
#绘制折线图
plt.style.use('default')
fig,ax = plt.subplots()     #fig 变量为 图形
#绘制数据到坐标轴
ax.plot(dates,highs,color='red') #数据1 最大温度
ax.plot(dates,lows,color='blue') #数据2 最小温度
ax.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.1)  #填充区域 alpha 表示透明度 facecolor 表示填充颜色
#给XY轴取名字
ax.set_title("Daily High and Low Temperatures,Aug 2023 data\nSan Francisco",fontsize=20)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)',fontsize=16)
ax.tick_params(labelsize=16)
plt.show()


