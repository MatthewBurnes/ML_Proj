



import requests as rqs #urls from website
import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
import h5py as h5 # hdf5 files - large files compact
import shutil as sh
import os as os
from PIL import Image, ImageDraw
import math
import scipy
import getUrls
from scipy.stats import spearmanr
import makePrediction

# def seefailures():
#     for row in getUrls.getURL():
#         res = makePrediction.makePrediction(row[0])
#         if res != row[1]:
#             print(res)
#             print(row)
# seefailures()
url = 'https://data.mangonetwork.org/data/transport/mango/archive/cvo/greenline/raw/2024/300/04/mango-cvo-greenline-20241026-043400.hdf5'
r = rqs.get(url, stream=True)
dump = r.raw
cwd = os.getcwd()
location = os.path.abspath(cwd)
with open('testfile.hdf5', 'wb') as location:
    sh.copyfileobj(dump, location)
file = h5.File('testfile.hdf5', 'r+')
arr = file['image'] #array of values
a = arr[100:450, 100:550] #crop the image
a = arr[0:][0:]
print(a)

plt.imshow(a, cmap='gray', vmax = 10000)
plt.show()



#seefailures()
