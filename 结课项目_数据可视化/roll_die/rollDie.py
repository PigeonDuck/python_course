from Die import Die
import plotly.express as px

#函数:投掷骰子N次
def rollDie_N(n):  
  results = [] 
  for roll_num in range(n):
    results.append(die.roll())  #将骰子投掷的结果存入数组results
  return results

#统计每个点数出现的次数
def frequencies_of_everysides(results,N):
    frequencies = []
    for i in range(1*N,(die.num_sides*N+1)):    #[3,19)
           frequencies.append(results.count(i))
    return frequencies

#一次投掷N个骰子，重复n次
def NDie_rolling_n_Times(N,n):
  #没有初值 不能依次对应的加！
  results = [0]*n
  for i in range(n):
    for _ in range(N):
       random_num = die.roll() 
       results[i]+=random_num    
  return results


die = Die()                 #创建对象
N_Die = 1
rolling_times = 1000
results = NDie_rolling_n_Times(N_Die,rolling_times)
frequencies = frequencies_of_everysides(results,N_Die)


# print(results)
# print(frequencies)
# print(len(frequencies))
#依次传递数组里的值
# 例如：
# x轴 ：[1,6]
# y轴 ：[171, 160, 172, 168, 170, 159]
#添加标签
title = "Results of Rolling Three D6 1,000 Times"
labels = {'x':'Result','y':'Frequency of Result'}
fig = px.bar(x=range(N_Die,die.num_sides*N_Die+1),y=frequencies,title=title,labels=labels)        # [1,7)
fig.show()


#print(rollNDies(3,1000))
#同时投掷骰子D6三次 统计结果：

