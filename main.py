#!/usr/bin/python3
# -*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox
import numpy as np
import nash
import math

class MainWindow:

    def __init__(self, root):

        self.varName = []
        self.entryName = []

        for i in range(0,8):
            self.varName.append(tkinter.StringVar(value=''))

        self.labelName = tkinter.Label(
            root, text='支付矩阵:', justify=tkinter.RIGHT, width=80)
        self.labelName.place(x=40, y=15, width=80, height=20)

        self.labelName = tkinter.Label(
            root, text='A', justify=tkinter.RIGHT, width=80)
        self.labelName.place(x=40, y=55, width=80, height=20)

        self.labelName = tkinter.Label(
            root, text='B', justify=tkinter.RIGHT, width=80)
        self.labelName.place(x=200, y=15, width=80, height=20)

        for i in range(0,4):
            self.entryName.append(tkinter.Entry(
                root, width=80, textvariable=self.varName[i*2]))
            self.entryName[i*2].place(x=150 + 100*(i%2), y=35 + 30*(i//2), width=30, height=20)

            self.entryName.append(tkinter.Entry(
                root, width=80, textvariable=self.varName[i*2+1]))
            self.entryName[i*2+1].place(x=200 + 100*(i%2), y=35 + 30*(i//2), width=30, height=20)

        self.buttonOk = tkinter.Button(root, text='计算', command=self.call)
        self.buttonOk.place(x=30, y=100, width=50, height=20)
        self.buttonCancel = tkinter.Button(
            root, text='清空', command=self.cancel)
        self.buttonCancel.place(x=90, y=100, width=50, height=20)

        # root.mainloop()

    def call(self):
        array1 = []
        array2 = []
        for i in range(0,4):
            if self.isNum(self.entryName[i * 2].get()) == False or self.isNum(self.entryName[i*2+1].get()) == False:
                tkinter.messagebox.showerror("Error", "输入不合法！")
                return
            array1.append(int(self.entryName[i*2].get()))
            array2.append(int(self.entryName[i*2+1].get()))

        A = np.array([array1[0:2], array1[2:4]])
        B = np.array([array2[0:2], array2[2:4]])

        rps = nash.Game(A, B)
        # print(rps)
        eqs = rps.support_enumeration()
        # print(list(eqs))

        label = tkinter.Label(root, text='计算结果:',
                              justify=tkinter.RIGHT, width=80)
        label.place(x=10, y=140, width=80, height=20)
        text2 = tkinter.Text(root, height=20, width=50)

        set_precision = 4
        cnt = 1
        for ans in eqs:
            tmp = '策略'+str(cnt)+': '+'('+'('+str(round(ans[0][0],set_precision))+','+str(round(ans[0][1],set_precision))+')'+' , '
            tmp += '('+str(round(ans[1][0],set_precision))+','+str(round(ans[1][1],set_precision))+')'+')'
            tmp += '\n'
            # print (tmp)
            text2.insert('end', tmp)
            cnt += 1

        text2.place(x=10, y=160)
        # text2.pack()

    def cancel(self):
        for i in range(0,8):
            self.varName[i].set('')
    
    def isNum(self,value):
        try:
            x = int(value)
        except TypeError:
            return False
        except ValueError:
            return False
        except Exception as err:
            return False
        else:
            return True


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Nash')
    root.geometry('410x500+300+300')
    window = MainWindow(root)
    root.mainloop()
    # MainWindow.main_action()

# For debug
# A = np.array([[50, 100], [900, -20]])
# B = np.array([[50, 800], [600, -30]])
