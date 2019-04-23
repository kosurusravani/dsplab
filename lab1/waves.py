import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
print(t)
c=np.pi
a=c/2 #phase shift
print(c)
x1=np.cos(2*c*t+a)
plt.subplot(1,3,1)
plt.plot(t,x1,'r')
plt.title("cosine funtion  ")
plt.xlabel("time")
plt.ylabel("amplitude")
x2=np.sin(2*c*t+a)
plt.subplot(1,3,2)
plt.plot(t,x2,'g')
plt.title("sine funtion  ")
plt.xlabel("time")
plt.ylabel("amplitude")
x3=x1*x2
plt.subplot(1,3,3)
plt.plot(t,x3,'black')
plt.title("sine funtion multiplication with cosine  ")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()