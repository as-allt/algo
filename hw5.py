# Python code to implement the
# matrix chain multiplication using recursion

import sys

# Matrix A[i] has dimension p[i-1] x p[i]
# for i = 1..n
def Matrix_ChainOrder(p, i, j):
	if i == j:
		return 0

	_min = sys.maxsize

	# Place parenthesis at different places
	# between first and last matrix,
	# recursively calculate count of multiplications
	# for each parenthesis placement
	# and return the minimum count
	for k in range(i, j):

		count = (Matrix_ChainOrder(p, i, k)
				+ Matrix_ChainOrder(p, k + 1, j)
				+ p[i-1] * p[k] * p[j])

		if count < _min:
			_min = count

	# Return minimum count
	return _min


# Python program using memoization
import sys
dp = [[-1 for i in range(100)] for j in range(100)]

# Function for matrix chain multiplication
# def matrixChainMemoised(p, i, j):
# 	if(i == j):
# 		return 0
	
# 	if(dp[i][j] != -1):
# 		return dp[i][j]
	
# 	dp[i][j] = sys.maxsize
	
# 	for k in range(i,j):
# 		dp[i][j] = min(dp[i][j], matrixChainMemoised(p, i, k) + matrixChainMemoised(p, k + 1, j)+ p[i - 1] * p[k] * p[j])
	
# 	return dp[i][j]

# def MatrixChainOrder(p,n):
# 	i = 1
# 	j = n - 1
# 	return matrixChainMemoised(p, i, j)

def myself(arr,n):
	column=n
	row=n
	m=[[0]*row for _ in range(column)]
	for i in range(1,n):
		m[i][i]=0
	s=[[0]*row for _ in range(column)]
	
	for l in range(2,n):
		for i in range(1,n-l+1):
			j=i+l-1
			
			m[i][j]=sys.maxsize
			for k in range(i,j):
				tempCost = m[i][k] +m[k+1][j] +arr[i-1]*arr[k]*arr[j]
				if(tempCost<m[i][j]):
					m[i][j] = tempCost
					s[i-1][j-1]=k
	#print(m)
	return m[1][n-1]
			

	


# This code is contributed by rag2127

import random
import time
# Driver code

	
arr = [10,30,5,60,50]
x_axis_brute=[]
x_axis_dp=[]
y_axis_brute=[]
y_axis_dp=[]
b=5
while(b<=10):
    arr.append(random.randint(1,100))
    N = len(arr)
    n = len(arr)
    x_axis_brute.append(n)
    x_axis_dp.append(n)
    b+=1
    start = time.process_time_ns()
    print("Minimum number of multiplications is by Brute-Force Algorithm",Matrix_ChainOrder(arr, 1, N-1))
    end1 = time.process_time_ns()
    y_axis_brute.append(end1-start)
    print("Minimum number of multiplications is by Dynamic Programming Algorithm",myself(arr,n))
    end2  =time.process_time_ns()
    y_axis_dp.append(end2-end1)
    


# This code is contributed by Aryan Garg
import matplotlib.pyplot as plt
def chart():
    plt.plot(x_axis_brute, y_axis_brute, color='red',linewidth=0.5,label='brute')
    plt.plot(x_axis_dp, y_axis_dp, color='green',linewidth=0.5,label='dp')
    
    plt.title('comparsion', fontsize=14)
    plt.xlabel('size', fontsize=14)
    plt.ylabel('time', fontsize=14)
#     plt.xlim(100,10000)
#     plt.ylim(0,0.003)
    plt.grid(True)
    plt.show()
chart()