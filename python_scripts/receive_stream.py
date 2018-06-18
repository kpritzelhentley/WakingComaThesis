from pylsl import StreamInlet, resolve_stream
import ubicpy.sigproc as sigproc
import numpy as np
import pdb

winsize = 1025 # 5 sec
overlap = 512 # 2.5 sec
viewsize = winsize + overlap*2
srate = 205

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

    #pdb.set_trace()

    # build a list with all incoming channel columns
    data.append(sample[0])
    print data
    # check if number of samples of one channel is larger than viewsize
    if len(data[0]) > viewsize:
        data.pop(0)
        arr = np.array(data)

        # data was a list of rows and each row contained the nect sample for
        # ech channel. Through transpose the array now contains rows which contain
        # all the smaples of one channel. Therefore 32 rows each with 'viewsize'
        # amount of samples.
        arr.transpose()
        bandmat,t,f = sigproc.bandpower_relband(arr,'all',srate,winsize,overlap)
        print bandmat
