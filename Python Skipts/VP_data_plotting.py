from __future__ import division
import h5py
import numpy as np
from numpy import matlib
import os
import glob
import collections
import mne
import scipy.io as sio
import matplotlib
import matplotlib.pyplot as plt


# EEG data with srate of 1/2048
data = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_data.npy')
# Array with beginning of events timestamps
trigger = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_trigger.npy')
# 
labels = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_label.npy')

time = np.arange(0, data.shape[1])
trig_time = np.arange(0, trigger.shape[1])


# for i in range(data.shape[0]):
# 	plt.plot(x, data[i])

plt.plot(time, data[1])
plt.plot(trig_time, trigger[0])
plt.show()


