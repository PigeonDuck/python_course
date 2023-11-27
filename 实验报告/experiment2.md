# 实验二 Python变量、简单数据类型

班级： 21计科1班

学号： B20210302127

姓名： 刘嘉伟

Github地址：<https://github.com/PigeonDuck/python_course>

CodeWars地址：<https://www.codewars.com/users/DuckPigeon>

---

## 实验目的

1. 使用VSCode编写和运行Python程序
2. 学习Python变量和简单数据类型

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

实验环境的安装

1. 安装Python，从Python官网下载Python 3.10安装包，下载后直接点击可以安装：[Python官网地址](https://www.python.org/downloads/)
2. 为了在VSCode集成环境下编写和运行Python程序，安装下列VScode插件
   - Python
   - Python Environment Manager
   - Python Indent
   - Python Extended
   - Python Docstring Generator
   - Jupyter
   - indent-rainbow
   - Jinja

---

### 第二部分

Python变量、简单数据类型和列表简介

完成教材《Python编程从入门到实践》下列章节的练习：

- 第2章 变量和简单数据类型

---

### 第三部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第1题：求离整数n最近的平方数（Find Nearest square number）

难度：8kyu

你的任务是找到一个正整数n的最近的平方数
例如，如果n=111，那么nearest_sq(n)（nearestSq(n)）等于121，因为111比100（10的平方）更接近121（11的平方）。
如果n已经是完全平方（例如n=144，n=81，等等），你需要直接返回n。
代码提交地址
<https://www.codewars.com/kata/5a805d8cafa10f8b930005ba>  

---

#### 第2题：弹跳的球（Bouncing Balls）

难度：6kyu

一个孩子在一栋高楼的第N层玩球。这层楼离地面的高度h是已知的。他把球从窗口扔出去。球弹了起来,  例如:弹到其高度的三分之二（弹力为0.66）。他的母亲从离地面w米的窗户向外看,母亲会看到球在她的窗前经过多少次（包括球下落和反弹的时候）？

一个有效的实验必须满足三个条件：

- 参数 "h"（米）必须大于0
- 参数 "bounce "必须大于0且小于1
- 参数 “window "必须小于h。

如果以上三个条件都满足，返回一个正整数，否则返回-1。
**注意:只有当反弹球的高度严格大于窗口参数时，才能看到球。**
代码提交地址
<https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python>

---
#### 第3题： 元音统计(Vowel Count)

难度： 7kyu

返回给定字符串中元音的数量（计数）。对于这个Kata，我们将考虑a、e、i、o、u作为元音（但不包括y）。输入的字符串将只由小写字母和/或空格组成。

代码提交地址：
<https://www.codewars.com/kata/54ff3102c1bad923760001f3>
<br>
代码如下：

---

#### 第4题：偶数或者奇数（Even or Odd）

难度：8kyu

创建一个函数接收一个整数作为参数，当整数为偶数时返回”Even”当整数位奇数时返回”Odd”。
代码提交地址：
<https://www.codewars.com/kata/53da3dbb4a5168369a0000fe>

---
### 第四部分

使用Mermaid绘制程序流程图


## 实验过程与结果

请将实验过程与结果放在这里，包括：

- [第二部分 Python变量、简单数据类型和列表简介](#第二部分)
- [第三部分 Codewars Kata挑战](#第三部分)
- [第四部分 使用Mermaid绘制程序流程图](#第四部分)  
- 
第三部分:  
  #### 第1题：求离整数n最近的平方数（Find Nearest square number）

难度：8kyu

你的任务是找到一个正整数n的最近的平方数
例如，如果n=111，那么nearest_sq(n)（nearestSq(n)）等于121，因为111比100（10的平方）更接近121（11的平方）。
如果n已经是完全平方（例如n=144，n=81，等等），你需要直接返回n。
代码提交地址
<https://www.codewars.com/kata/5a805d8cafa10f8b930005ba>  
<br>
代码如下：
```python
def nearest_sq(n):
  a =  (int(n**0.5)+1)**2
  b =   int(n**0.5)**2
  if (n - b) < (a - n):
    return b
  else :
    return a
```
---

#### 第2题：弹跳的球（Bouncing Balls）

难度：6kyu

一个孩子在一栋高楼的第N层玩球。这层楼离地面的高度h是已知的。他把球从窗口扔出去。球弹了起来,  例如:弹到其高度的三分之二（弹力为0.66）。他的母亲从离地面w米的窗户向外看,母亲会看到球在她的窗前经过多少次（包括球下落和反弹的时候）？

一个有效的实验必须满足三个条件：

- 参数 "h"（米）必须大于0
- 参数 "bounce "必须大于0且小于1
- 参数 “window "必须小于h。

如果以上三个条件都满足，返回一个正整数，否则返回-1。
**注意:只有当反弹球的高度严格大于窗口参数时，才能看到球。**
代码提交地址
<https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python>
<br>
代码如下：
```python
def bouncing_ball(h, bounce, window):
    times = 0
    if h <= window :    
        return -1
    if bounce <= 0 or bounce>=1:
        return -1
    if h<=0 :
        return -1
    # your code
    if h > window and bounce<1 and bounce>0 and h>0 and window>0:        # 10 > 5
        times = times + 1    # 1
        h_ball = h * bounce  # h_ball = 6.6
        while True:
          if h_ball > window : # 6.6 > 5 
             h_ball = h_ball * bounce
             times = times + 2
          else:
            break
    return times
```
---
#### 第3题： 元音统计(Vowel Count)

难度： 7kyu

返回给定字符串中元音的数量（计数）。对于这个Kata，我们将考虑a、e、i、o、u作为元音（但不包括y）。输入的字符串将只由小写字母和/或空格组成。

代码提交地址：
<https://www.codewars.com/kata/54ff3102c1bad923760001f3>
<br>
代码如下：
```python
def get_count(sentence):
    #pass
    cnt = 0
    for stcs in sentence:
        if stcs == 'a' or stcs == 'e' or stcs == 'i' or stcs == 'o' or stcs == 'u':
            cnt = cnt + 1
    return cnt
```
---

#### 第4题：偶数或者奇数（Even or Odd）

难度：8kyu

创建一个函数接收一个整数作为参数，当整数为偶数时返回”Even”当整数位奇数时返回”Odd”。
代码提交地址：
<https://www.codewars.com/kata/53da3dbb4a5168369a0000fe>
<br>
代码如下：
```python
def even_or_odd(number):
    if number % 2 == 0 :
      return "Even"
    else:
      return "Odd"
```
---


第四部分：  
使用Mermaid绘制程序流程图
第4题：偶数或者奇数（Even or Odd）  流程图的绘制

显示效果如下：

```mermaid
flowchart LR
    A[Start] --> B{n%2==0?}
    B -->|Yes| C[retrun 'Even']
    C ---->E[End]
    B -->|No| D[return 'Odd']
    D ---->E[End]
```
![流程图](./odd.png)


## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

1. Python中的简单数据类型有那些？我们可以对这些数据类型做哪些操作？  
   int、float、bool、complex、list、string、Tuple、set、dictionary
2. 为什么说Python中的变量都是标签？    
   python中的变量不是容器，而是指向python对象的标签，对象位于解释器的命名空间中，但是
任意数量的标签可以指向同一个对象，当对象发生变化时，所有指向它的变量的值都会改变。

3. 有哪些方法可以提高Python代码的可读性？  
   规范代码格式，封装代码块，添加注释，起有意义的变量名
## 实验总结
本次实验学会了使用VSCode编写和运行Python程序。
通过完成Kata的挑战和对书本的学习，进一步了解了Python变量和简单数据类型。