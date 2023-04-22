# Linear Search in Python
import random
import time

x_axis_linear=[]
y_axis_linear=[]
x_axis_binary=[]
y_axis_binary=[]
x_axis_fibnoacci=[]
y_axis_fibnoacci=[]

def create_array():
    record_linear=0
    record_binary=0
    record_fibnoacci=0
    for i in range(1,101):
        
        array_=[]
        for c in range(5):
            array = []
            b=10*i
            for c in range(b):
                array.append(random.randrange(10000))
            array.sort()
            array_.append(array)
        x_axis_linear.append(b)
        x_axis_binary.append(b)
        x_axis_fibnoacci.append(b)

        start=time.time()
        for c in range(5):
            x = random.randrange(10000)
            n = len(array_[c])
            linearSearch(array_[c],n,x)
        end=time.time()
        y_axis_linear.append(end-start)
        record_linear+=(end-start)/5

        start=time.time()
        for c in range(5):
            x = random.randrange(10000)
            n = len(array_[c])
            binary_search(array_[c],x,n)
        end=time.time()
        y_axis_binary.append(end-start)
        
        record_binary+=(end-start)/5

        start=time.time()
        for c in range(5):
            x = random.randrange(10000)
            n = len(array_[c])
            fibonacci_search(array_[c],x,n)
        end=time.time()
        y_axis_fibnoacci.append(end-start)
        record_fibnoacci+=(end-start)/5
        print(end-start)

    print("linear:",record_linear)
    print("binary:",record_binary)
    print("fibnoacci:",record_fibnoacci)

def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

def binary_search(data, key,n):
    #設置選取範圍的指標
    low = 0
    upper = n - 1
    while low <= upper:
        mid = (low + upper) // 2  #取中間索引的值
        if data[mid] < key:    #若搜尋值比中間的值大，將中間索引+1，取右半
            low = mid + 1
        elif data[mid] > key:  #若搜尋值比中間的值小，將中間索引+1，取左半
            upper = mid - 1
        else:                    #若搜尋值等於中間的值，則回傳
            return mid
    return -1




from bisect import bisect_left

def fibonacci_search(lst, target,size):
    
     
    start = -1
     
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
     
     
    while(f2 > 1):
        index = min(start + f0, size - 1)
        if lst[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (lst[size - 1] == target):
        return size - 1
    return None

import matplotlib.pyplot as plt
def chart():
    plt.plot(x_axis_linear, y_axis_linear, color='red',linewidth=0.5,label='linear')
    plt.plot(x_axis_binary, y_axis_binary, color='green',linewidth=0.5,label='binary')
    plt.plot(x_axis_fibnoacci, y_axis_fibnoacci, color='blue',linewidth=0.5,label='fibnoacci')
    plt.title('comparsion', fontsize=14)
    plt.xlabel('n', fontsize=14)
    plt.ylabel('time', fontsize=14)
    plt.xlim(100,10000)
    plt.ylim(0,0.003)
    plt.grid(True)
    plt.show()

def main():
    # linear_Search()
    # binarySearch()  
    # fibonacciSearch()
    
    create_array()
    #chart()
main()