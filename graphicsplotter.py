import os.path
from matplotlib import pyplot as plt
import numpy as np


projectname = "firsttest"


def read_in (projectname):

    #unpacking energies
    energies = np.loadtxt(os.path.join("output/data_submitted", projectname, "energies.dat"))
    #unpacking Potential and x_values
    discrpot = np.loadtxt(os.path.join("output/data_submitted", projectname, "discrpot.dat"))

    x_values = discrpot[:,0]
    discropt_values =  discrpot[:,1]

    #unpacking wfuncs
    wfuncs = np.loadtxt(os.path.join("output/data_submitted", projectname, "wfuncs.dat"))

    wfuncs_values = wfuncs[:,1:]


   return energies, x_values, discropt_values, wfuncs_values




def plotting(energies, x_values, discropt_values, wfuncs_values, factor=1, factor1=1, x_bound=None , y_max=None ):


    plt.figure(figsize=(15, 7.5), dpi=80)
    plt.subplot(1,2,1)

    #plotting Potential:
    plt.plot(x_values, discropt_values)
    #plotting Wfuncs:
    plt.plot(x_values, wfuncs_values*factor + energies)
    #x_range:
    if x_bound is None:
        plt.xlim(x_values.min()*1.1,x_values.max()*1.1)
    else:
        plt.xlim(-x_bound,x_bound)
    #y_range:
    if y_max is None:
        plt.ylim((wfuncs_values*factor +energies).min()-0.5, (wfuncs_values*factor +energies).max()*1.1)
    else:
        plt.ylim((wfuncs_values*factor +energies).min()-0.5, y_max)

    plt.subplot(1,2,2)

    #plotting Potential:
    plt.plot(x_values, discropt_values)
    #plotting Wfuncs:
    plt.plot(x_values, np.abs(wfuncs_values)**2 *factor1 + energies)
    #x_range:
    if x_bound is None:
        plt.xlim(x_values.min()*1.1,x_values.max()*1.1)
    else:
        plt.xlim(-x_bound,x_bound)
    #y_range:
    if y_max is None:
        plt.ylim((np.abs(wfuncs_values)**2 *factor1 + energies).min()-0.5, (np.abs(wfuncs_values)**2 *factor1 + energies).max()*1.1)
    else:
        plt.ylim((np.abs(wfuncs_values)**2 *factor1 + energies).min()-0.5, y_max)

    plt.show()