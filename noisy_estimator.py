import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

N_trials = np.logspace(0,4,100,dtype=int)
N_trials = np.unique(N_trials)
size_grid = [5,5]
N_images = 5
idx_images = np.round(np.linspace(0,N_trials.shape[0]-1,5)).astype(int)
n_images = N_trials[idx_images]
images = []

variance = []
experiments = np.random.rand(size_grid[0],size_grid[1],N_trials[-1]) >= 0.5
for n in N_trials:
    start = 0
    stop = n
    var = 0
    for k in range(N_trials[-1]//n):
        group = experiments[:,:,start:stop]
        var += np.var(group)
        start = stop
        stop += n
    variance.append( np.mean(var) )

    if n in n_images:
        img = np.mean(group,axis=2)
        images.append(img)

fig0,ax0 = plt.subplots(1,N_images)
for j in range(N_images):
    mappable = ax0[j].imshow(images[j],cmap='gray',vmin=0,vmax=1)
    ax0[j].set_xticks([])
    ax0[j].set_yticks([])

fig1,ax1 = plt.subplots(1,1,figsize=(10,5))
ax1.semilogx(N_trials,variance)
ax1.plot([N_trials[0],N_trials[-1]],[0,0],'--',linewidth=0.75,color='gray')
ax1.set_ylabel('Variance (Image Noise)')
ax1.set_xlabel('Number of Trials (Exposure Time)')
ax1.set_xticks([N_trials[0],N_trials[-1]])
ax1.set_yticks([0])
plt.minorticks_off()

fig0.show()
fig1.show()
