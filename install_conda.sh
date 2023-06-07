#!/bin/bash

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -f -p $HOME/miniconda
ls $HOME/miniconda
cat $HOME/miniconda/etc/profile.d/conda.sh >> $HOME/.bashrc
chmod 777 .bashrc
cat $HOME/.bashrc & source $HOME/.bashrc
conda init bash

