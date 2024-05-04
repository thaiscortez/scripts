# -*- coding: utf-8 -*-
"""teste_bacia.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j84WmGlGYeQWOB4LC2A8g6rjDW3N7gAN
"""

!pip install xarray
!pip install geopandas
!pip install rasterio
!pip install salem

import xarray as xr
import geopandas as gpd
from shapely.geometry import mapping,Point, Polygon, LineString
from rasterio.features import geometry_mask
import rasterio
import salem

from pyproj import Proj, transform
import pandas as pd

url = 'https://coastwatch.pfeg.noaa.gov/erddap/griddap/chirps20GlobalDailyP05_Lon0360'
ds_diario = xr.open_dataset(url)
ds_diario

# Carregar o shapefile
shape = '/home/cepremg/Documentos/thais/shapefile/vitoria.conquista.shp'
shape = salem.read_shapefile(shape)

ds_diario.coords['longitude'] = ((ds_diario.coords['longitude'] + 180) % 360) - 180
ds_diario = ds_diario.sortby(ds_diario.longitude)

dados = ds_diario['precip'][:,:,:].sel(latitude=slice(-17,-14), longitude=slice(-42,-38))
dados

recorte = dados[0].salem.roi(shape=shape)

recorte

recorte.salem.quick_map()


