import numpy as np
from numpy import matlib
import matplotlib
import matplotlib.pyplot as plt
import mne

srate = 2048
# EEG data with srate of 1/2048. Load onto disk with mmap_mode set to 'r' for read only
data = np.load('/vol/nct/data/Elim_BMBF/npy/VP1_10.07_NM.bdf.mat_data.npy', 'r+')
# Array with beginning of events timestamps
trigger = np.load('/vol/nct/data/Elim_BMBF/npy/VP1_10.07_NM.bdf.mat_trigger.npy')
trigger = trigger.ravel()
# labels for each trigger:
# 1:Haeufiger Ton, 2:seltener Ton, 3:Novels, 4:Satzanfaenge, 5:Sinnvolle Satzenden, 6:Sinnlose Satzenden
labels = np.load('/vol/nct/data/Elim_BMBF/npy/VP1_10.07_NM.bdf.mat_label.npy')
labels = labels.ravel()

print "Filtering...."
hi = .1
lo = 30
filt_data = mne.filter.filter_data(data,srate,l_freq=hi,h_freq=lo,n_jobs=6,method='iir')

## extract data segments for novel triggers
# using 'flatnonzero' instead of 'where' to have 1d array (not a one-element-tuple) as output
novels_idx = np.flatnonzero(labels == 3)
# array with averaged p300 segements for each channel
p300_sgmts = np.empty([novels_idx.size, srate])
p300_mean = np.empty([data.shape[0], srate])

print('Collecting data segments for novels....')
for k in range (data.shape[0]):
    for i in range(novels_idx.size):
        # labels and trigger have the same size, therefore the novels_idxs can be used
        # as trigger idxs
        trig_idx = novels_idx[i]
        novel_begin_idx = int(trigger[trig_idx])
        novel_end_idx = int(trigger[trig_idx]+srate)
        # take the first row of data (channel 1) and get the trigger timestamps
        # at the novels_idxs. One segment should be about one second long (from one
        # trigger to the next)
        p300_sgmts[i][:] = data[k][novel_begin_idx:novel_end_idx]
    # calculate mean of all segments in one channel (mean of numbers over all rows)
    p300_mean[k][:] = np.mean(p300_sgmts, axis=0)


# plot segments for each channel
print('Plotting and saving data segments....')
for i in range (data.shape[0]):
    plt.figure()
    time = np.arange(srate)
    plt.plot(time, p300_mean[i])
    # plot vertical line a 300ms (0.3 * 2048 = 614)
    plt.axvline(x=614, color='r')
    plt.savefig('p300_data/p300_channel_' + str(i+1))
    plt.close(fig) # or use plt.close('all') to close all open figures

del data
