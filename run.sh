#!/bin/bash

NIDIR=/iexec_in/nilearn_data
unzip $NIDIR.zip
DATAPATH_NILEARN=~/.

# Data Management
if [ -d $NIDIR ]; then
  echo "data input exists"
  mv $NIDIR $DATAPATH_NILEARN
  echo "copy files in ${DATAPATH_NILEARN}"
else
  echo "data not found ... download"
fi

python3 plot_3d_and_4d_niimg_nogui.py /iexec_out image_

echo "{ \"deterministic-output-path\" : \"/iexec_out/image_1.png\" }" > /iexec_out/computed.json
