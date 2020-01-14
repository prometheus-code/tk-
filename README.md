# 计算器

## 要用到的库

- tkinter库

## 开始思路

1. python的shell框里输入加减乘除可以直接给出答案

2. python的内置函数eval()函数可以执行一个字符串表达式，并返回表达式的值。

3. tkinter库可以给我们提供按钮输入数字和运算符，也可以提供文本框显示值。

## tkinter库里可能用到的函数以及选项

- 注：选项里的master只是表示主容器名，可以替换

1. Label(master,width= ,anchor= ,textvariable= )
2. Button(master,width= ,text= ,command= )
3. Entry(master,width= ,justify= )

## 其他注意事项

1. Button里的command是只能调用函数，不能使用方法，所以为了实现command使用方法可以用匿名函数lambda
2. 多次调用Button时，可能会出现一些要多次重复的选项，这时可以使用functools模块里的partial()函数固定住这些选项的输入

## 可视化框架建设

![image](https://raw.githubusercontent.com/prometheus-code/tk-/master/image/1.jpg)

​																		预览图片

- 根据预览图片大体可以分为四个部分:

1. 标题

2. label显示区

3. 文本框

4. 按键区

### 标题

​	首先我们先导入模块并创建一个窗口

~~~
import tkinter as tk
import tkinter.messagebox 
root=tk.Tk()
root.title("计算器")
"""
后面在这里写label显示区，文本框和按键区的代码，并删去备注
"""
root.mainloop()
~~~

![image](https://raw.githubusercontent.com/prometheus-code/tk-/master/image/3.jpg)



   
