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

### 1.标题

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

大体如下

![image](https://raw.githubusercontent.com/prometheus-code/tk-/master/image/3.jpg)

### 2.label显示区

- 做这个的思路是来自window里的计算器里放结果的地方无法直接通过键盘修改数字所以选用Label，当然也可以用文本框代替

- 作用:保留上一个运算式和结果并显示出来

  ~~~
  text1=tk.StringVar()
  label1 =tk.Label(root, width=25,anchor='se',textvariable=text1)#显示的文本内容向右对齐
  label1.grid(row=0,column=0,columnspan=5)#把label1放在窗口里的第一行
  ~~~

大体如下

![image](https://raw.githubusercontent.com/prometheus-code/tk-/master/image/4.jpg)

   在root.mainloop前加一段测试label(测试完后删去这段)

> text1.set("hello world")

 ![image](https://raw.githubusercontent.com/prometheus-code/tk-/master/image/5.jpg)

 ### 3.文本框

- 作用:作为开始计算运算式前的缓存区

  ~~~
  entry1=tk.Entry(root, width=25, justify="right")#使输入从右往左 
  entry1.grid(row=1, column=0, columnspan=5, sticky=tk.N + tk.W + tk.S + tk.E)
  ~~~

大体如下

![image](https://raw.githubusercontent.com/prometheus-code/tk-/master/image/6.jpg)

可能有点看不到文本框的显示，我随便写几个数字进去

![image](https://raw.githubusercontent.com/prometheus-code/tk-/master/image/7.jpg)

这样就完成了以上三个部分。

### 4.按钮区

- 这个部分可能是工程量最大的地方，我们先搞好布局，再考虑按钮调用的问题
  - 关于布局可以参考我的布局
  - ![image](https://raw.githubusercontent.com/prometheus-code/tk-/master/image/1.jpg)

我们先安放两行按钮

~~~
button_z1= tk.Button(width=5,text='(') 
button_z2= tk.Button(width=5,text=')')
button_clear= tk.Button(width=5,text='C')
button_del= tk.Button(width=5,text='←')
button_rem= tk.Button(width=5,text='%')

button_z1.grid(row=2, column=0)
button_z2.grid(row=2, column=1)
button_clear.grid(row=2, column=2)
button_del.grid(row=2, column=3)
button_rem.grid(row=2, column=4,rowspan=2,sticky=tk.N+tk.S)

button_7= tk.Button(width=5,text=' 7 ')
button_8= tk.Button(width=5,text=' 8 ')
button_9= tk.Button(width=5,text=' 9 ')
button_div= tk.Button(width=5,text=' / ')
        
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_div.grid(row=3, column=3)
~~~

大体如下

![image](https://raw.githubusercontent.com/prometheus-code/tk-/master/image/8.jpg)



- 我们把按钮的宽度定为5是因为我们前面的label显示区和文本框的宽度都定为25，为了安放5个按钮一行，所以我们定位一个按钮的宽度为5.



接下来到剩下的三行按钮
