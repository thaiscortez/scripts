# -*- coding: utf-8 -*-
"""chirps_mensal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eCvglsZcwVYbQwyrG-iujpVJUXvaOvEe
"""

!pip install xarray
!pip install time
!pip install proplot
!pip install pandas
!pip install matplotlib
!pip install seaborn
!pip install numpy
!pip install csv
!pip install datetime

import xarray as xr
import time
import proplot as pplt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings("ignore")

from google.colab import drive
drive.mount('/content/drive')

#MÁXIMO DIÁRIO - SÉRIE HISTÓRICA
chirps = pd.read_excel('/content/drive/MyDrive/mestrado/Dados/chirps/chirps_maxd (1).xlsx')
chirps

chirps = chirps.set_index('date')
chirps

## ---------------------------------------------------------- #
#                          MENSAL
# ---------------------------------------------------------- #
# total
#mensal = chirps.groupby(pd.Grouper(freq='1M')).mean()
#mensal = chirps.groupby(pd.Grouper(freq='1M')).sum()

# climatológica
#mensal_climatologia = mensal.groupby(mensal.index.month).mean()

# ---------------------------------------------------------- #
#                          ANUAL
# ---------------------------------------------------------- #
# total
anual = chirps.groupby(pd.Grouper(freq='1Y')).mean()
anual = chirps.groupby(pd.Grouper(freq='1Y')).sum()

mensal.to_excel(f'/home/cepremg/Documentos/thais/chirps/mensal.xlsx')

anual.to_excel(f'/content/drive/MyDrive/mestrado/Dados/chirps/anual2.xlsx')

mensal_climatologia.to_excel(f'/home/cepremg/Documentos/thais/mensal_climatologia.xlsx')

mensal_climatologia = pd.read_excel('/content/drive/MyDrive/mestrado/Dados/chirps/mensal_climatologia.xlsx')
mensal_climatologia

chirps_2021 = pd.read_excel('/content/drive/MyDrive/mestrado/Dados/chirps/chirps_maxd (1).xlsx', sheet_name='2021')
chirps_2021

mensal = chirps_2021.groupby('mes').sum()
mensal

mensal = mensal.reset_index(drop=True)
mensal.mes

#criando a figura
fig, ax = pplt.subplots(nrows=3,ncols=2, figsize=(14,14), tight=True)

#largura da barra
barWidth = 0.22

#vetor
data = [1,2,3,4,5,6,7,8,9,10,11,12]

#posição das barras
t1 = np.arange(len(data))
t2 = [x + barWidth for x in t1]
t3 = [x + barWidth for x in t2]
t4 = [x + barWidth for x in t3]

#FIGURA 1
# gráfico de barras
ax[0,0].bar(t1, mensal_climatologia.caraí, width=barWidth, color ='royalblue', label = 'Caraí (MG)')
ax[0,0].bar(t2, mensal_climatologia.carlos_chagas, width=barWidth, color = 'limegreen', label = 'Carlos Chagas (MG)')
ax[0,0].bar(t3, mensal_climatologia.unai, width=barWidth, color = 'salmon', label ='Unaí (MG)' )
#linha
ax[0, 0].plot(t1, mensal.caraí, color='royalblue', linewidth=2, label='Caraí (2021)')
ax[0, 0].plot(t1, mensal.carlos_chagas, color='limegreen',linewidth=2, label='Carlos Chagas (2021)')
ax[0, 0].plot(t1, mensal.unai, color='salmon', linewidth=2, label='Unaí (2021)')

ax[0,0].tick_params(axis='x', labelsize=10, rotation=0)
ax[0,0].set_yticks([0,100,200,300,400,500,600,700,800,900,1000])
ax[0,0].xaxis.set_minor_locator(plt.NullLocator())
ax[0,0].yaxis.set_minor_locator(plt.NullLocator())
ax[0,0].legend(fontsize= 24, loc= 'upper right')
ax[0,0].tick_params(axis='y', labelsize=16, rotation=0)
ax[0,0].set_ylabel('Precipitação (mm/mês)', fontsize=24)  # Edita o rótulo do eixo y
ax[0,0].set_xlabel('Meses', fontsize = 24)
ax[0,0].text(0, 1.02, 'a)', transform=ax[0, 0].transAxes, fontsize=14, fontweight='bold')

