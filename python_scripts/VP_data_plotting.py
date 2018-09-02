import numpy as np
from numpy import matlib
import collections
import scipy.io as sio
from scipy import signal
import matplotlib
import matplotlib.pyplot as plt
import mne
import ubicpy.sigproc as sigproc

doPlot = False
doFilt = True
doSpectro = False
doDownSmpl= True

srate = int(2048/10)
winsize = srate * 60 # don't go lower than 10 sek windows
overlap = winsize/10

# EEG data with srate of 1/2048
print "Loading Data..."
data = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_data.npy')
# Array with beginning of events timestamps
trigger = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_trigger.npy')
# labels for each trigger:
# 1:Haeufiger Ton, 2:seltener Ton, 3:Novels, 4:Satzanfaenge, 5:Sinnvolle Satzenden, 6:Sinnlose Satzenden
labels = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_label.npy') * 500

time = np.arange(0, data.shape[1] / 2048 / 60)
trig_height = np.ones_like(trigger) * 200

if doFilt:
    print "Filtering...."
    srate = 2048
    hi = .1
    lo = 30
    data = mne.filter.filter_data(data,srate,l_freq=hi,h_freq=lo,n_jobs=6,method='iir')

if doDownSmpl:
    data = data[::,::10]

if relBandPlot:
    data = data.transpose()
    relband, t, f = sigproc.bandpower_relband(arr, 'all', srate, winsize, overlap, doPow=True)
    bandmeans = np.mean(relband,axis=2)
    bandstd = np.std(relband,axis=2)

    plt.xlabel('Time')
    plt.ylabel('Micro Volts')
    plt.title('Data Section with Mean and Standard Deviation')

    plt.plot(time, data[1, 400:4000])

    plt.savefig('relband mean and std')

if doPlot:
    print 'Plotting...'
    for i in range(3):
        fig = plt.figure(figsize=(40.0, 10.0)) # figsize in inches
        ax = fig.add_subplot(1,1,1)
        plt.plot(time, data[i])
        plt.plot(trigger, trig_height, 'ro')

        plt.xlabel('Time in Minutes')
        plt.ylabel('Micro Volts')
        plt.title('EEG Channel ' + str(i+1))

        # set the distance between ticks on the x-axis
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.arange(start, end, 500000))
        plt.ylim = 300
        # plt.plot(trigger, labels, 'bo')
        plt.savefig('channel_plots/channel_' + str(i+1))
        plt.close(fig) # or use plt.close('all') to close all open figures

if doSpectro:
    print 'Spectrogram...'
    for i in range(2):
        f, t, Sxx = signal.spectrogram(data[i], 2048, nperseg=2048)
        plt.pcolormesh(t, f, Sxx)
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.ylim(ymax = 30)
        plt.savefig('channel_plots/spectro_channel_' + str(i+1))

del data
print "Finished processing all files. Exiting."
