import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

r,U = np.genfromtxt('content/values/diode.txt',unpack=True)
r/=100
def f(x, a):
    return a/((x)**2)

parameters, pcov = curve_fit(f, r, U)
errors = np.sqrt(np.diag(pcov))

print('a= ',parameters[0],'pm',errors[0])
print('Amplitude ohne Gain:',parameters[0]/40,'pm',errors[0]/40,'V')
ln = np.linspace(r[0],r[len(r)-1],5000)

plt.plot(ln, f(ln, *parameters), 'r-', label='Fit')
plt.plot(r,U,'bx',label='Werte')
plt.xlabel(r'$r/m$')
plt.ylabel(r'$U/V$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/diode.pdf')
print('-------------------')