#---------------------------------------------------------------------------------------------
#FIGURA 2
# gráfico de barras
ax[0,1].bar(t1, mensal_climatologia.governador, width=barWidth, color ='royalblue', label ='Governador Valadares (MG)')
ax[0,1].bar(t2, mensal_climatologia.jampruca, width=barWidth, color ='limegreen', label ='Jampruca (MG)')
ax[0,1].bar(t3, mensal_climatologia.montes, width=barWidth, color = 'salmon', label = 'Montes Claros (MG)')
#linha
ax[0,1].plot(t1, mensal.governador, color='royalblue', linestyle='-', linewidth=2, label='Governador Valadares (2021)')
ax[0,1].plot(t1, mensal.jampruca, color='limegreen', linestyle='-', linewidth=2, label='Jampruca (2021)')
ax[0,1].plot(t1, mensal.montes, color='salmon', linestyle='-', linewidth=2, label='Montes Claros (2021)')

ax[0,1].tick_params(axis='x', labelsize=10, rotation=0)
ax[0,1].set_yticks([0,100,200,300,400,500,600,700,800,900,1000])
ax[0,1].xaxis.set_minor_locator(plt.NullLocator())
ax[0,1].yaxis.set_minor_locator(plt.NullLocator())
ax[0,1].legend(fontsize= 24, loc= 'upper left')
ax[0,1].set_ylabel('Precipitação mm/mês', fontsize=24)
ax[0,1].set_xlabel('Meses', fontsize = 24)
ax[0,1].text(0, 1.02, 'b)', transform=ax[0, 1].transAxes, fontsize=14, fontweight='bold')

#---------------------------------------------------------------------------------------------
#FIGURA 3
# gráfico de barras
ax[1,0].bar(t1, mensal_climatologia.ilheus, width=barWidth, color = 'royalblue', label = 'Ilheús (BA)')
ax[1,0].bar(t2, mensal_climatologia.itabuna, width=barWidth, color = 'limegreen', label = 'Itabuna (BA)')
ax[1,0].bar(t3, mensal_climatologia.itapetinga, width=barWidth, color ='salmon', label ='Itapetinga (BA)')
#linha
ax[1,0].plot(t1, mensal.ilheus, color='royalblue',  linewidth=2, label='Ilheús (2021)')
ax[1,0].plot(t1, mensal.itabuna, color='limegreen', linewidth=2, label='Itabuna (2021)')
ax[1,0].plot(t1, mensal.itapetinga, color='salmon', linewidth=2, label='Itapetinga (2021)')

ax[1,0].tick_params(axis='x', labelsize=10, rotation=0)
ax[1,0].set_yticks([0,100,200,300,400,500,600,700,800,900,1000])
ax[1,0].xaxis.set_minor_locator(plt.NullLocator())
ax[1,0].yaxis.set_minor_locator(plt.NullLocator())
ax[1,0].legend(fontsize= 24, loc= 'upper left')
ax[1,0].tick_params(axis='y', labelsize=16, rotation=0)
ax[1,0].set_ylabel('Precipitação mm/mês', fontsize=24)
ax[1,0].set_xlabel('Meses', fontsize = 24)
ax[1,0].text(0, 1.02, 'c)', transform=ax[1,0].transAxes, fontsize=14, fontweight='bold')


#---------------------------------------------------------------------------------------------
#FIGURA 4
# gráfico de barras
ax[1,1].bar(t1, mensal_climatologia.jaguaquara, width=barWidth, color = 'royalblue', label = 'Jaguaquara (BA)')
ax[1,1].bar(t2, mensal_climatologia.itacare, width=barWidth, color = 'limegreen', label = 'Itacaré (BA)')
ax[1,1].bar(t3, mensal_climatologia.matuipe, width=barWidth, color = 'salmon', label = 'Matuípe (BA)')
#linha
ax[1,1].plot(t1, mensal.jaguaquara, color='royalblue', linewidth=2, label='Jaguaquara (2021)')
ax[1,1].plot(t1, mensal.itacare, color='limegreen',  linewidth=2, label='Itacaré (2021)')
ax[1,1].plot(t1, mensal.matuipe, color='salmon',  linewidth=2, label='Matuípe (2021)')

