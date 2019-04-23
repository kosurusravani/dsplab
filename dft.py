import numpy as np
from matplotlib import pyplot as plt
import cmath as c
N=input('enter the number for finding dft:')
x=input('enter the sequence:')
X=[]
j=c.sqrt(-1)
p=np.pi
for k in range(0,N,1):
	sum=0
	for n in range(0,N,1):
		sum=sum+x[n]*np.exp(-j*(2*p/N)*n*k)
	X.append(sum)
print(X)

