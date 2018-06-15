from pylsl import StreamInlet, resolve_stream
import ubicpy.sigproc as sigproc
import numpy as np

winsize = 1025 # 5 sec
overlap = 512 # 2.5 sec

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

# data = np.zeros(32, winsize + overlap * 2)
data = []

print("pull samples...")
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample = inlet.pull_sample()

    # build a list with all incoming channel columns
    data.append(sample[0])
    print data
