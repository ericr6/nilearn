"""
3D and 4D niimgs: handling and visualizing
==========================================

Here we discover how to work with 3D and 4D niimgs.
"""
import sys

dir=sys.argv[1];
prefix=sys.argv[2];
idx=0;

###############################################################################
# Downloading tutorial datasets from Internet
# --------------------------------------------
#
# Nilearn comes with functions that download public data from Internet
#
# Let's first check where the data is downloaded on our disk:
from nilearn import datasets
print('Datasets are stored in: %r' % datasets.get_data_dirs("/home/eric/wdir/wdir_nilearn/inputdata/"))

###############################################################################
# Let's now retrieve a motor contrast from a Neurovault repository
motor_images = datasets.fetch_neurovault_motor_task()
print(motor_images.images)

###############################################################################
# motor_images is a list of filenames. We need to take the first one
tmap_filename = motor_images.images[0]


###############################################################################
# Visualizing a 3D file
# ----------------------
#
# The file contains a 3D volume, we can easily visualize it as a
# statistical map:
from nilearn import plotting
display = plotting.plot_stat_map(tmap_filename)
idx+=1
display.savefig(dir + '/' + prefix + str(idx))

###############################################################################
# Visualizing works better with a threshold
display = plotting.plot_stat_map(tmap_filename, threshold=3)
idx+=1
display.savefig(dir+'/'+prefix+str(idx))

# Warning, to limit the size of data input,we stop the script here    
exit()

###############################################################################
# Visualizing one volume in a 4D file
# -----------------------------------
#
# We can download resting-state networks from the Smith 2009 study on
# correspondance between rest and task
rsn = datasets.fetch_atlas_smith_2009()['rsn10']
print(rsn)

###############################################################################
# It is a 4D nifti file. We load it into the memory to print its
# shape.
from nilearn import image

print(image.load_img(rsn).shape)

###############################################################################
# We can retrieve the first volume (note that Python indexing starts at 0):
first_rsn = image.index_img(rsn, 0)
print(first_rsn.shape)

###############################################################################
# first_rsn is a 3D image.
#
# We can then plot it
display = plotting.plot_stat_map(first_rsn)
idx+=1
display.savefig(dir+'/'+prefix+str(idx))


###############################################################################
# Looping on all volumes in a 4D file
# -----------------------------------
#
# If we want to plot all the volumes in this 4D file, we can use iter_img
# to loop on them.
#
# Then we give a few arguments to plot_stat_map in order to have a more
# compact display.

for img in image.iter_img(rsn):
    # img is now an in-memory 3D img
    idx+=1
    display = plotting.plot_stat_map(img, threshold=3, display_mode="z", cut_coords=1,
                           colorbar=False)
    display.savefig(dir + '/' + prefix + str(idx))
                           
    
###############################################################################
# plotting.show is useful to force the display of figures when running
# outside IPython
#plotting.show()

#########################################################################
# |
#
# ______
#
# To recap, neuroimaging images (niimgs as we call them) come in
# different flavors:
#
# * 3D images, containing only one brain volume
# * 4D images, containing multiple brain volumes.
#
# More details about the input formats in nilearn for 3D and 4D images is
# given in the documentation section: :ref:`loading_data`.
#
# Functions accept either 3D or 4D images, and we need to use on the one
# hand :func:`nilearn.image.index_img` or :func:`nilearn.image.iter_img`
# to break down 4D images into 3D images, and on the other hand
# :func:`nilearn.image.concat_imgs` to group a list of 3D images into a 4D
# image.