ax[1,1].tick_params(axis='x', labelsize=10, rotation=0)
ax[1,1].set_yticks([0,100,200,300,400,500,600,700,800,900,1000])
ax[1,1].xaxis.set_minor_locator(plt.NullLocator())
ax[1,1].yaxis.set_minor_locator(plt.NullLocator())
ax[1,1].legend(fontsize= 24, loc= 'upper right')
ax[1,1].set_ylabel('Precipitação mm/mês', fontsize=24)
ax[1,1].set_xlabel('Meses', fontsize = 24)
ax[1,1].text(0, 1.02, 'd)', transform=ax[1,1].transAxes, fontsize=14, fontweight='bold')

#-----------------------------------------------------------------------------------------------
#FIGURA 5
ax[2,0].bar(t1, mensal_climatologia.gandu, width=barWidth, color ='royalblue', label ='Gandu (BA)')
ax[2,0].bar(t2, mensal_climatologia.medeiros, width=barWidth, color = 'limegreen', label = 'Medeiros Neto (BA)')
ax[2,0].bar(t3, mensal_climatologia.porto, width=barWidth, color = 'salmon', label = 'Porto Seguro (BA)')
#linha
ax[2,0].plot(t1, mensal.gandu, color='royalblue', linewidth=2, label='Gandu (2021)')
ax[2,0].plot(t1, mensal.medeiros, color='limegreen',  linewidth=2, label='Medeiros Neto (2021)')
ax[2,0].plot(t1, mensal.porto, color='salmon',  linewidth=2, label='Porto Seguro (2021)')

ax[2,0].tick_params(axis='x', labelsize=10, rotation=0)
ax[2,0].set_yticks([0,100,200,300,400,500,600,700,800,900,1000])
ax[2,0].xaxis.set_minor_locator(plt.NullLocator())
ax[2,0].yaxis.set_minor_locator(plt.NullLocator())
ax[2,0].legend(fontsize= 24, loc= 'upper left')
ax[2,0].tick_params(axis='x', labelsize=16, rotation=0)
ax[2,0].tick_params(axis='y', labelsize=16, rotation=0)
ax[2,0].set_xlabel('Meses', fontsize = 24)
ax[2,0].set_ylabel('Precipitação mm/mês', fontsize=24)
# Defina as posições exatas para os rótulos do eixo x
month_positions = t2
# Configuração dos rótulos do eixo x na terceira subtrama (ax[2,0])
ax[2,0].set_xticks(month_positions)
ax[2,0].set_xticklabels(['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ'], fontsize=14)
ax[2,0].text(0, 1.02, 'e)', transform=ax[2,0].transAxes, fontsize=14, fontweight='bold')

#----------------------------------------------------------------------------------------------------
#FIGURA 6
ax[2,1].bar(t1, mensal_climatologia.salvador, width=barWidth, color = 'royalblue', label = 'Salvador (BA)')
ax[2,1].bar(t2, mensal_climatologia.vitoria, width=barWidth, color = 'limegreen', label = 'Vitória da Conquista (BA)')
#linha
ax[2,1].plot(t1, mensal.salvador, color='royalblue',  linewidth=2, label='Salvador (2021)')
ax[2,1].plot(t1, mensal.vitoria, color='limegreen', linewidth=2, label='Vitória da Conquista (2021)')

ax[2,1].tick_params(axis='x', labelsize=14, rotation=0)
ax[2,1].set_yticks([0,100,200,300,400,500,600,700,800,900,1000])
ax[2,1].xaxis.set_minor_locator(plt.NullLocator())
ax[2,1].yaxis.set_minor_locator(plt.NullLocator())
ax[2,1].legend(fontsize= 24, loc= 'upper right')
ax[2,1].tick_params(axis='x', labelsize=16, rotation=0)
ax[2,1].tick_params(axis='y', labelsize=16, rotation=0)
# Defina as posições exatas para os rótulos do eixo x
month_positions = t2
# Configuração dos rótulos do eixo x na terceira subtrama (ax[2,0])
ax[2,1].set_xticks(month_positions)
ax[2,1].set_xticklabels(['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ'], fontsize=14)
ax[2,1].set_ylabel('Precipitação mm/mês', fontsize=24)
ax[2,1].set_xlabel('Meses', fontsize = 24)
ax[2,1].text(0, 1.02, 'f)', transform=ax[2,1].transAxes, fontsize=14, fontweight='bold')

fig.savefig('/content/drive/MyDrive/mestrado/Dados/Figuras/chirps/mensal_completo.png', dpi=300)

