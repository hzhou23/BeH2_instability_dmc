#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import uncertainties
from uncertainties import ufloat
from uncertainties import unumpy
from uncertainties import ufloat_fromstr
from scipy.optimize import curve_fit
import re
import string

styles = {
'2enoTmoves' :{'label':'2e- ccECP no Tmoves', 'color':'#ff9933', 'linestyle':'--', 'dashes': (3,1), 'marker':'s', 'markersize':6, 'markeredgecolor':'#000000', 'markeredgewidth':0.5},
'2eTmoves':{'label':'2e- ccECP Tmoves','color':'#009933', 'linestyle':'--', 'dashes': (6,1), 'marker':'o', 'markersize':6, 'markeredgecolor':'#000000', 'markeredgewidth':0.5},
}


def init():
    font   = {'family' : 'serif', 'size': 20}
    lines  = {'linewidth': 2.5}
    axes   = {'linewidth': 2.0}    # border width
    tick   = {'major.size': 2, 'major.width':2}
    legend = {'frameon':False, 'fontsize':16.0, 'handlelength':2.20, 'labelspacing':0.40, 'handletextpad':0.4, 'loc':'best'}

    mpl.rc('font',**font)
    mpl.rc('lines',**lines)
    mpl.rc('axes',**axes)
    mpl.rc('xtick',**tick)
    mpl.rc('ytick',**tick)
    mpl.rc('legend',**legend)

    mpl.rcParams['text.usetex'] = True
    mpl.rcParams.update({'figure.autolayout':True})
    fig = plt.figure()
    fig.set_size_inches(7.04, 5.28)   # Default 6.4, 4.8
    ax1 = fig.add_subplot(111) # row, column, nth plot
    #gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1])
    #ax1 = plt.subplot(gs[0])
    #ax2 = plt.subplot(gs[1], sharex = ax1)
    return fig, ax1

##########################DATA#######################

timestep = [0.001, 0.002, 0.003, 0.005, 0.008, 0.01, 0.02, 0.045, 0.05, 0.055, 0.07, 0.09, 0.1, 0.2, 0.3, 0.5]
energy = [-2.2454, -2.2448, -2.2448, -2.2438, -2.2451, -2.2456, -2.2464, -2.2464, -2.2464, -2.2469, -2.2476, -2.2481, -2.2472, -2.2525,-2.2519, -2.2568]
err =[0.0006,0.0009,0.0005,0.0003,0.0005,0.0005,0.0009,0.0004,0.0006,0.0004,0.0008,0.0004,0.0007,0.001,0.0006,0.0008]

#########################Plot#########################

fig, ax1 = init()
ax1.tick_params(direction='in', length=8, width=2, which='major', pad=10)
ax1.tick_params(direction='in', length=4, width=1, which='minor', pad=10)
ax1.set_ylabel('Energy and Errorbar (Hatree)')
ax1.set_xlabel('$Timestep (Hatree$^{-1}$)$')
tick_spacing = 1.0
ax1.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax1.set_ylim(-2.2600, -2.2400)

ax1.errorbar(timestep, energy, yerr=err, **styles['2enoTmoves'])

ax1.axhline(y=0.0, ls='--', lw=1.0, color='#ff0000', alpha=0.5)
ax1.legend(ncol=1)
ax1.grid(b=None, which='major', axis='both', alpha=0.2)          
plt.savefig('2eccECPnoTmoves.pdf')
