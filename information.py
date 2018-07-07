#!/usr/bin/env python
#coding=utf-8
#Author:Willard Zhu

import time
import random
import signal
import re
from tkinter import *

all_problem=[]
answers=[]
def getRandomData():
    a=random.randint(1,10)
    b=random.randint(1,10)
    c=random.randint(1,10)
    d=random.randint(1,10)
    e=random.randint(1,10)
    f=random.randint(1,10)
    if a>=b or c>=d:
        if a+2>10:
            a-=2
        else:
            a+=2
        if d+2>10:
            d-=2
        else:
            d+=2
    if e==f:
        if e+2>10:
            e-=2
    return a,b,c,d,e,f

def getProblem(a,b,c,d,e,f):
    tar=random.randint(0,2)
    right_result=-1
    if tar==0:
    #包含括号
        tar0=random.randint(0,1)
        #决定括号的位置
        if tar0==0:
            right_result=(a+b+c)*d
            problem='({0} + {1} + {2}) * {3} = '.format(a,b,c,d)
            #all_problem.append(problem) 
            #print('(',a,' + ',b,' + ',c,' ) * ',d,' = ')
            print(problem,'\n')
                
        if tar0==1:
            right_result=a+(b+c)*d
            problem='{0} + ( {1} + {2} ) * {3} = '.format(a,b,c,d)
            #all_problem.append(problem)
            #print(a,' + (',b,' + ',c,' ) * ',d,' = ')
            print(problem)
        return right_result,problem
    
    if tar==1:
    #乘+加/减
        if a*b-c*d<0:
            problem='{0} * {1} + {2} * {3} = '.format(a,b,c,d)
            #all_problem.append(problem)
            print('{0} * {1} + {2} * {3} = '.format(a,b,c,d))
            right_result=a*b+c*d
            
        else:
            problem='{0} * {1} - {2} * {3} = '.format(a,b,c,d)
            #all_problem.append(problem)
            print('{0} * {1} - {2} * {3} = '.format(a,b,c,d))
            right_result=a*b-c*d
        return right_result,problem
    
    if tar==2:
    #分数+加/减
        if (a/b)-(c/d)-(e/f)<0:
            problem='{0} / {1} + {2} / {3} + {4} / {5} = '.format(a,b,c,d,e,f)
            #all_problem.append(problem)
            print('{0} / {1} + {2} / {3} + {4} / {5} = '.format(a,b,c,d,e,f))
            right_result=a/b+c/d+e/f            
        else:
            problem='{0} / {1} - {2} / {3} - {4} / {5} = '.format(a,b,c,d,e,f)
            #all_problem.append(problem)
            print('{0} / {1} - {2} / {3} - {4} / {5} = '.format(a,b,c,d,e,f))
            right_result=a/b-c/d-e/f
        return right_result,problem

def main():
    def handler(signum, frame):
        raise AssertionError

    for i in range(0,1000):
        try:
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(20)
            a,b,c,d,e,f=getRandomData()
            right_result,problem=getProblem(a,b,c,d,e,f)
            all_problem.append(problem)
            answers.append(right_result)

            windows=Tk()
            windows.wm_title('考试系统')
            windows.geometry("1000x500+300+200")
            l1 = Label(windows, text="基础四则运算测试系统",compound='center',font=('微软雅黑','30'))
            l1.pack()
            l2=Label(windows,text=problem,compound='center',font=('微软雅黑','20')).pack()
            l3=Label(windows,text='Input your answer:',font=('微软雅黑','20'))
            l3.pack(ipadx=3)
            e=Entry(windows)
            def evaluate(event):
                res.configure(text = "Your answer is: " + str(e.get()),font=('微软雅黑','20'))
                if re.findall('/',str(e.get())):
                    a=str(e.get()).split('/')
                    b=[]
                    for i in a:
                        b.append(int(i))
                    if b[0]/b[1] == right_result:
                        judge.configure(text='Accept!',font=('微软雅黑','15'))
                    else:
                        judge.configure(text='Wrong Answer!',font=('微软雅黑','15'))
                else:
                    if int(str(e.get()))==right_result:
                        judge.configure(text='Accept!',font=('微软雅黑','15'))
                    else:
                        judge.configure(text='Wrong Answer!',font=('微软雅黑','15'))
            

            e.bind('<Return>',evaluate)
            e.pack()
            res=Label(windows)
            res.pack()
            judge=Label(windows)
            judge.pack()
            windows.mainloop()
            time.sleep(2)
            windows.destroy()
            signal.alarm(0)
        except:
            print("timeout\n")


    f1 = open('/home/willard/Desktop/problems.txt','w')
    f2 = open('/home/willard/Desktop/answers.txt','w')
    print('All the problem is here:\n')

    for i in all_problem:
        #print(i,'\n')
        f1.write(i+'\n')
    for i in answers:
        #rint(i,'\n')
        f2.write(str(i)+'\n')
    print('Save all problems and answers.')
    f1.close()
    f2.close()
    

if __name__=='__main__':
    main()
