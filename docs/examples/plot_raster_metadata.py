"""
# Raster's metadata

This example shows how to get metadata stored raster files or raster objects.
"""

from pprint import pprint

import rasterio
from osgeo import gdal

print(gdal.__version__)
print(rasterio.__version__)

############################################################
# ## With Rasterio
#
# To access metadata, use `rasterio.io.DatasetReader.profile`

raster_file = "data/raster_1_b2.tif"

with rasterio.open(raster_file) as dataset:
    profile = dataset.profile

pprint(profile)

############################################################
# Rasterio's `Profile` is a dict like class.
# Each items can be access with `.get()` or `[]`.

print(profile.get("dtype"))
print(profile["dtype"])

############################################################
# ## With GDAL

info = gdal.Info(raster_file)
print(info)

############################################################
# `gdal.info()` returns a printable strings which describe
# metadatas of a given file.
# To get each items as a value, `Open` as a dataset, and access
# properties.

dataset = gdal.Open(raster_file)
band = dataset.GetRasterBand(1)
print(gdal.GetDataTypeName(band.DataType))
dataset = None

############################################################
# Refer
# [gdal.org](https://gdal.org/api/python/osgeo.gdal.html#osgeo.gdal.Band)
# to access to other properties.
