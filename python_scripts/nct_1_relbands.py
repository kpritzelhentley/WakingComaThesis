from __future__ import division
import numpy as np
import scipy.io as sio
import glob
import ubicpy.sigproc as sigproc
import matplotlib.pyplot as plt
import os

datapath = '/vol/nct/data/Elim_BMBF/mat/dwn10/python/'

# os.chdir(datapath)
files = glob.glob(datapath+'VP*dwn10.mat')

winsize = 1025 # 5 sec
overlap = 512 # 2.5 sec
doPlot = True
doSave = False

pcount = np.zeros((len(files),5,32),dtype=np.int)
ncount = np.zeros((len(files),5,32),dtype=np.int)
pratio = np.zeros((len(files),5,32),dtype=np.float64)
nratio = np.zeros((len(files),5,32),dtype=np.float64)

for s in range(0,1):
    # if ('VP1_' in files[s])|('VP5_' in files[s])|('VP9' in files[s])|('VP19' in files[s]):
    #     continue

    print "Processing file ",files[s]
    struct = sio.loadmat(files[s])
    data = struct['data']
    # label = struct['label']
    # trigger = struct['trigger']
    srate = struct['srate']
    if type(srate)==np.ndarray:
        srate = srate[0][0]


    bandmat,t,f = sigproc.bandpower_relband(data,'all',srate,winsize,overlap)
    bandmeans = np.mean(bandmat,axis=2)
    bandstd = np.std(bandmat,axis=2)
    diffs = np.diff(bandmat,axis=2)
    diffdiffs = np.diff(diffs,axis=2)

    trigger = struct['trigger']
    label = struct['label']

    bandmat = np.swapaxes(bandmat,1,2)
    movband = sigproc.movavg(bandmat,winsize=10)
    bandmat = np.swapaxes(bandmat,1,2)

    if doSave:
        sio.savemat(files[s]+'_relbands.mat',{'bandmat':bandmat,'mvavg':movband,'t':t,'f':f,'winsize':winsize,'overlap':overlap})

    # samples = movband.shape[1]
    # for i in range(bandmeans.shape[0]):
    #     for j in range(32):
    #         pixs = np.nonzero(movband[i,:,j]>bandmeans[i,j]+bandstd[i,j])
    #         nixs = np.nonzero(movband[i,:,j]<bandmeans[i,j]-bandstd[i,j])
    #         pcount[s,i,j] = pixs[0].shape[0]
    #         ncount[s,i,j] = nixs[0].shape[0]
    #         pratio[s,i,j] = pixs[0].shape[0]/samples
    #         nratio[s,i,j] = nixs[0].shape[0]/samples

    # fig,ax = plt.subplots(2,figsize=(10,6))
    # l1,l2,l3,l4,l5 = ax[0].plot(np.transpose(pratio[s,:,:]))
    # ax[0].legend((l1,l2,l3,l4,l5),("delta","theta","alpha","beta1","beta2"))
    # ax[0].set_xlim(0,40)
    # ax[0].set_ylim(0,.25)
    # l1,l2,l3,l4,l5 = ax[1].plot(np.transpose(nratio[s,:,:]))
    # ax[1].legend((l1,l2,l3,l4,l5),("delta","theta","alpha","beta1","beta2"))
    # ax[1].set_xlim(0,40)
    # ax[1].set_ylim(0,.25)
    # plt.xlabel("Channel")

    # Optional Plotting
    if doPlot:
        plotmat = bandmat
        chan2plot = 31 # Cz
        #plt.ion()

        blist = ['delta','theta','alpha','beta1','beta2']

        dt = 1/srate
        diffts = np.ceil(np.mean(np.diff(t))/dt)+1
        vec = np.arange(0,data.shape[0],diffts) # sampling points corresponding to STFT windows onsets
        if vec.shape[0]>t.shape[0]:
            vec = vec[:-2]

        trigger = trigger.flatten()
        label = label.flatten()

        # groupnum = np.unique(label).shape[0]
        colorlist = plt.cm.viridis(np.linspace(0,1,5))
        mcolor = ['r','g','b','r','g','b','k','k'] # Marker colors

        fig,ax = plt.subplots(bandmeans.shape[0]) #groupnum,sharex=True)

        labellist = [1,2,3,4,5,6,8,9]
        paralist = ['P3-frequent','P3-rare','P3-novels','N4-start','N4-end','N4-nonsense','Eye-open','Eye-close']
        label2win = {}
        for i,group in enumerate(labellist): # Loop over all groups (aka label)
            ixs = label==group
            ixs = ixs.flatten()
            currtrigg = trigger[ixs]
            nearestval = np.zeros((currtrigg.shape[0],))
            nearestix = np.zeros((currtrigg.shape[0],))
            for l in range(currtrigg.shape[0]): # Loop over all triggers in group
                diff = np.repeat(currtrigg[l],vec.shape[0],axis=0) - vec
                pos = diff>=0
                diff = diff[pos] # Keep only positive values
                nearestval[l] = np.min(diff)
                nearestix[l] = np.argmin(diff) # Index of window trigger belongs in

            label2win[paralist[i]] = nearestix.astype(int)
            # nearestix = nearestix.astype(int)


        for p in range(bandmeans.shape[0]):
            l1, = ax[p].plot(t/60.0,plotmat[p,chan2plot,],color=colorlist[p,]) #),linewidth=2)

            lavg, = ax[p].plot(t/60,movband[p,:,chan2plot],color='r',linewidth=2)
            l2 = ax[p].axhline(y=bandmeans[p,chan2plot],color='k')
            l3 = ax[p].axhline(y=bandmeans[p,chan2plot]+bandstd[p,chan2plot],color='g')
            l4 = ax[p].axhline(y=bandmeans[p,chan2plot]-bandstd[p,chan2plot],color='g')

            if p==bandmeans.shape[0]-1: # P300
                for i in range(3):
                    dummy = label2win[paralist[i]]
                    ax[p].plot(t[dummy]/60.0,np.repeat(np.max(plotmat[p,chan2plot,])+.1,dummy.shape[0],axis=0),\
                            linestyle='None',marker='*',color=mcolor[i],markeredgecolor=mcolor[i])

            if p==bandmeans.shape[0]-2: # N400
                for i in range(3,6):
                    dummy = label2win[paralist[i]]
                    ax[p].plot(t[dummy]/60.0,np.repeat(np.max(plotmat[p,chan2plot,])+.1,dummy.shape[0],axis=0),\
                            linestyle='None',marker='*',color=mcolor[i],markeredgecolor=mcolor[i])

            ax[p].set_ylim(0,np.max(plotmat[p,chan2plot,])+.2)
            # ax[p].set_xlim(0,t[699]/60)
            # ax[p].xaxis.set_ticks(np.arange(0,80,5))
            ax[p].grid()
            ax[p].legend((l1,lavg,l2,l3),(blist[p],'movavg','mean','stdev'))
            # ax.yaxis.set_ticks(np.arange(0,1.5,.5))

        plt.xlabel('Time [min]')
        plt.show()


        # ax.legend((l1,l2,l3,l4,l5),('delta','theta','alpha','beta1','beta2'))
        # plt.title(files[s])
