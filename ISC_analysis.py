def ISC_analysis( filename ):
    import h5py, numpy as np, nibabel as nib 
    from scipy.stats.stats import pearsonr

    print('loading subject data...')
    f = h5py.File(filename)
    data = f['subj_data']
    cond = np.array(data)

    print('computing ISC...')

    store_corr = np.zeros([cond.shape[2],cond.shape[0]])

    for i in np.arange(len(data)):
	    cond_mean = np.mean(cond[np.arange(len(data)) !=i,:,:],axis=0)
	    leftout = cond[i,:,:]
	    for j in range(len(store_corr)):
		    r,p = pearsonr(cond_mean[:,j],leftout[:,j])
		    store_corr[j,i] = r

    ISC_brain = np.nanmean(store_corr,axis=1)
    data_map = np.reshape(ISC_brain,(91,109,91))


