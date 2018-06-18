from pylsl import StreamInlet, resolve_stream
import ubicpy.sigproc as sigproc
import numpy as np
import pdb

# 1 min of data (srate * 60 sec), this is the window on which the band
# frewuencies are calculated on
winsize = 12300
overlap = 512 # 2.5 sec
srate = 205

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

# data = np.zeros(32, winsize + overlap * 2)
data = []
# The counter tracks how many new samples have been added to the data list
counter = 0
bandlist = []

print("pull samples...")
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample = inlet.pull_sample()

    # build a list with all incoming channel columns
    data.append(sample[0])
    counter += 1

    # check if 410 (2 sec) new sample arrays have been added to data
    if counter == 410:
        if len(data) >= winsize + counter:
            # delete first 2 seconds of incoming data
            del data[0:counter]
        arr = np.array(data)

        # data was a list of rows and each row contained the nect sample for
        # ech channel. Through transpose the array now contains rows which contain
        # all the smaples of one channel. Therefore 32 rows each with 'viewsize'
        # amount of samples.
        arr.transpose()
        bandmat,t,f = sigproc.bandpower_relband(arr, 'all', srate, arr.shape[0], overlap=0, doPow=True)
        bandlist.append(bandmat)
        print bandmat
