import matplotlib.pyplot as plt
from matplotlib import gridspec

def plot_data(avg_rel_track, sd_rel_track_sum, sd_index, sd_grad):

    fig = plt.figure(figsize=(15,10))
    gs  = gridspec.GridSpec(4, 1, height_ratios=[1, 1 ,1.5, 1])
    ax0 = plt.subplot(gs[0])
    ax1 = plt.subplot(gs[1])
    ax2 = plt.subplot(gs[2])
    ax3 = plt.subplot(gs[3])

    fig.subplots_adjust(top=0.85)
    lineObjects = ax0.plot(avg_rel_track_nan)

    if len(sd_index)>1:
        for i in xrange(1, len(sd_index)):
            if sd_grad[i]==1:
                ax0.axvspan(sd_index[i-1], sd_index[i],
                            edgecolor='#FFCC66', facecolor='#FFCC66',
                            alpha=1)

    #The following plot has 5 plots within it.
    ax0.set_title('Averaged Relative Track',fontsize=11)
    ax0.legend(lineObjects, (1,2,3,4,5))

    ax1.plot(sd_rel_track_sum)
    ax1.set_title('RT Standard Deviation',fontsize=11)
    ax1.set_ylim([0,250])

    ax2.plot(splitpre)
    ax2.set_title('Track Split',fontsize=11)

    ax3.plot(ts_sd)
    ax3.set_title('Track Split Standard Dev',fontsize=11)
    ax3.set_ylim([0,100])

    fig.tight_layout()
    plt.show()