anual = pd.read_excel('/content/drive/MyDrive/mestrado/Dados/chirps/anual2.xlsx')
anual

#criando a figura
fig, ax = pplt.subplots(nrows=3,ncols=2, figsize=(14,14), tight=True)

#largura da barra
barWidth = 0.22

#vetor
data = [1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

#posição das barras
t1 = np.arange(len(data))
t2 = [x + barWidth for x in t1]
t3 = [x + barWidth for x in t2]
t4 = [x + barWidth for x in t3]

#FIGURA 1
# gráfico de barras
ax[0,0].bar(t1, anual.caraí, width=barWidth, color ='royalblue', label = 'Caraí (MG)')
ax[0,0].bar(t2, anual.carlos_chagas, width=barWidth, color = 'limegreen', label = 'Carlos Chagas (MG)')
ax[0,0].bar(t3, anual.unai, width=barWidth, color = 'salmon', label ='Unaí (MG)' )
ax[0,0].tick_params(axis='x', labelsize=10, rotation=0)
ax[0,0].set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500])
ax[0,0].xaxis.set_minor_locator(plt.NullLocator())
ax[0,0].yaxis.set_minor_locator(plt.NullLocator())
ax[0,0].legend(fontsize= 14, loc= 'upper right')
ax[0,0].tick_params(axis='y', labelsize=16, rotation=0)
ax[0,0].set_ylabel('Precipitação (mm/ano)', fontsize=24)  # Edita o rótulo do eixo y
ax[0,0].set_xlabel('Anos', fontsize = 24)
ax[0,0].text(0, 1.02, 'a)', transform=ax[0, 0].transAxes, fontsize=14, fontweight='bold')

#---------------------------------------------------------------------------------------------
#FIGURA 2
# gráfico de barras
ax[0,1].bar(t1, anual.governador, width=barWidth, color ='royalblue', label ='Governador Valadares (MG)')
ax[0,1].bar(t2, anual.jampruca, width=barWidth, color ='limegreen', label ='Jampruca (MG)')
ax[0,1].bar(t3, anual.montes, width=barWidth, color = 'salmon', label = 'Montes Claros (MG)')
ax[0,1].tick_params(axis='x', labelsize=10, rotation=0)
ax[0,1].set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500])
ax[0,1].xaxis.set_minor_locator(plt.NullLocator())
ax[0,1].yaxis.set_minor_locator(plt.NullLocator())
ax[0,1].legend(fontsize= 14, loc= 'upper left')
ax[0,1].set_ylabel('Precipitação mm/ano', fontsize=24)
ax[0,1].set_xlabel('Anos', fontsize = 24)
ax[0,1].text(0, 1.02, 'b)', transform=ax[0, 1].transAxes, fontsize=14, fontweight='bold')

#---------------------------------------------------------------------------------------------
#FIGURA 3
# gráfico de barras
ax[1,0].bar(t1, anual.ilheus, width=barWidth, color = 'royalblue', label = 'Ilheús (BA)')
ax[1,0].bar(t2, anual.itabuna, width=barWidth, color = 'limegreen', label = 'Itabuna (BA)')
ax[1,0].bar(t3, anual.itapetinga, width=barWidth, color ='salmon', label ='Itapetinga (BA)')
ax[1,0].tick_params(axis='x', labelsize=10, rotation=0)
ax[1,0].set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500])
ax[1,0].xaxis.set_minor_locator(plt.NullLocator())
ax[1,0].yaxis.set_minor_locator(plt.NullLocator())
ax[1,0].legend(fontsize= 14, loc= 'upper right')
ax[1,0].tick_params(axis='y', labelsize=16, rotation=0)
ax[1,0].set_ylabel('Precipitação mm/ano', fontsize=24)
ax[1,0].set_xlabel('Anos', fontsize = 24)
ax[1,0].text(0, 1.02, 'c)', transform=ax[1, 0].transAxes, fontsize=14, fontweight='bold')

