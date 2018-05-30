import numpy as np
from numpy import matlib
import matplotlib
import matplotlib.pyplot as plt

srate = 2048
# EEG data with srate of 1/2048
data = np.load('/vol/nct/data/Elim_BMBF/npy/VP1_10.07_NM.bdf.mat_data.npy')
# Array with beginning of events timestamps
trigger = np.load('/vol/nct/data/Elim_BMBF/npy/VP1_10.07_NM.bdf.mat_trigger.npy')
trigger = trigger.ravel()
# labels for each trigger:
# 1:Haeufiger Ton, 2:seltener Ton, 3:Novels, 4:Satzanfaenge, 5:Sinnvolle Satzenden, 6:Sinnlose Satzenden
labels = np.load('/vol/nct/data/Elim_BMBF/npy/VP1_10.07_NM.bdf.mat_label.npy')
labels = labels.ravel()

## extract data segments for novel triggers
# using 'flatnonzero' instead of 'where' to have 1d array (not a one-element-tuple) as output
novels_idx = np.flatnonzero(labels == 3)
# array with averaged p300 segements for each channel
p300_sgmts = np.empty_like([data.shape[0], novels_idx.size])

print('collecting data segments for novels...')
for k in range (data.shape[0]):
    for i in range(novels_idx.size):
        # labels and trigger have the same size, therefore the novels_idxs can be used
        # as trigger idxs
        trig_idx = novels_idx[k]
        # take the first row of data (channel 1) and get the trigger timestamps
        # at the novels_idxs. One segment should be about one second long (from one
        # trigger to the next)
        p300_sgmts[k][i] = data[k][trigger[trig_idx]:trigger[trig_idx]+srate]
    # calculate mean of all segments in one channel (mean of numbers inside a row)
    p300_mean = np.mean(p300_sgmts, axis=1)


# plot all segments in subplots
print('plotting and saving data segments...')
for i in range (len(p300_sgmts)):
    plt.figure()
    time = np.arange(p300_sgmts[i].size)
    plt.plot(time, p300_sgmts[i])
    # plot vertical line a 300ms (0.3 * 2048 = 614)
    plt.axvline(x=614, color='r')
    plt.savefig('p300_data/p300_sgmt_' + str(i))
