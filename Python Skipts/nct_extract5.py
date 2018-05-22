from __future__ import division
import h5py
import numpy as np
from numpy import matlib
import os
import glob
import collections
import mne
import scipy.io as sio


#datapath = '/vol/nct/data/Elim_BMBF/mat/tmp/'
#savepath = '/vol/nct/data/Elim_BMBF/npy/epochs/'

# PARAMETERS
srate = 2048
hi = .1
lo = 30
dwnfac = 0 # downsampling factor
samples = srate
doEpochs = False
saveNpy = True
doFilt = True


files = glob.glob(datapath+'VP*.mat')

for s in range(3, len(files)):
    # Extract v7.3 mat file with h5py and place items in dict
    
    # if ('VP1_' in files[s])|('VP5_' in files[s])|('VP9' in files[s])|('VP19' in files[s]):
    #     continue
    
    print "Processing file ", files[s]
    f = h5py.File(files[s])
    
    print "Extracting data... This will take a while. Please wait."
    # f can be used like a dictionary and has the following keys:
    # [u'#refs#', u'data', u'header', u'label', u'trigger']
    label = f['label'][...]
    trigger = f['trigger'][...]
    data = f['data'][...]


    # Re-reference EEG channels to refs (A1+A2)/2
    refs = data[32:34, :]
    data = data[:32, :]
    data = data-np.matlib.repmat(np.mean(refs, axis=0), 32, 1)

    # Band-pass filter data first, then downsample by factor 10
    if doFilt:
        print "Filtering...."
        srate = 2048
        data = mne.filter.filter_data(data,srate,l_freq=hi,h_freq=lo,n_jobs=6,method='iir')
    
    if doEpochs:
        print "Epoching..."
        label = label.flatten().astype(int)
        trigger = trigger.flatten().astype(int)
        epochs = np.zeros((label.shape[0],samples,32),dtype=np.float64)
        for i in range(trigger.shape[0]):
            epochs[i,:,:] = np.transpose(data[:,trigger[i]:trigger[i]+samples])

    if saveNpy:
        # np.save(files[s]+'_30Hz_epochs.npy',data)
        # np.save(files[s]+'_label.npy',label)
        # np.save(files[s]+'_trigger.npy',trigger)
        print "No saving..."

    if dwnfac > 0:
        print "Re-sampling..."
        data = np.transpose(mne.filter.resample(data,1,dwnfac,n_jobs='cuda')) 
        # # Adjust trigger to downsampling
        trigger = np.rint(trigger/dwnfac)
        srate = np.rint(srate/dwnfac)
        # # Save data
        print "Saving..."
        # sio.savemat(files[s]+"_band-pass30_dwn10.mat",{'data':data,'label':label,'trigger':trigger,'srate':srate})
        del data

print "Finished processing all files. Exiting."

