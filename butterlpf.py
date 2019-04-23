import numpy as np
from matplotlib import pyplot as plt
import cmath as c1
T=0.1
p=0.35*np.pi
c=0.7*np.pi
def frequency(p,c):	
	a=((2.0/T)*np.tan(p/2.0))	
	b=((2.0/T)*np.tan(c/2.0))
	return a,b
t=frequency(p,c)
a=t[0]
print "analog pass band edge fre=", a
b=t[1]
print "analog stop band edge fre=", b






#order
sp=0.6
ss=0.1
h=ss**2
i=sp**2
def order(h,i,a,b):
	x1=((1.0/h)-1.0)
	x2=((1.0/i)-1.0)
	q=(x1/x2)
	k=((1.0/2.0)*np.log(q))
	n=np.log(a/b)
	N=(k/n)
	return N
y=order (h,i,a,b)
print y
m=np.abs(y)
n1=np.ceil(m)
print "order=",n1



#cutt off frequency
ss=0.1
def cutof(n1,ss,b):
	a1=((1.0/ss**2)-1.0)
	a2=(1/(2.0*n1))
	a3=(a1)**a2
	f=(b/a3)
	return f
e=cutof(n1,ss,b)
print "cutt of frequency=",e	


#trasfer function

def trans(e,T,n1):
	bk=2*np.sin((np.pi)/4.0)
	j=c1.sqrt(-1)
	w=np.arange(0,np.pi,0.01)
	z=np.exp(j*w)
	s=((2.0/T)*((1-(1/z))/(1+(1/z))))
	p1=((s**2)+(bk*e*s)+(e**2))
	p2=e**n1
	hs=(p2/p1)
	return hs
h1=trans(e,T,n1)
print"transfer function=",h1
w=np.arange(0,np.pi,0.01)
plt.plot(w,np.abs(h1))
plt.show()














