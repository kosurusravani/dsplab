import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs1,d8k=wav.read('myvoice1.wav')
print(fs1,len(d8k))
print(d8k) #values of samples
t=np.arange(0,len(d8k)/fs1,1.0/fs1) #time scale
plt.plot(d8k)
plt.show()
#wav.write('slow.wav',fs1*0.5,d8k)
wav.write('fast.wav',fs1*2,d8k)