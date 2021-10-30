import scanpy as sc
import scipy.cluster
import numpy as np
from os.path import join

print("Retrieving dataset")
adata = sc.datasets.visium_sge(sample_id="V1_Human_Lymph_Node", include_hires_tiff=True)

# Calculate QC metrics
print("Calculating QC Metrics")
adata.var_names_make_unique()
adata.var["mt"] = adata.var_names.str.startswith("MT-")
sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], inplace=True)

# Perform basic filtering
print("Performing basic filtering")
sc.pp.filter_cells(adata, min_counts=5000)
sc.pp.filter_cells(adata, max_counts=35000)
adata = adata[adata.obs["pct_counts_mt"] < 20]
sc.pp.filter_genes(adata, min_cells=10)

# Perform normalization
sc.pp.normalize_total(adata, inplace=True)
sc.pp.log1p(adata)
# Determine the top 300 highly variable genes.
sc.pp.highly_variable_genes(adata, flavor="seurat", n_top_genes=300)

# Dimensionality reduction and clustering
sc.pp.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.tl.leiden(adata, key_added="clusters")

# Get the highly variable gene matrix as a plain NumPy array
X_hvg_arr = adata[:, adata.var['highly_variable']].X.toarray()
X_hvg_index = adata[:, adata.var['highly_variable']].var.copy().index

# Perform average linkage hierarchical clustering on along the genes axis of the array
Z = scipy.cluster.hierarchy.linkage(X_hvg_arr.T, method="average", optimal_ordering=True)

# Get the hierarchy-based ordering of genes.
num_genes = adata.var.shape[0]
highly_var_index_ordering = scipy.cluster.hierarchy.leaves_list(Z)
highly_var_genes = X_hvg_index.values[highly_var_index_ordering].tolist()

all_genes = adata.var.index.values.tolist()
not_var_genes = adata.var.loc[~adata.var['highly_variable']].index.values.tolist()

def get_orig_index(gene_id):
    return all_genes.index(gene_id)
var_index_ordering = list(map(get_orig_index, highly_var_genes)) + list(map(get_orig_index, not_var_genes))

adata = adata[:, var_index_ordering].copy()
adata.obsm['X_hvg'] = adata[:, adata.var['highly_variable']].X.copy()
adata.obsm['spatial'] = adata.obsm['spatial'].astype('uint16')

# Convert images from interleaved to non-interleaved (the color axis should be first).
img_hires = adata.uns['spatial']['V1_Human_Lymph_Node']['images']['hires']
img_lowres = adata.uns['spatial']['V1_Human_Lymph_Node']['images']['lowres']

adata.uns['spatial']['V1_Human_Lymph_Node']['images']['hires'] = np.transpose(img_hires, (2, 0, 1))
adata.uns['spatial']['V1_Human_Lymph_Node']['images']['lowres'] = np.transpose(img_lowres, (2, 0, 1))

adata.write_zarr("V1_Human_Lymph_Node.zarr")
