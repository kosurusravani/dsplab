import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
print(t)
c=np.pi
a=c/2 #phase shift
print(c)
x1=np.cos(2*c*t+a)
y1=x1*x1
plt.subplot(1,3,1)
plt.plot(t,y1,'r')
plt.title("squareofcosine funtion  ")
plt.xlabel("time")
plt.ylabel("amplitude")
x2=np.sin(2*c*t+a)
y2=x2*x2
plt.subplot(1,3,2)
plt.plot(t,y2,'g')
plt.title("square of sine funtion  ")
plt.xlabel("time")
plt.ylabel("amplitude")
x3=y1*y2
plt.subplot(1,3,3)
plt.plot(t,x3,'black')
plt.title("sine funtion multiplication with cosine  ")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()