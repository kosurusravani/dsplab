import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs1,d16k=wav.read('myvoice2.wav')
print(fs1,len(d16k))
print(d16k) #values of samples
t=np.arange(0,len(d16k)/fs1,1.0/fs1) #time scale
plt.plot(d16k)
plt.show()
#wav.write('slow.wav',fs1*0.5,d16k)
wav.write('fast.wav',fs1*2,d16k)