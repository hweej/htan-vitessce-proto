#!/usr/bin/env bash

conda create -n vitessce-tutorial-env python=3.8 -y
# conda activate vitessce-tutorial-env

conda install -c bioconda scanpy -y
conda install -c conda-forge leidenalg -y
conda install -c conda-forge scipy -y
conda install pandas=1.2 -y
conda install zarr -y
pip install git+git://github.com/theislab/anndata@master

python dataset_preprocessing.py
