
#from sort_definition import *
from  test1 import *
import random
import sys
sys.setrecursionlimit(1500)
N=random.randint(10,15)
N=16

A=[]
'''
for n in range(N):
    A.append(N-n)
print('The original list is:\n',A,'\n')
'''
A = [56, 132, 54, 28, 92, 54, 125, 95, 62, 107, 47, 44, 15, 87, 9, 34]
print('The original list is:\n',A,'\n')

a1=A.copy()
a2=A.copy()
a3=A.copy()
a4=A.copy()
a5=A.copy()
a6=A.copy()
a7=A.copy()
a8=A.copy()
a9=A.copy()

SelectSort(a1)
print(a1)
InsertSort(a2)
print(a2)
BubbleSort(a3)
print(a3)
ShellSort(a4)
print(a4)
MergeSort(a5,0, len(a5)-1)
print(a5)
QuickSort(a6,0, len(a5)-1)
print(a6)
HeapSort(a7)
print(a7)
CountingSort(a8)
print(a8)
RadixSort(a9)
print(a9)


#BubbleSort()
