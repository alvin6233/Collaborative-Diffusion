#!/bin/bash

conda env create -f environment.yaml
conda activate codiff

pip install transformers==4.19.2 scann kornia==0.6.4 torchmetrics==0.6.0
conda install -c anaconda git
pip install git+https://github.com/arogozhnikov/einops.git

directory="pretrained"

if [ ! -d "$directory" ]; then
    mkdir "$directory"

wget https://download.openxlab.org.cn/models/abel-9512/codiff/weight/512_codiff_mask_text -O ./pretrained/512_codiff_mask_text.ckpt
wget https://download.openxlab.org.cn/models/abel-9512/codiff/weight/512_mask -O ./pretrained/512_mask.ckpt
wget https://download.openxlab.org.cn/models/abel-9512/codiff/weight/512_text -O ./pretrained/512_text.ckpt
wget https://download.openxlab.org.cn/models/abel-9512/codiff/weight/512_vae -O ./pretrained/512_vae.ckpt