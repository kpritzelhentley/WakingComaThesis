import numpy as np
from numpy import matlib
import matplotlib
import matplotlib.pyplot as plt

# EEG data with srate of 1/2048
data = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_data.npy')
# Array with beginning of events timestamps
trigger = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_trigger.npy')
trigger = trigger.ravel()
# labels for each trigger:
# 1:Haeufiger Ton, 2:seltener Ton, 3:Novels, 4:Satzanfaenge, 5:Sinnvolle Satzenden, 6:Sinnlose Satzenden
labels = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_label.npy')
labels = labels.ravel()

## extract data segments for novel triggers
# using 'flatnonzero' instead of 'where' to have 1d array (not a one-element-tuple) as output
novels_idx = np.flatnonzero(labels == 3)
# this list will be filled with arrays which represent the wanted data segments
p300_sgmts = []

# calculate average of all data channels
data_sum = np.empty(data.shape[1])
for i in range(data.shape[0]):
    data_sum += data[i]
# divide the sum by number of channels
data_avg = data_sum / data.shape[0]

print('collecting data segments for novels...')
for i in range(novels_idx.size):
    # labels and trigger have the same size, therefore the novels_idxs can be used
    # as trigger idxs
    trig_idx = novels_idx[i]
    # take the first row of data (channel 1) and get the trigger timestamps
    # at the novels_idxs. One segment should be about one second long (from one
    # trigger to the next)
    p300_sgmts.append(data_avg[trigger[trig_idx]:trigger[trig_idx+1]])

# plot all segments in subplots
print('plotting and saving data segments...')
for i in range (len(p300_sgmts)):
    plt.figure()
    time = np.arange(p300_sgmts[i].size)
    plt.plot(time, p300_sgmts[i])
    # plot vertical line a 300ms (0.3 * 2048 = 614)
    plt.axvline(x=614, color='r')
    plt.savefig('p300_data/p300_sgmt_' + str(i))
