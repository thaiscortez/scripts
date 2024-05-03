# -*- coding: utf-8 -*-
"""geotiff.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iocD1-QIetrIWyrpjPVckqMpdUkmuc90
"""

import netCDF4 as nc
import numpy as np
import rasterio
from rasterio.transform import from_origin
from rasterio.warp import calculate_default_transform
from rasterio.enums import Resampling
import os, glob

import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
# %%time
# #========================================================================#
# #               Definição da região e período dos dados
# #========================================================================#
# # Utiliza um ponto central e soma 20 km para cada lado, formando um quadrado.
# lat_central, lon_central, ds_km = -15.9, -41.90, 20 # =20 km
# ds_graus = ds_km/100.0
# 
# lat_min = lat_central - ds_graus
# lat_max = lat_central + ds_graus
# lon_min = lon_central - ds_graus
# lon_max = lon_central + ds_graus
# 
# # período dos dados
# ano_min, mes_min, dia_min = '1981', '01', '01'
# ano_max, mes_max, dia_max = '2022', '12', '31'
# time_min, time_max = f'{ano_min}-{mes_min}-{dia_min}', f'{ano_max}-{mes_max}-{dia_max}'
# 
# #========================================================================#
# #                               CHIRPS
# #========================================================================#
# # leitudo do dado
# chirps = xr.open_dataset('https://coastwatch.pfeg.noaa.gov/erddap/griddap/chirps20GlobalDailyP05_Lon0360')
# 
# # tranforma longitudes
# chirps.coords['longitude'] = ((chirps.coords['longitude'] + 180) % 360) - 180 ; chirps = chirps.sortby(chirps.longitude)
# 
# # recorta para um ponto
# #chirps_regiao = dset.sel(lat=lat_central, lon=(lon_central), method='nearest').sel(time=slice(time_min, time_max))
# 
# # recorta para um quadrado e no tempo
# chirps_regiao = chirps.sel(longitude=slice(lon_min, lon_max), latitude=slice(lat_min, lat_max)).sel(time=slice(time_min, time_max))
# 
# # calcula a média espacial dentro da região
# chirps_mean = chirps_regiao.mean(dim=['latitude', 'longitude'])
# 
# # transforma para tabela
# df_chirps = chirps_mean.to_dataframe()
# df_chirps
#

files = sorted(glob.glob("/home/cepremg/Documentos/thais/merge_dez2021/*.nc"))
files

# Abra o arquivo NetCDF
for file in files:
    merge = nc.Dataset(file, 'r')
    ano = file[57:65]

# Leia os dados que deseja converter em um GeoTIFF
    data = merge.variables['PREC_surface'][0, :, :]  # Suponha que você deseja a primeira banda de dados

    # Obtenha informações geoespaciais dos metadados do NetCDF
    lon = merge.variables['longitude'][:]
    lat = merge.variables['latitude'][:]
    transform = from_origin(lon[0], lat[-1], abs(lon[1] - lon[0]), abs(lat[1] - lat[0]))

    # Crie um arquivo GeoTIFF com o número correto de bandas
    with rasterio.open(f'/home/cepremg/Documentos/thais/teste{ano}.tif', 'w', driver='GTiff', height=data.shape[0], width=data.shape[1], count=1, dtype=data.dtype, crs='+proj=latlong', transform=transform) as dst:
        dst.write(data, 1)

    # Feche o arquivo NetCDF
    merge.close()

with rasterio.open('/home/cepremg/Documentos/thais/teste.tif') as src:
     metadata = src.meta
     transform = src.transform
     data = src.read(1)  # Leitura da banda 1 (substitua 1 pelo número da banda que você deseja ler)

# Exemplo de como acessar informações do arquivo
print("Metadados do arquivo GeoTIFF:")
print(metadata)
print("\nTransformação geoespacial:")
print(transform)

# Especifique o caminho para o arquivo GeoTIFF que você deseja plotar
file_path = '/home/cepremg/Documentos/thais/teste.tif'

# Abra o arquivo GeoTIFF
with rasterio.open(file_path) as src:
    # Leia a banda que você deseja plotar (por exemplo, a primeira banda)
    band = src.read(1)

    # Plote a banda
    plt.figure(figsize=(10, 8))
    plt.imshow(band, cmap='viridis')  # Pode escolher um mapa de cores (cmap) diferente
    plt.title('Mapa do GeoTIFF')
    plt.colorbar()
    plt.show()

