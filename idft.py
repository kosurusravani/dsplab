import numpy as np
from matplotlib import pyplot as plt
import cmath as c
N=input('enter the number for finding idft:')
X=input('enter the sequence:')
x=[]
j=c.sqrt(-1)
p=np.pi
for n in range(0,N,1):
	sum=0
	for k in range(0,N,1):
		sum=sum+X[k]*np.exp(j*(2*p/N)*n*k)
	x.append(sum/N)
print(x)

