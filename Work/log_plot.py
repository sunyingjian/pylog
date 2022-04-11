import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def make_log_plot(logs):
    logs = logs.sort_values(by='Depth')

    ztop = logs.Depth.min()
    zbot = logs.Depth.max()

    f,ax = plt.subplots(nrows=1,ncols=logs.shape[1]-1,figsize=(8,12))

    colors = 'bgrcmykw'
    indexs = 0
    for c in logs:
        if c=='Depth':
            continue
        ax[indexs].plot(logs[c],logs.Depth,'-',color=colors[indexs])
        indexs+=1

    for i in range(len(ax)):
        ax[i].set_ylim(ztop,zbot)
        ax[i].invert_yaxis()
        ax[i].grid()
        ax[i].locator_params(axis='x',nbins=3)

    col_name = logs.columns.values.tolist()#获取列名
    for i in range(1,len(col_name)):
        ax[i-1].set_xlabel(col_name[i])
        ax[i-1].set_xlim(logs[col_name[i]].min(),logs[col_name[i]].max())

    for i in range(1,len(col_name)):
        ax[i-1].set_yticklabels([])