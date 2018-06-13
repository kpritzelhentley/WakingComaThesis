from __future__ import division
import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet
from pylsl import StreamInlet, resolve_stream


print "loading data..."
data = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_data.npy')

# give information about the stream
# (name of stream, content type, channels, srate, channel format, source id)
info = StreamInfo('EEG', 'EEG', 32, 2048, 'float32', '')

# create outlet
outlet = StreamOutlet(info)

print 'sending data...'
# push out every sample individually
for i in range(10):
    outlet.push_sample(data[:,i])
    time.sleep(0.01)

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream(info)

# create a new inlet to read from the stream
print("creating inlet...")
inlet = StreamInlet(streams[0])

print("pushing samples...")
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample = inlet.pull_sample()
    print(sample)
