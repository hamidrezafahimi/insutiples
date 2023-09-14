import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 = cv2.imread("img_.png")
img2 = cv2.imread("binImg.png")
img3 = cv2.imread("flow.png")
img4 = cv2.imread("depthMap.png")
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)


# Fixing random state for reproducibility
np.random.seed(19680801)

cmap_rev = plt.cm.get_cmap('jet_r')

ax1 = plt.subplot(221)
plt.imshow(img1, cmap=cmap_rev)
plt.axis('off')
plt.text(0.5,-0.1, "(a)", size=12, ha="center",
         transform=ax1.transAxes)

ax2 = plt.subplot(222)
plt.imshow(img3, cmap=cmap_rev)
plt.axis('off')
plt.text(0.5,-0.1, "(b)", size=12, ha="center",
         transform=ax2.transAxes)

ax3 = plt.subplot(223)
plt.imshow(img4, cmap=cmap_rev)
plt.axis('off')
plt.text(0.5,-0.1, "(c)", size=12, ha="center",
         transform=ax3.transAxes)

ax4 = plt.subplot(224)
plt.imshow(img2, cmap=cmap_rev)
plt.axis('off')
plt.text(0.5,-0.1, "(d)", size=12, ha="center",
         transform=ax4.transAxes)


plt.subplots_adjust(bottom=0.15, right=0.9, top=0.9, left=0.1)
cax = plt.axes([0.1, 0.05, 0.8, 0.05])


plt.colorbar(cax=cax,orientation="horizontal")
plt.clim(0,50)

plt.show()
