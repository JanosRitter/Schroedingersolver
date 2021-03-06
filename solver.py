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
        print("unvalid type, please enter either linear,"
              "polynomial or cspline")

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
    """Soll die vorhin ausgegebenen Daten in die ben??tigten Werte umrechnen

    """
    Npoint = float("".join(nPoint))
    Abstand = -(xkoords[0] - xkoords[-1]) / Npoint
    Mass = float("".join(mass))
    abk??rzung = 1 / (Mass * Abstand ** 2)
# rechner der energien und wellenfunktionen
    diagonale = np.array([abk??rzung + ii for ii in ykoords])
    off_diagonale = np.array([-abk??rzung / 2] * (len(ykoords)-1))
    energie, wavefct = scipy.linalg.eigh_tridiagonal(diagonale, off_diagonale)
# normierung der Wellenfunktionen
    wavefunc = wavefct.T
    for index, wfunc in enumerate(wavefunc):
        wavefunc[index, :] = wfunc / (np.sqrt(Abstand * np.sum(wfunc ** 2)))
# Berechnung von Erwartungswerten
    for wfunc in wavefunc:
        expvalues = np.append(expvalues,
                              [Abstand * np.sum(wfunc ** 2 * xkoords ** 2)],
                              axis=0)

    return energie, wavefunc, expvalues
