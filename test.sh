#!/bin/bash
#path to save images 
arg1=$1
#prefix for images 
arg2=$2
#Data input for nilearn.zip
FILE=nilearn_data.zip
DATAPATH_NILEARN=~/. 

# wget https://transfer.sh/wTlV3/input_nilearn.zip
if [ -f $FILE ]; then
  unzip -o $FILE
  mv nilearn_data $DATAPATH_NILEARN
fi

# args 1 is the directory where to save image , args 2 is the prefix for images.
# if args are missing, program failed.  
python3 plot_3d_and_4d_niimg_nogui.py $arg1 $arg2
