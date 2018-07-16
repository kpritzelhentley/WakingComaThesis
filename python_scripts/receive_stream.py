from pylsl import StreamInlet, resolve_stream
import ubicpy.sigproc as sigproc
import numpy as np
import pdb

# 1 min of data (srate * 60 sec), this is the window on which the band
# frewuencies are calculated on
winsize = 12300
overlap = 410 # 2 sec
srate = 205

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

data = []
bandlist = []

print("pull samples...")
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample = inlet.pull_sample()

    if len(data)%1000 == 0:
        print("new 1000 samples...")

    # build a list with all incoming channel columns
    data.append(sample[0])

    # Wait until the window is large enough to calculate good bandmat
    if len(data) == winsize:
        arr = np.array(data)
        # data was a list of rows and each row contained the nect sample for
        # ech channel. Through transpose the array now contains rows which contain
        # all the smaples of one channel. Therefore 32 ros each with 'viewsize'
        # amount of samples.
        print("arr shape: ", arr.shape)
        bandmat,t,f = sigproc.bandpower_relband(arr, 'all', srate, 600, overlap=300, doPow=True)
        print ("bandmat shape: ", bandmat.shape)
        bandlist.append(bandmat)
        print bandmat

        # delete first 2 seconds of incoming data
        del data[0:overlap]
