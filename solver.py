# -*- coding: utf-8 -*-
import os.path
import numpy as np
import scipy
from scipy.interpolate import interp1d, KroghInterpolator, CubicSpline


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

    Eingang = [line for line in open("os.path.join(input_directory, schrodinger.inp)", "r")]
    mass = [Eingang[0].split()[0]]
    xMin = [Eingang[1].split()[0]]
    xMax = [Eingang[1].split()[1]]
    nPoint = [Eingang[1].split()[2]]
    ev1 = [Eingang[2].split()[0]]
    ev2 = [Eingang[2].split()[1]]
    interpol = [Eingang[3].split()[0]]
    points = [Eingang[5].split()[0]]
    xPot = []
    for aa in range(5, len(Eingang)):
        xPot.append(Eingang[aa].split()[0])
    yPot = []
    for bb in range(5, len(Eingang)):
        yPot.append(Eingang[bb].split()[1])

    return mass, xMin, xMax, nPoint, ev1, ev2, interpol, points, xPot, yPot


def Interpolation(xPot, yPot, xMin, xMax, nPoint, Typ, ):
    """Checks the interpolatioin type and interpolates the potential.
    creates the potential.dat for plotting

    Args:
        xPot: given x Koordinates of the Potential
        yPot: given y Koordinates of the Potential
        xMin: minimal x koordinate
        xMax: maximal x koordinate
        nPoint: Number of Points for the potential.dat
        Typ: type of interpolation to be used

    Returns:
        xkoords: the x koordinates of the potential
        ykoords: the interpolates y koordinates for the potential
        or Error Msg if Typ is not linear, cspline or polynomial
    """
    if Typ not == "linear", "polynomial", "cspline":
        print("unvalid type, please enter either linear, polynomial or cspline")

    Xmin = float("".join(xMin))
    Xmin = float("".join(xMax))
    Npoint = float("".join(nPoint))
    # converted list into string into float, because linspace wont work otherwise
    xkoords = np.linspace(Xmin, Xmax, Npoint)

    Xpot = [float(ii) for ii in xPot]
    Ypot = [float(ii) for ii in yPot]

    if Typ == "linear":
        interpolfunc = scipy.interpolate.interp1d(Xpot, Ypot)

    if Typ == "polynomial":
        interpolfunc = scipy.interpolate.CubicSpline(Xpot, Ypot)

    if Typ == "cspline":
        interpolfunc = scipy.interpolate.KroghInterpolator(Xpot, Ypot)

    ykoords = interpolfunc(xkoords)

    return xkoords, ykoords


def Solver():
    """Soll die vorhin ausgegebenen Daten in die benötigten Werte umrechnen

    """
    Npoint = float("".join(nPoint))
    Abstand = (xkoords[0] - xkoords[-1]) / Npoint
    Mass = float("".join(mass))
    abkürzung = 1 / (Mass * Abstand ** 2)

    diagonale = np.array([abkürzung + ii for ii in ykoords])
    off_diagonale = np.array([-abkürzung / 2] * (len(ykoords)-1))
    energie, wavefct = scipy.linalg.eigh_tridiagonal(diagonale, off_diagonale)


    return energie, wavefct
