import pdb
import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet

print "loading data..."
data = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_data.npy')

# first create a new stream info (here we set the name to BioSemi,
# the content-type to EEG, 8 channels, 100 Hz, and float-valued data) The
# last value would be the serial number of the device or some other more or
# less locally unique identifier for the stream as far as available (you
# could also omit it but interrupted connections wouldn't auto-recover)

# (name of stream, content type, channels, srate, channel format, source id)
info = StreamInfo('DoC', 'EEG', 32, 2048, 'float32', 'DoC_ID')

# create outlet
outlet = StreamOutlet(info)

print 'sending data...'
# push out every sample individually
for i in range(data.shape[1]):
    outlet.push_sample(data[:32,i].tolist())
    # adjust sleep time to srate of 2048
    time.sleep(0.002)
