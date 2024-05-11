# radiationpat.py
import numpy as np
from scipy.signal import find_peaks

def radiationpat(SNR, theta):
    Pn = 10**(-SNR/10)
    th = np.arange(0, 180, 0.1)
    x = np.arange(0, 1800)

    A = np.zeros((24, 6), dtype=complex)
    for k in range(24):
        for i in range(6):
            A[k, i] = np.exp(1j * (k - 1) * np.pi * np.cos(theta[0, i] * np.pi / 180))

    atheta = np.zeros((24, len(th)), dtype=complex)
    for i in range(24):
        atheta[i, 0:len(th)] = np.exp(1j * (i - 1) * np.pi * np.cos(th * np.pi / 180))

    w_nsb = np.dot(A, np.linalg.inv(np.dot(A.T, A) + Pn * np.diag(np.ones(6))))
    w_nsb1 = w_nsb[0:24, 0]

    AF = np.dot(w_nsb1.T, atheta)
    AF /= np.max(np.abs(AF))

    P, _ = find_peaks(np.abs(AF))
    P = np.sort(P)
    sidelobes = P[0:len(P) - 1]

    while np.max(sidelobes) > 0.1:
        P, _ = find_peaks(np.abs(AF))
        th_peaks = P / 10  
        theta1 = th_peaks
        while theta1[0] > theta[0, 0] + 5 or theta1[0] < theta[0, 0] - 5:
            theta1 = np.roll(theta1, -1)
        theta1[1:6] = np.sort(theta1[1:6])
        A1 = np.zeros((24, len(theta1)), dtype=complex)
        for k in range(24):
            for i in range(len(theta1)):
                A1[k, i] = np.exp(1j * (k - 1) * np.pi * np.cos(theta1[i] * np.pi / 180))

        w_nsb = np.dot(A1, np.linalg.inv(np.dot(A1.T, A1) + Pn * np.diag(np.ones(len(theta1)))))
        w_nsb1 = w_nsb[0:24, 0]
        AF = np.dot(w_nsb1.T, atheta)
        AF = np.abs(AF) / np.max(np.abs(AF))
        P, _ = find_peaks(np.abs(AF))
        P = np.sort(P)
        sidelobes = P[0:len(P) - 1]

    P, _ = find_peaks(np.abs(AF))
    th_peaks = P / 10
    theta1 = th_peaks

    while theta1[0] > theta[0, 0] + 5 or theta1[0] < theta[0, 0] - 5:
        theta1 = np.roll(theta1, -1)

    angleofmax = theta1[0]
    PointsofZeros = np.r_[True, AF[1:] < AF[:-1]] & np.r_[AF[:-1] < AF[1:], True]
    mins = x[PointsofZeros] / 10

    while mins[0] > np.min(theta[0, 1:6]) + 5 or mins[0] < np.min(theta[0, 1:6]) - 5:
        mins = np.roll(mins, -1)

    angleofzeros = mins[0:5]
    SLL = -20 * np.log10(np.max(P) / np.max(sidelobes))

    return AF, angleofzeros, angleofmax, SLL
