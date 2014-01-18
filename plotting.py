import matplotlib.pylab as pl

def plot_photodata(d):
    n2pl=1e4; s=5; cmap=pl.cm.jet; fs=14;
    pl.figure(figsize=(10,4))
    pl.subplot(1,2,1)
    pl.scatter((d.g-d.r)[0:n2pl], (d.i)[0:n2pl], 
               c=(d.redshift)[0:n2pl], s=s, cmap=cmap, edgecolors='none')
    pl.xlim(-0.5,2)
    pl.ylim(13,21)
    pl.xlabel('Color [g-r]',fontsize=fs)
    pl.ylabel('Magnitude [i]',fontsize=fs)
    pl.subplot(1,2,2)
    pl.scatter((d.r-d.i)[0:n2pl], (d.i-d.z)[0:n2pl], 
        c=(d.redshift)[0:n2pl], s=s, cmap=cmap, edgecolors='none')
    pl.xlim(-0.1,1.1)
    pl.ylim(-.2, .8)
    pl.xlabel('Color [r-i]',fontsize=fs)
    pl.ylabel('Color [i-z]',fontsize=fs)
    pl.colorbar()
