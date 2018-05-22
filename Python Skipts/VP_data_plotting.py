import numpy as np
from numpy import matlib
import collections
import scipy.io as sio
import matplotlib
import matplotlib.pyplot as plt


# EEG data with srate of 1/2048
data = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_data.npy')
# Array with beginning of events timestamps
trigger = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_trigger.npy')
# labels for each trigger: 
# 1:Haeufiger Ton, 2:seltener Ton, 3:Novels, 4:Satzanfaenge, 5:Sinnvolle Satzenden, 6:Sinnlose Satzenden
labels = np.load('/vol/nct/data/Elim_BMBF/npy/VP07_17.07_VM.bdf.mat_label.npy') * 500

time = np.arange(0, data.shape[1])
trig_height = np.ones_like(trigger) * 400

# for i in range(data.shape[0]):
# 	plt.plot(x, data[i])

print 'plotting...'
plt.plot(time, data[1])
plt.plot(trigger, trig_height, 'ro')
plt.plot(trigger, labels, 'bo')
plt.show()


