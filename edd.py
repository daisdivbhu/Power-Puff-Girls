from matplotlib import pyplot as plt
from skimage import data
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread
example_file=glob.glob(r"C:\Users\HP\Downloads\127927812.cAdkCBDv")[0]
im=imread(example_file,as_grey=True)
plt.imshow(im, cmap=cm.gray)
plt.show()
blobs_log=blob_log(im,max_sigma=30,num_sigma=10,threshhold=.1)
# comoute raddii in the 3rd column.
blobs_log[:,2]=blobs_log[:,2]*sqrt(2)
numrows=len(blobs_log)
print("number of mosquitos counted :",numrows)
fig,ax=plt.subplots(1,1)
plt.imshow(im,cmap=cm.gray)
for blob in blobs_log:
    y,x,r=blob
    c=plt.circle((x,y),r+5,color='lime',linewidth=2,fill=false)
    ax.add_patch(c)
if numrows>=10:
    print("Alert - prevention required")
else
    print("safe zone")
