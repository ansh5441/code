from __future__ import division
import random
import math
from numpy import *

def res(f, x):
	k = ((x[2]-f[1])/(x[1]-f[0]))-((f[3]-f[1])/(f[2]-f[0]))

	if (k >= 0):
		return(1)
	else:
		return(-1)

def res2(w, x):
	k = (w[0] * x[0] + w[1] * x[1] + w[2] * x[2])
	if (k >= 0):
		return(1)
	else:
		return(-1)

def chooseRandom(arr):
	if (arr == []):
		return(-1)
	return(arr[int(math.floor(len(arr) * random.random()))])

def sign(x):
	if (x>=0):
		return (1)
	else:
		return(-1)

def w1():
	sum = 0
	num = 0
	c = 0
	iter = 500
	for i in range(1000):
		N = 10
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
		for j in range(100):
			x = [1, 2 * random.random() - 1, 2 * random.random() - 1]
			if (res2(w,x) == res(f,x)):
				c = c + 1
	print(sum/num)
	print(1 - c/100000)	

def w2_1():
	n1 = 0
	nmin = 0
	nran = 0
	for k in range(1000):
		coin = []
		heads = []
		for i in range(1000):
			toss = []	
			for j in range (10):
				toss.append(random.randrange(2))
			coin.append(toss)
			heads.append(sum(toss))
		n1 = n1 + heads[0]
		nmin = nmin + min(heads)
		nran =nran + chooseRandom(heads)
	print(n1/1000)
	print(nmin/1000)
	print(nran/1000)

def w2_2():
	numTrials = 1000
	N = 100
	tot = 0
	for i in range(numTrials):
		E = 0
		x = []
		y = []
		f = [2 * random.random() - 1, 2 * random.random() - 1, 2 * random.random() - 1, 2 * random.random() - 1]
		for j in range(N):
			x.append([1,2 * random.random() - 1, 2 * random.random() - 1])
			y.append(res(f,x[j]))
		x = matrix(x)
		y = matrix(y)
		w = (((((x.T)*x)).I)*(x.T))*(y.T)
		w = w.T*x.T
		for j in range(N):
			if(sign(w[0,j]) != y[0,j]):
				E = E+1
		tot = tot + (E/N)
		print(sign(w[0,j]),y[0,j])
		print()
	print(tot/numTrials)

def w2_3():
	numTrials = 100
	N = 1000
	tot = 0
	for _ in range (numTrials):
		x = []
		y = []
		E = 0
		for i in range(N):
			x1 = 2 * random.random() - 1
			x2 = 2 * random.random() - 1
			x.append([1,x1, x2, x1*x2, x1**2, x2**2])
			y.append(sign(x[i][1]**2 + x[i][2]**2 - 0.6))
			p = random.randint(1,10)
			if(p == 1):
				y[i] = -y[i]
		x = matrix(x)
		y = matrix(y)
		w = (((((x.T)*x)).I)*(x.T))*(y.T)
		w = w.T*x.T
		for j in range(N):
			if(sign(w[0,j]) != y[0,j]):
				E = E+1
		tot = tot + (E/N)

	print(tot/numTrials)
	print()
def w2_9():
	numTrials = 1000
	N = 1000
	tot = 0
	wtot = [0,0,0,0,0,0]
	for _ in range (numTrials):
		x = []
		y = []
		E = 0
		for i in range(N):
			x1 = 2 * random.random() - 1
			x2 = 2 * random.random() - 1
			x.append([1,x1, x2, x1*x2, x1**2, x2**2])
			y.append(sign(x[i][1]**2 + x[i][2]**2 - 0.6))
			p = random.randint(1,10)
			if(p == 1):
				y[i] = -y[i]
		x = matrix(x)
		y = matrix(y)
		w = (((((x.T)*x)).I)*(x.T))*(y.T)
		for i in range (6):
			wtot[i] = wtot[i] + w[i,0]
	for i in range (6):
		wtot[i] = wtot[i]/numTrials
	print(wtot)

def w2_10():
	numTrials = 100
	N = 1000
	tot = 0
	wtot = [0,0,0,0,0,0]
	for _ in range (numTrials):
		x = []
		y = []
		for i in range(N):
			x1 = 2 * random.random() - 1
			x2 = 2 * random.random() - 1
			x.append([1,x1, x2, x1*x2, x1**2, x2**2])
			y.append(sign(x[i][1]**2 + x[i][2]**2 - 0.6))
			p = random.randint(1,10)
			if(p == 1):
				y[i] = -y[i]
		x = matrix(x)
		y = matrix(y)
		w = (((((x.T)*x)).I)*(x.T))*(y.T)
		for i in range (6):
			wtot[i] = wtot[i] + w[i,0]
	for i in range (6):
		wtot[i] = wtot[i]/numTrials
	etot = 0
	for _ in range (numTrials):
		x = []
		y = []
		E = 0
		z = []
		for i in range(N):
			x1 = 2 * random.random() - 1
			x2 = 2 * random.random() - 1
			x.append([1,x1, x2, x1*x2, x1**2, x2**2])
			y.append(sign(x[i][1]**2 + x[i][2]**2 - 0.6))
			p = random.randint(1,10)
			if(p == 1):
				y[i] = -y[i]
			wtot = matrix(wtot)
			xx = matrix(x[i])
			z.append (sign(wtot * xx.T))
			if (y[i] != z[i]):
				E = E + 1
		etot = etot + E / N
	print(etot/numTrials)
def eu(u,v):
	return 2*(u*exp(v)-2*v*exp(-u))*(exp(v)+2*v*exp(-u))
def ev(u,v):
	return 2*(u*exp(v)-2*v*exp(-u))*(u*exp(v)-2*exp(-u))
def err5(u,v):
	return ((u*exp(v)-2*v*exp(-u))**2)
def w5_5():
	u = long(1.0)
	v = long(1.0)
	count = 0
	while err5(u,v) > 0.00000000000001:
		count = count+1
		du = 0.1 * eu(u,v)
		dv = 0.1 * ev(u,v)
		u = u - du
		v = v - dv
	print(count)
	print(u,v)

def w5_7():
	u = long(1.0)
	v = long(1.0)
	for i in range(15):
		du = 0.1 * eu(u,v)
		u = u - du
		dv = 0.1 * ev(u,v)
		v = v - dv
	print(err5(u,v))

def w5_8():
	errorre = 0
	
	for trial in range(100):
		#f = [2*random.random()-1,2*random.random()-1,2*random.random()-1,2*random.random()-1]
		f = [0.3,0.4,-8,-3]
		x = []
		y = []
		w = [0,0,0]
		for i in range(100):
			x.append([1,2*random.random()-1,2*random.random()-1])
			y.append(res(f,x[i]))
			e = (y[i]*matrix(x[i]))/(1+exp(y[i]*res2(w,x[i])))
			w[0] = w[0] - 0.01 * e[0,0]
			w[1] = w[1] - 0.01 * e[0,1]
			w[2] = w[2] - 0.01 * e[0,2]
		for i in range(1000):
			x.append([1,2*random.random()-1,2*random.random()-1])
			if (res(f,x[i]) == res2(w,x[i])):
				errorre = errorre + 1
	print(errorre/(100000))






if __name__ == '__main__':
	w5_8()
