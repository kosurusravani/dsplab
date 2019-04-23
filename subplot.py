import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs1,d8k=wav.read('myvoice1.wav')
print(fs1,len(d8k))
print(d8k) #values of samples
t1=np.arange(0,len(d8k)/fs1,1.0/fs1) #time scale
plt.subplot(2,1,1)
plt.title('voice signal for low sampling frequency ')
plt.plot(d8k)
fs2,d16k=wav.read('myvoice2.wav')
print(fs2,len(d16k))
print(d16k)
t2=np.arange(0,len(d16k)/fs2,1.0/fs2) #time scale
plt.subplot(2,1,2)
plt.title('voice signal for high sampling frequency')
plt.plot(d16k)
plt.show()
