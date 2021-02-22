import numpy as np
from scipy.io import wavfile

v_rate, v_data = wavfile.read('thermo.wav')
b_rate, b_data = wavfile.read('woman.wav')

print('voice and backgroud (rate, shape):',v_rate, v_data.shape,b_rate, b_data.shape)

if(len(v_data.shape)!=len(b_data.shape)): # if number of channel is not matched
# Unify to mono channel by taking mean between Left and Right Channel
    if(len(v_data.shape)>1):                            # if it is stereo
        v_data=np.array((v_data[:,0]+v_data[:,1])/2)    # Mean
    if(len(b_data.shape)>1):                            # if it is stereo
        b_data=np.array((b_data[:,0]+b_data[:,1])/2)    # Mean

# Down-Sampling
if (v_rate > b_rate) :
   diffRate = v_rate // b_rate                          # get diff Multiple rate
   v_data = np.array(v_data[0:len(v_data):diffRate])    # skip to match sample rate
   rate = b_rate                                        # dst sample rate
elif (v_rate < b_rate) : 
   diffRate = b_rate // v_rate
   b_data = np.array(b_data[0:len(b_data):diffRate])
   rate = v_rate
else :
   rate = b_rate
   
print('voice and backgroud (rate, shape):',v_rate, v_data.shape,b_rate, b_data.shape)

# Normalize before processing
v_data = np.array(v_data/np.max(np.abs(v_data))) # normalize in range of [-1:1]
b_data = np.array(b_data/np.max(np.abs(b_data))) # normalize in range of [-1:1]

# Insert and mix voice in background at 3 sec.
b_data[rate*3:rate*3+len(v_data)] *= 0.3
b_data[rate*3:rate*3+len(v_data)] += 0.7*v_data

# Restore to 16bit wavfile (signed int16)
scaled = np.int16(b_data/np.max(np.abs(b_data)) * 32767)
wavfile.write('mixed.wav', rate, scaled)
