import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox 

class ttk1():
    def __init__(self):
        self.label1()
        self.entry1()
        self.button1()
    
    def label1(self):
        global text1
        text1=tk.StringVar()
        label1 =ttk.Label(root, width=25,anchor='se',textvariable=text1)
        label1.grid(row=0,column=0,columnspan=5)
    
    def entry1(self):
        global entry1
        entry1=ttk.Entry(root, width=25, justify="right")
        entry1.grid(row=1, column=0, columnspan=5, sticky=tk.N + tk.W + tk.S + tk.E)

    def button1(self):
        button_z1= ttk.Button(width=5,text='(',command=lambda:entry1.insert(tk.INSERT,'(')) 
        button_z2= ttk.Button(width=5,text=')',command=lambda:entry1.insert(tk.INSERT,')'))
        button_clear= ttk.Button(width=5,text='C',command=lambda:self.clear())
        button_del= ttk.Button(width=5,text='←',command=lambda:entry1.delete(len(entry1.get()) -1))
        button_rem= ttk.Button(width=5,text='%',command=lambda:entry1.insert(tk.INSERT,'%'))

        button_z1.grid(row=2, column=0)
        button_z2.grid(row=2, column=1)
        button_clear.grid(row=2, column=2)
        button_del.grid(row=2, column=3)
        button_rem.grid(row=2, column=4,rowspan=2,sticky=tk.N+tk.S)

        button_7= ttk.Button(width=5,text=' 7 ',command=lambda:entry1.insert(tk.INSERT,'7'))
        button_8= ttk.Button(width=5,text=' 8 ',command=lambda:entry1.insert(tk.INSERT,'8'))
        button_9= ttk.Button(width=5,text=' 9 ',command=lambda:entry1.insert(tk.INSERT,'9'))
        button_div= ttk.Button(width=5,text=' / ',command=lambda:entry1.insert(tk.INSERT,'/'))
                
        button_7.grid(row=3, column=0)
        button_8.grid(row=3, column=1)
        button_9.grid(row=3, column=2)
        button_div.grid(row=3, column=3)

        button_4=ttk.Button(width=5,text=' 4 ',command=lambda:entry1.insert(tk.INSERT,'4'))
        button_5=ttk.Button(width=5,text=' 5 ',command=lambda:entry1.insert(tk.INSERT,'5'))
        button_6=ttk.Button(width=5,text=' 6 ',command=lambda:entry1.insert(tk.INSERT,'6'))
        button_multiply=ttk.Button(width=5,text=' * ',command=lambda:entry1.insert(tk.INSERT,'*'))
        button_is=ttk.Button(width=5,text=' \n = \n ',command=lambda:self.enter())

        button_4.grid(row=4, column=0)
        button_5.grid(row=4, column=1)
        button_6.grid(row=4, column=2)
        button_multiply.grid(row=4, column=3)
        button_is.grid(row=4, column=4, rowspan=5,sticky=tk.N+tk.S)

        button_1=ttk.Button(width=5,text=' 1 ',command=lambda:entry1.insert(tk.INSERT,'1'))
        button_2=ttk.Button(width=5,text=' 2 ',command=lambda:entry1.insert(tk.INSERT,'2'))
        button_3=ttk.Button(width=5,text=' 3 ',command=lambda:entry1.insert(tk.INSERT,'3'))
        button_minus=ttk.Button(width=5,text=' - ',command=lambda:entry1.insert(tk.INSERT,'-'))

        button_1.grid(row=5, column=0)
        button_2.grid(row=5, column=1)
        button_3.grid(row=5, column=2)
        button_minus.grid(row=5, column=3)

        button_help=ttk.Button(width=5,text='HELP',command=lambda:tkinter.messagebox.showinfo('\
        提示','基本按照你想的去做就可以了，不过只能进行简单的运算'))#这里怕麻烦提前写上help键的调用
        button_0=ttk.Button(width=5,text=' 0 ',command=lambda:entry1.insert(tk.INSERT,'0'))
        button_point=ttk.Button(width=5,text=' . ',command=lambda:entry1.insert(tk.INSERT,'.'))
        button_add=ttk.Button(width=5,text=' + ',command=lambda:entry1.insert(tk.INSERT,'+'))

        button_help.grid(row=6, column=0)
        button_0.grid(row=6, column=1)
        button_point.grid(row=6, column=2)
        button_add.grid(row=6, column=3)

    def clear(self):
        entry1.delete(0,tk.END)
        text1.set(' ')

    def enter(self):
        en=eval(entry1.get())
        el=entry1.get()
        text1.set(el+'='+str(en))
        entry1.delete(0,tk.END)

if __name__ == "__main__":
    root=tk.Tk()
    root.title("ttk版计算器")
    root.resizable(0, 0)
    ttk1()
    root.mainloop()