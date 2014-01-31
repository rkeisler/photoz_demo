import matplotlib.pylab as pl
import numpy as np

def plot_photodata(d):
    n2pl=10000; s=5; cmap=pl.cm.RdBu_r; fs=14;
    colors = np.log((d.redshift)[0:n2pl])
    pl.figure(figsize=(10,4))
    pl.subplot(1,2,1)
    pl.scatter((d.g-d.r)[0:n2pl], (d.i)[0:n2pl], 
               c=colors, s=s, cmap=cmap, edgecolors='none')
    pl.xlim(-0.5,2)
    pl.ylim(12,20)
    pl.xlabel('Color [g-r]',fontsize=fs)
    pl.ylabel('Magnitude [i]',fontsize=fs)
    pl.subplot(1,2,2)
    pl.scatter((d.r-d.i)[0:n2pl], (d.i-d.z)[0:n2pl], 
        c=colors, s=s, cmap=cmap, edgecolors='none')
    pl.xlim(-0.2,1.0)
    pl.ylim(-.2, .8)
    pl.xlabel('Color [r-i]',fontsize=fs)
    pl.ylabel('Color [i-z]',fontsize=fs)
    pl.colorbar()
