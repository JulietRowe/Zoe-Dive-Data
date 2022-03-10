# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:00:22 2021

@author: julie
"""


from IPython import get_ipython
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import seaborn as sns
from scipy import stats
import statsmodels.stats.api as sms
import matplotlib.patches as mpatches

get_ipython().magic('reset -f')
get_ipython().magic('clear')

col_names1 = ['DateTime', 'Depth']
col_names2 = ['Real time', 'Call Type']

# #2020-09-05
# File1 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File1.csv', header = 0, usecols = col_names1)
# File1 = File1.dropna()
# File1 = File1.astype(str)

# File2 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File2.csv', header = 0, usecols = col_names2)
# File2 = File2.dropna()
# File2 = File2.astype(str)

# File2['Real time'] = File2['Real time'].apply(lambda x: "2020-09-05 " + x)
# File2['DateTime'] = File2['Real time'] 

# FileOUT = File2.merge(File1, on = 'DateTime')

# #2020-09-03
# File3 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File3.csv', header = 0, usecols = col_names1)
# File3 = File3.dropna()
# File3 = File3.astype(str)

# File4 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File4.csv', header = 0, usecols = col_names2)
# File4 = File4.dropna()
# File4 = File4.astype(str)

# File4['Real time'] = File4['Real time'].apply(lambda x: "2020-09-03 " + x)
# File4['DateTime'] = File4['Real time'] 

# File0903 = File4.merge(File3, on = 'DateTime')

# #2020-09-07
# File5 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File5.csv', header = 0, usecols = col_names1)
# File5 = File5.dropna()
# File5 = File5.astype(str)

# File6 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File6.csv', header = 0, usecols = col_names2)
# File6 = File6.dropna()
# File6 = File6.astype(str)

# File6['Real time'] = File6['Real time'].apply(lambda x: "2020-09-07 " + x)
# File6['DateTime'] = File6['Real time'] 

# File0907 = File6.merge(File5, on = 'DateTime')

# #2020-09-08
# File7 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File7.csv', header = 0, usecols = col_names1)
# File7 = File7.dropna()
# File7 = File7.astype(str)

# File8 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File8.csv', header = 0, usecols = col_names2)
# File8 = File8.dropna()
# File8 = File8.astype(str)

# File8['Real time'] = File8['Real time'].apply(lambda x: "2020-09-08 " + x)
# File8['DateTime'] = File8['Real time'] 

# File0908 = File8.merge(File7, on = 'DateTime')

# #Saveing Data
# selectfolder = sg.popup_get_folder('Select a folder to save Zoes life', keep_on_top = True)

# with pd.ExcelWriter(selectfolder + '/Call depth time series2.xlsx') as writer:
#     FileOUT.to_excel(writer, sheet_name = '2020-09-05')
#     File0903.to_excel(writer, sheet_name = '2020-09-03')
#     File0907.to_excel(writer, sheet_name = '2020-09-07')
#     File0908.to_excel(writer, sheet_name = '2020-09-08')


#05
DataGraph = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File1.csv', header = 0)
# DataGraph = DataGraph.dropna()
DataGraph['DateTime'] = pd.to_datetime(DataGraph['DateTime'])
DataGraph['Droplet'] = DataGraph['Droplet'].dropna()
DataGraph['Cry'] = DataGraph['Cry'].dropna()
DataGraph[['Depth','Droplet','Cry']] = DataGraph[['Depth', 'Droplet', 'Cry']]*-1

#03
DataGraph2 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File3.csv', header = 0)
# DataGraph = DataGraph.dropna()
DataGraph2['DateTime'] = pd.to_datetime(DataGraph2['DateTime'])
DataGraph2['Droplet'] = DataGraph2['Droplet'].dropna()
DataGraph2['Cry'] = DataGraph2['Cry'].dropna()
DataGraph2[['Depth','Droplet','Cry']] = DataGraph2[['Depth', 'Droplet', 'Cry']]*-1

#07
DataGraph3 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File5.csv', header = 0)
# DataGraph = DataGraph.dropna()
DataGraph3['DateTime'] = pd.to_datetime(DataGraph3['DateTime'])
DataGraph3['Droplet'] = DataGraph3['Droplet'].dropna()
DataGraph3['Cry'] = DataGraph3['Cry'].dropna()
DataGraph3[['Depth','Droplet','Cry']] = DataGraph3[['Depth', 'Droplet', 'Cry']]*-1

#08
DataGraph4 = pd.read_csv('C:/Users/julie/Year 4 Kin/Zoe Dive Data/File7.csv', header = 0)
# DataGraph = DataGraph.dropna()
DataGraph4['DateTime'] = pd.to_datetime(DataGraph4['DateTime'])
DataGraph4['Cry'] = DataGraph4['Cry'].dropna()
DataGraph4[['Depth','Droplet','Cry']] = DataGraph4[['Depth', 'Droplet', 'Cry']]*-1


fig6, axes = plt.subplots(3, figsize =(20,20), dpi = 300)
DataGraph.plot(x = 'DateTime', y = 'Depth', legend = False, zorder = 1, ax = axes[1], color = 'black', title = '2020/09/05')
DataGraph.plot.scatter(x='DateTime', y='Droplet', c='r', ax = axes[1], s = 125)
DataGraph.plot.scatter(x='DateTime', y='Cry', c='b', ax = axes[1], zorder = 2, s = 125)

DataGraph2.plot(x = 'DateTime', y = 'Depth', legend = False, zorder = 1, ax = axes[0], color = 'black', title = '2020/09/03')
DataGraph2.plot.scatter(x='DateTime', y='Droplet', c='r', ax = axes[0], s = 125)
DataGraph2.plot.scatter(x='DateTime', y='Cry', c='b', ax = axes[0], zorder = 2, s = 125)

DataGraph3.plot(x = 'DateTime', y = 'Depth', legend = False, zorder = 1, ax = axes[2], color = 'black', title = '2020/09/07')
DataGraph3.plot.scatter(x='DateTime', y='Droplet', c='r', ax = axes[2], s= 125)
DataGraph3.plot.scatter(x='DateTime', y='Cry', c='b', ax = axes[2], zorder = 2, s = 125)
red_patch = mpatches.Patch(color='red', label='Droplet')
blue_patch = mpatches.Patch(color='blue', label='Cry')
plt.legend(handles=[red_patch, blue_patch], frameon = False)

# DataGraph4.plot(x = 'DateTime', y = 'Depth', legend = False, zorder = 1, ax = axes[3], color = 'black', title = '2020/09/08')
# DataGraph4.plot.scatter(x='DateTime', y='Cry', c='b', ax = axes[3], s = 125)
# red_patch = mpatches.Patch(color='red', label='Droplet')
# blue_patch = mpatches.Patch(color='blue', label='Cry')
# plt.legend(handles=[red_patch, blue_patch], frameon = False)

for ax in axes.flat:
    ax.set_ylabel('Depth (m)', fontsize = 12)
    ax.set_xlabel('Time', fontsize = 12)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.title.set_size(12)
    ax.set_ylim(-20,280)
    ax.invert_yaxis()

    
selectfolder = sg.popup_get_folder('Select a folder to save all plots', keep_on_top = True)
fig6.savefig(selectfolder + '/CroppedWhale.png', bbox_inches='tight') 
