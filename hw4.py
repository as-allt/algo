import time
pure_recursive_record=[]
dynamic_programming_record=[]
pure_recursive_record.append(0)
dynamic_programming_record.append(0)
def pure_recursive(n):
    end_time=time.time()
    if(end_time-start>=60):
        return 100
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return pure_recursive(n-1) +pure_recursive(n-2)
def dynamic_programming(n):
    a=1
    b=1
    c=0
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    return c
for i in range(1,11):
    
    if(pure_recursive_record[-1]>60):
        pure_recursive_record.append(70)
    else:
        start = time.time()
        ans = pure_recursive(10*i)
        end=time.time()
        if(ans):
            pure_recursive_record.append(end-start)
        
    end1=time.time()
    dynamic_programming(10*i)
    end2=time.time()
    dynamic_programming_record.append(end2-end1)
    
number=[0,10,20,30,40,50,60,70,80,90,100]
import matplotlib.pyplot as plt
def chart():
    plt.plot(number, pure_recursive_record, color='red',linewidth=0.5,label='recursive')
    plt.plot(number, dynamic_programming_record, color='green',linewidth=0.5,label='dynamic')
    plt.title('comparsion', fontsize=14)
    plt.xlabel('n', fontsize=14)
    plt.ylabel('time', fontsize=14)
    #plt.xlim(100,10000)
    #plt.ylim(0,0.003)
    plt.grid(True)
    plt.show()
print(pure_recursive_record)
print(dynamic_programming_record)
chart()


#######################################################################################################################################################
def fibonacci(n):
    if n == 1:
        return 1
    if n==0:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 0
while True:
    try:
        fibonacci(n+1)
        n += 1
    except RecursionError:
        print("The maximum value of n is:", n-1)
        break
def dynamic_programming(n):
    a=1
    b=1
    c=0
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    return c
print(dynamic_programming(n))


