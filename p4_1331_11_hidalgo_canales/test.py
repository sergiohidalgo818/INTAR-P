import pandas
import sklearn
a = (1,)
b = (1,2,)
c = (1,2,3)

print(len(a))
print(len(b))
print(len(c))

A = pandas.DataFrame()
A.to_string(index=False)

from sklearn.cluster import KMeans, SpectralClustering
from sklearn.decomposition import PCA, KernelPCA
from sklearn.preprocessing import normalize

from sklearn import preprocessing