#---------------------------------------------------------------------------------------------
#FIGURA 4
# gráfico de barras
ax[1,1].bar(t1, anual.jaguaquara, width=barWidth, color = 'royalblue', label = 'Jaguaquara (BA)')
ax[1,1].bar(t2, anual.itacare, width=barWidth, color = 'limegreen', label = 'Itacaré (BA)')
ax[1,1].bar(t3, anual.matuipe, width=barWidth, color = 'salmon', label = 'Matuipe (BA)')
ax[1,1].tick_params(axis='x', labelsize=10, rotation=0)
ax[1,1].set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500])
ax[1,1].xaxis.set_minor_locator(plt.NullLocator())
ax[1,1].yaxis.set_minor_locator(plt.NullLocator())
ax[1,1].legend(fontsize= 14, loc= 'upper right')
ax[1,1].set_ylabel('Precipitação mm/ano', fontsize=24)
ax[1,1].set_xlabel('Anos', fontsize = 24)
ax[1,1].text(0, 1.02, 'd)', transform=ax[1,1].transAxes, fontsize=14, fontweight='bold')

#-----------------------------------------------------------------------------------------------
#FIGURA 5
ax[2,0].bar(t1, anual.gandu, width=barWidth, color ='royalblue', label ='Gandu (BA)')
ax[2,0].bar(t2, anual.medeiros, width=barWidth, color = 'limegreen', label = 'Medeiros Neto (BA)')
ax[2,0].bar(t3, anual.porto, width=barWidth, color = 'salmon', label = 'Porto Seguro (BA)')
ax[2,0].tick_params(axis='x', labelsize=10, rotation=0)
ax[2,0].set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500])
ax[2,0].xaxis.set_minor_locator(plt.NullLocator())
ax[2,0].yaxis.set_minor_locator(plt.NullLocator())
ax[2,0].legend(fontsize= 14, loc= 'upper right')
ax[2,0].tick_params(axis='x', labelsize=16, rotation=0)
ax[2,0].tick_params(axis='y', labelsize=16, rotation=0)
# Defina as posições exatas para os rótulos do eixo x (anos ímpares)
year_positions = t1[::2]  # Use t1 para anos ímpares, t1[::2] pega todos os elementos nas posições ímpares
# Configuração dos rótulos do eixo x na última subtrama (ax[2,1])
ax[2,0].set_xticks(year_positions)
ax[2,0].set_xticklabels([str(year) for year in data[::2]], fontsize=14, rotation=45, ha="right")
ax[2,0].set_ylabel('Precipitação mm/ano', fontsize=24)
ax[2,0].set_xlabel('Anos', fontsize = 24)
ax[2,0].text(0, 1.02, 'e)', transform=ax[2,0].transAxes, fontsize=14, fontweight='bold')

#----------------------------------------------------------------------------------------------------
#FIGURA 6
ax[2,1].bar(t1, anual.salvador, width=barWidth, color = 'royalblue', label = 'Salvador (BA)')
ax[2,1].bar(t2, anual.vitoria, width=barWidth, color = 'limegreen', label = 'Vitória da Conquista (BA)')
ax[2,1].tick_params(axis='x', labelsize=10, rotation=0)
ax[2,1].set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500])
ax[2,1].xaxis.set_minor_locator(plt.NullLocator())
ax[2,1].yaxis.set_minor_locator(plt.NullLocator())
ax[2,1].legend(fontsize= 14, loc= 'upper right')
ax[2,1].tick_params(axis='x', labelsize=16, rotation=0)
# Defina as posições exatas para os rótulos do eixo x (anos ímpares)
year_positions = t1[::2]  # Use t1 para anos ímpares, t1[::2] pega todos os elementos nas posições ímpares
# Configuração dos rótulos do eixo x na última subtrama (ax[2,1])
ax[2,1].set_xticks(year_positions)
ax[2,1].set_xticklabels([str(year) for year in data[::2]], fontsize=14, rotation=45, ha="right")  # Ajuste a rotação conforme necessário
ax[2,1].set_ylabel('Precipitação mm/ano', fontsize=24)
ax[2,1].set_xlabel('Anos', fontsize = 24)
ax[2,1].text(0, 1.02, 'f)', transform=ax[2,1].transAxes, fontsize=14, fontweight='bold')

fig.savefig('/content/drive/MyDrive/mestrado/Dados/chirps/anual2.png', dpi=300)

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Data de início e data de término
data_inicio = datetime(1991, 1, 1)
data_fim = datetime(2021, 12, 31)

# Passo (intervalo) entre as datas (um mês, neste exemplo)
passo = relativedelta(months=1)

# Lista para armazenar as datas
datas = []

# Loop para gerar as datas consecutivas
data_atual = data_inicio
while data_atual <= data_fim:
    datas.append(data_atual)
    data_atual += passo

