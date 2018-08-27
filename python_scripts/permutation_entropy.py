import numpy as np
from numpy import matlib
import collections
import scipy.io as sio
from scipy import signal
import matplotlib
import matplotlib.pyplot as plt
import mne
import glob
import ubicpy.sigproc as sigproc
from pyentrp import entropy as ent

datapath = '/vol/nct/data/Elim_BMBF/mat/dwn10/python/'

# os.chdir(datapath)
files = glob.glob(datapath+'VP*dwn10.mat')

winsize = 1025 # 5 sec
overlap = 512 # 2.5 sec
doPlot = True
doSave = False

for s in range(1):

    print "Processing file ",files[s]
    struct = sio.loadmat(files[s])
    data = struct['data']
    print("data shape: ", data.shape)
    # label = struct['label']
    # trigger = struct['trigger']
    srate = struct['srate']
    if type(srate)==np.ndarray:
        srate = srate[0][0]

    bandmat,t,f = sigproc.bandpower_relband(data,'all',srate,winsize,overlap)
    print "data: ", data.shape

    #for i in range(int(data.shape[0]/winsize)):
    # Calculate Permutation Entropy (a type of complexity measurement) for the theta band
    perm_entropy = np.empty((32, ))
    for channel in range(32):
        perm_entropy[channel] = ent.permutation_entropy(bandmat[1][channel], 3, 1)
        print "perm_entropy for channel" + str(channel+1), perm_entropy[channel]
