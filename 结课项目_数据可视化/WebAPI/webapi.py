import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept":"application/vnd.github.v3+json"}  #指定版本
r = requests.get(url,headers=headers)  #将响应对象储存在r中
print(f"Status code:{r.status_code}")  #打印状态码 若状态码为200 则响应成功
#将结果转化为json格式
response_dict = r.json()
#打印字典所有的键值
print(response_dict.keys()) 

#输出所有的仓库数量
print(f"所有的仓库数量为:{response_dict['total_count']}")
print(f"完成结果:{not response_dict['incomplete_results']}")

#探索有关仓库的信息:只返回了前30个仓库
repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")  #returned 30


#研究第一个仓库
repo_dict = repo_dicts[0]             #第一个仓库
print(f"\nKeys:{len(repo_dict)}")     #键值长度为80 
for key in sorted(repo_dict.keys()):  #按照字母顺序排序关键词
   print(key)

for repo_dict in repo_dicts:
    print("\nSelected imformation about first repositories:")
    print(f"Name:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f"Stars:{repo_dict['stargazers_count']}")
    print(f"Repository:{repo_dict['html_url']}")
    print(f"Created:{repo_dict['created_at']}")
    print(f"Updated:{repo_dict['updated_at']}")
    print(f"Description:{repo_dict['description']}")