# Exibir as datas geradas
for data in datas:
    print(data.strftime('%Y-%m-%d'))

data = len(datas)
data

mensal = pd.read_excel('/content/drive/MyDrive/mestrado/Dados/chirps/mensal.xlsx')
mensal

# Criando vetor de ano

# Criando a figura
fig, ax = plt.subplots(nrows=4, ncols=2, figsize=(14, 14), sharex=True)

# FIGURA 1
# Gráfico de linhas
ax[0, 0].plot(datas, mensal['caraí'].values, color='royalblue', label='Caraí (MG)')
ax[0, 0].plot(datas, mensal['carlos_chagas'].values, color='salmon', label='Carlos Chagas (MG)')
ax[0, 0].tick_params(axis='x', labelsize=14, rotation=0)
ax[0, 0].set_yticks([0, 300, 600, 900, 1200, 1500, 1800])
ax[0, 0].xaxis.set_minor_locator(plt.NullLocator())
ax[0, 0].yaxis.set_minor_locator(plt.NullLocator())
ax[0, 0].legend(fontsize=10, loc='upper right')
ax[0, 0].tick_params(axis='y', labelsize=14, rotation=0)
ax[0, 0].set_ylabel('Precipitação (mm/mês)', fontsize=16)
ax[0, 0].text(0, 1.02, 'a)', transform=ax[0,0].transAxes, fontsize=14, fontweight='bold')

#---------------------------------------------------------------------------------------------
#FIGURA 2
# gráfico de barras
ax[0,1].plot(datas, mensal['governador'].values,color ='royalblue', label ='Governador Valadares (MG)')
ax[0,1].plot(datas, mensal['jampruca'].values, color ='salmon', label ='Jampruca (MG)')
ax[0,1].tick_params(axis='x', labelsize=14, rotation=0)
ax[0,1].tick_params(axis='y', labelsize=14, rotation=0)
ax[0,1].set_yticks([0,300,600,900,1200,1500,1800])
ax[0,1].xaxis.set_minor_locator(plt.NullLocator())
ax[0,1].yaxis.set_minor_locator(plt.NullLocator())
ax[0,1].legend(fontsize= 10, loc= 'upper left')
ax[0,1].text(0, 1.02, 'b)', transform=ax[0,1].transAxes, fontsize=14, fontweight='bold')

#---------------------------------------------------------------------------------------------
#FIGURA 3
# gráfico de barras
ax[1,0].plot(datas, mensal['ilheus'].values, color = 'royalblue', label = 'Ilheús (BA)')
ax[1,0].plot(datas, mensal['itabuna'].values, color = 'salmon', label = 'Itabuna (BA)')
ax[1,0].set_yticks([0,300,600,900,1200,1500,1800])
ax[1,0].xaxis.set_minor_locator(plt.NullLocator())
ax[1,0].yaxis.set_minor_locator(plt.NullLocator())
ax[1,0].legend(fontsize= 10, loc= 'upper right')
ax[1,0].tick_params(axis='y', labelsize=14, rotation=0)
ax[1,0].set_ylabel('Precipitação mm/mês', fontsize=16)
ax[1,0].text(0, 1.02, 'c)', transform=ax[1,0].transAxes, fontsize=14, fontweight='bold')

#---------------------------------------------------------------------------------------------
#FIGURA 4
# gráfico de barras
ax[1,1].plot(datas, mensal['jaguaquara'].values, color = 'royalblue', label = 'Jaguaquara (BA)')
ax[1,1].plot(datas, mensal['itacare'].values, color = 'salmon', label = 'Itacaré (BA)')
#ax[1,1].bar(t3, mensal.matuipe, width=barWidth, color = 'salmon', label = 'Matuipe (BA)')
ax[1,1].tick_params(axis='x', labelsize=14, rotation=0)
ax[1,1].tick_params(axis='y', labelsize=14, rotation=0)
ax[1,1].set_yticks([0,300,600,900,1200,1500,1800])
ax[1,1].xaxis.set_minor_locator(plt.NullLocator())
ax[1,1].yaxis.set_minor_locator(plt.NullLocator())
ax[1,1].legend(fontsize= 10, loc= 'upper right')
ax[1,1].text(0, 1.02, 'd)', transform=ax[1,1].transAxes, fontsize=14, fontweight='bold')

