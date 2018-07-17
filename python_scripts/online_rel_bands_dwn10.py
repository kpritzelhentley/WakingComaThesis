import pdb
import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet
import glob
import scipy.io as sio

file = glob.glob('/vol/nct/data/Elim_BMBF/mat/dwn10/python/VP3_17.07_NM.bdf.mat_band-pass30_dwn10.mat')

print "Processing file "
struct = sio.loadmat(file[0])
data = struct['data']
data = data.transpose()
print("data shape: ", data.shape)

srate = struct['srate']
if type(srate)==np.ndarray:
    srate = srate[0][0]

# (name of stream, content type, channels, srate, channel format, source id)
info = StreamInfo('DoC', 'EEG', 32, srate, 'float32', 'DoC_ID')

# create outlet
outlet = StreamOutlet(info)

print 'sending data...'
# push out every sample individually
for i in range(data.shape[1]):
    outlet.push_sample(data[:32,i].tolist())
    # adjust sleep time to srate of 205
    time.sleep(0.005)
