from pathlib import Path
import json
import plotly.express as px
import pandas as pd
#文件路径
#数据来源Web地址： earthquake.usgs.gov 
path = Path('JSON/Geo_data/eq_30_days_m1.geojson')   
try:
   contents =  path.read_text()     
except:      #将数据读入contents
   contents =  path.read_text(encoding='utf-8')  
all_eq_data = json.loads(contents)   #转化为Python对象

# path = Path('JSON/Geo_data/eq_30_days_m1.geojson')   
# readable_contents = json.dumps(all_eq_data,indent=4)
# path.write_text(readable_contents)

#创建地震列表
all_eq_dicts=all_eq_data['features']
print(len(all_eq_dicts))  #输出为184 记录了这个文件里一共发生了184次地震

#输出地震的震等级： 对应字典 all_eq_data[i]['properties']['msg']
mags,titles,lons,lats= [],[],[],[] #地震等级>1
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]  #经度
    lat = eq_dict['geometry']['coordinates'][1]  #纬度
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
# print(mags[:20]) #只打印前20个
# print(titles[:2])
# print(lons[:5])
# print(lats[:5])
# 预期输出
# [1.56, 0.99, 1, 1.72, 4.7, 1.9, 1.7, 1.51, 1.07, 1.15, 4.4, 2, 1.05, 1.1, 1.51, 3.2, 2.09, 2, 1.6, 5.2]
# ['M 1.6 - 22 km NE of San Ardo, CA', 'M 1.0 - 8 km ESE of Valle Vista, CA']
# [-120.7611694, -116.8185, -116.8191667, -121.4095001, 125.7969]
# [36.1863327, 33.7091667, 33.7068333, 36.7721672, 10.0647]

#封装
data = pd.DataFrame(
   data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']  #可以将变量转化为字段
)
data.head()
#绘制散点图
fig = px.scatter(
      data,
      x='经度',
      y='纬度',
      range_x = [-200,200],
      range_y = [-90,90],
      width= 800,
      height= 800,
      title="全球地震散点图",
      size='震级',
      size_max=10, 
      color='震级',
      hover_name='位置',
)
fig.write_html('global_eqks.html')
fig.show()

