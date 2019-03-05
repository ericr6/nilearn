#!/bin/bash
#path to save images 
arg1=$1
#prefix for images 
arg2=$2

NIDIR=/iexec_in/nilearn_data
DATAPATH_NILEARN=~/. 

# Data Management 
if [ -d $NIDIR ]; then
  echo "data input exists"  
  mv $NIDIR $DATAPATH_NILEARN
  echo "copy files in ${DATAPATH_NILEARN}"
else 
  echo "data not found ... download"  
fi

python3 plot_3d_and_4d_niimg_nogui.py $arg1 $arg2