#-----------------------------------------------------------------------------------------------
#FIGURA 5
ax[2,0].plot(datas, mensal['gandu'].values, color ='royalblue', label ='Gandu (BA)')
ax[2,0].plot(datas, mensal['medeiros'].values, color = 'salmon', label = 'Medeiros Neto (BA)')
ax[2,0].set_yticks([0,300,600,900,1200,1500,1800])
ax[2,0].xaxis.set_minor_locator(plt.NullLocator())
ax[2,0].yaxis.set_minor_locator(plt.NullLocator())
ax[2,0].legend(fontsize= 10, loc= 'upper right')
ax[2,0].tick_params(axis='x', labelsize=14, rotation=0)
ax[2,0].tick_params(axis='y', labelsize=14, rotation=0)
ax[2,0].set_ylabel('Precipitação mm/mês', fontsize=16)
ax[2,0].text(0, 1.02, 'e)', transform=ax[2,0].transAxes, fontsize=14, fontweight='bold')

#----------------------------------------------------------------------------------------------------
#FIGURA 6
ax[2,1].plot(datas, mensal['salvador'].values,color = 'royalblue', label = 'Salvador (BA)')
ax[2,1].plot(datas, mensal['vitoria'].values, color = 'salmon', label = 'Vitória da Conquista (BA)')
ax[2,1].tick_params(axis='x', labelsize=14, rotation=0)
ax[2,1].tick_params(axis='y', labelsize=14, rotation=0)
ax[2,1].set_yticks([0,300,600,900,1200,1500,1800])
ax[2,1].xaxis.set_minor_locator(plt.NullLocator())
ax[2,1].yaxis.set_minor_locator(plt.NullLocator())
ax[2,1].legend(fontsize= 10, loc= 'upper left')
ax[2,1].text(0, 1.02, 'f)', transform=ax[2,1].transAxes, fontsize=14, fontweight='bold')

#-----------------------------------------------------------------------------------------------
#FIGURA 7
# gráfico de barras
ax[3,0].plot(datas, mensal['unai'].values, color ='royalblue', label = 'Unaí (MG)')
ax[3,0].plot(datas, mensal['montes'].values, color = 'salmon', label = 'Montes Claros (MG)')
ax[3,0].tick_params(axis='x', labelsize=14, rotation=0)
ax[3,0].set_yticks([0,300,600,900,1200,1500,1800])
ax[3,0].xaxis.set_minor_locator(plt.NullLocator())
ax[3,0].yaxis.set_minor_locator(plt.NullLocator())
ax[3,0].legend(fontsize= 10, loc= 'upper right')
ax[3,0].tick_params(axis='y', labelsize=14, rotation=0)
ax[3,0].set_ylabel('Precipitação (mm/mês)', fontsize=16)  # Edita o rótulo do eixo y
ax[3,0].set_xlabel('Anos', fontsize = 16)
ax[3,0].text(0, 1.02, 'g)', transform=ax[3,0].transAxes, fontsize=14, fontweight='bold')

#-----------------------------------------------------------------------------------------------
#FIGURA 8
# gráfico de barras
ax[3,1].plot(datas, mensal['itapetinga'].values, color ='royalblue', label = 'Itapetinga (BA)')
ax[3,1].plot(datas, mensal['porto'].values,color = 'salmon', label = 'Porto Seguro (BA)')
ax[3,1].plot(datas, mensal['matuipe'].values, color = 'limegreen', label = 'Matuípe (BA)')
ax[3,1].tick_params(axis='x', labelsize=14, rotation=0)
ax[3,1].set_yticks([0,300,600,900,1200,1500,1800])
ax[3,1].xaxis.set_minor_locator(plt.NullLocator())
ax[3,1].yaxis.set_minor_locator(plt.NullLocator())
ax[3,1].legend(fontsize= 10, loc= 'upper right')
ax[3,1].tick_params(axis='y', labelsize=14, rotation=0)
ax[3,1].set_xlabel('Anos', fontsize = 16)
ax[3,1].text(0, 1.02, 'h)', transform=ax[3,1].transAxes, fontsize=14, fontweight='bold')

fig.savefig('/content/drive/MyDrive/mestrado/Dados/Figuras/chirps/mensal_2.png', dpi=300)

sazonal = pd.read_excel('/home/cepremg/Documentos/thais/chirps/sazonal_media.xlsx')
sazonal
