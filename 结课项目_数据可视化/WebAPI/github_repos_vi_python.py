import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept":"application/vnd.github.v3+json"}  #指定版本
r = requests.get(url,headers=headers)  #将响应对象储存在r中
print(f"Status code:{r.status_code}")  #打印状态码 若状态码为200 则响应成功
#将结果转化为json格式
response_dict = r.json()
print(f"完成结果:{not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']                #存储所有的仓库
print(f"Repositories returned:{len(repo_dicts)}")  #实际返回： returned 30

repo_links,stars,hover_texts =[],[],[]

#请求网页--->获取数据--->图片可视化
#为数据赋值
for repo_dict in repo_dicts:
    #默认会显示xy轴的信息
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    #增加悬停窗的信息
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text) 
    # repo_link = repo_dict['html_url']
   
#绘制图像
title = "Most-Starred Pythonn Projects on Github" #标题
labels = {'x':'Repository','y':'Stars'}
fig = px.bar(x= repo_links,y=stars,title=title,labels=labels,
             hover_name=hover_texts)

fig.update_layout(title_font_size=28,xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.show()

#
