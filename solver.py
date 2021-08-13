# -*- coding: utf-8 -*-
import os.path
import numpy as np
from scipy import linalg.eigh_tridiagonal()


def Einlesen(input_directory):
    """Soll die Inputdatei (schrodinger.inp) auslesen
    und die darin enthaltenen Daten erkennen
    und als jeweiligen Wert ausgeben

    Args:
        input_directory: the directory path where to find schrodinger.int

    Returns:
        the data needed for Solver() function
        or Error message if Input dat. not found or couldnt be read


    """
#  erster Versuch, hat nicht so ganz funtioniert

#   directory = "input_directory"
#   input = np.loadtxt(os.path.join(directory, schrodinger.dat))
#   mass = input[0]  # Masse
#   xMin = input[1, 0]  # minimale x Koordinate
#   xMax = input[1, 1]  # maximale x Koordinate
#   nPoint = input[1, 2]  # anzahl an punkten dazwischen
#   ev1 = input[2, 0]  # first eigenvalue to print
#   ev2 = input[2, 1]  # last eigenvalue to print
#   interpol = input[3],  # hier noch ein default = linear irgendwie einbauen
#   if interpol is not linear, polynomial, cspline:
#       print("Wrong Interpolation type")
#       break
#   points = input[4]  # anzahl der interpolationspunkte
#   xPot = input[5:, 0]  # x koordinate des Potentials
#  yPot = input[5:, 1]  # y koordinate des Potentials

#    return mass, xMin, xMax, nPoin, ev1, ev2, interpol, points, xPot, yPot

# weiteres testen ob vielleicht was ganz anderes geht
# input = open(schrodinger.inp)
# input.readlines()

    Eingang = [line for line in open("os.path.join(input_directory, schrodinger.inp))", "r"]
    mass = [Eingang[0].split() [0]]
    xMin = [Eingang[1].split() [0]]
    xMax = [Eingang[1].split() [1]]
    nPoint = [Eingang[1].split() [2]]
    ev1 = [Eingang[2].split() [0]]
    ev2 = [Eingang[2].split() [1]]
    interpol = [Eingang[3].split() [0]]
    points = [Eingang[5].split() [0]]
    xPot = []
    for aa in range(5, len(Eingang)):
        xPot.append(Eingang[aa].split() [0])
    yPot = []
    for bb in range(5, len(Eingang)):
        yPot.append(Eingang[bb].split() [1])

    return mass, xMin, xMax, nPoin, ev1, ev2, interpol, points, xPot, yPot















def Solver():
    """Soll die vorhin ausgegebenen Daten in die benötigten Werte umrechnen

    """
    potential.dat
    energies.dat
    wavefuncs.dat
    expvalues.dat

    return lösung
