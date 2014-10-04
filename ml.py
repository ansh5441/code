from __future__ import division
import random
import math

def res(f, x):
	k = ((x[2]-f[1])/(x[1]-f[0]))-((f[3]-f[1])/(f[2]-f[0]))
	if (k>0):
		return(1)
	else:
		return(-1)

def res2(w, x):
	k = (w[0] * x[0] + w[1] * x[1] + w[2] * x[2])
	if (k>0):
		return(1)
	else:
		return(-1)

def chooseRandom(arr):
	if (arr == []):
		return(-1)
	return(arr[int(math.floor(len(arr) * random.random()))])


def w1():
	sum = 0
	num = 0
	c = 0
	iter = 500
	for i in range(400):
		N = 100
		f = [2 * random.random() - 1, 2 * random.random() - 1, 2 * random.random() - 1, 2 * random.random() - 1]
		x = []
		y = []
		y1 = []
		err = []
		w = [0,0,0]
		w1 = [(f[0]*f[3]-f[1]*f[2]), f[3]-f[1], f[2]-f[0]]
		for j in range(N):
			x.append([1, 2 * random.random() - 1, 2 * random.random() - 1])
			y.append(res(f, x[j]))
			y1.append(res2(w,x[j]))
			if (y[j] != y1[j]):
				err.append(j)
		count = 0
		
		while(err != [] and count <iter):
		#for djfj in range(10):
			count = count + 1
			error = chooseRandom(err)
			
			for j in range (3):
				w[j] = w[j] + y[error] * x[error][j]
			err = []
			y1=[]
			
			for j in range(N):
				y1.append(res2(w,x[j]))
				if (y[j] != y1[j]):
					err.append(j)
		if (count != iter):
			sum = sum + count
			num = num + 1
		
		for i in range(100):
			x = [1, 2 * random.random() - 1, 2 * random.random() - 1]
			if (res2(w,x) == res(f,x)):
				c = c + 1
	print(c/100000)
	print(sum)
	print(num)
	print(sum/num)
	





if __name__ == '__main__':
	w1()
