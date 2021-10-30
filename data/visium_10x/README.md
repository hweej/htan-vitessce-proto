https://scanpy-tutorials.readthedocs.io/en/latest/spatial/basic-analysis.html


# Fix 1
# Downgrade pandas to 1.3.2 -> 1.2.5
conda install pandas=1.2

# Fix 2
https://github.com/theislab/anndata/pull/579/files
pip install git+git://github.com/theislab/anndata@master

# Other notes
conda install zarr

Add import numpy as np to script




### instructions
```
make all
conda activate vitessce-tutorial-env
make install
```

