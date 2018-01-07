import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

ph, ohne, mit = np.genfromtxt('content/values/phasen.txt',unpack=True)
ph/=360
ph*=2*const.pi
def f(x, a, b):
    return a*np.cos(x+b)

parameters, pcov = curve_fit(f, ph, ohne)
errors = np.sqrt(np.diag(pcov))

print('a= ',parameters[0],'pm',errors[0])
print('b= ',parameters[1],'pm',errors[1])
print('Amplitude ohne Gain:',parameters[0]/2000,'pm',errors[0]/2000,'V')
ln = np.linspace(ph[0],ph[len(ph)-1],5000)

plt.plot(ln, f(ln, *parameters), 'r-', label='Fit ohne Störung')
plt.plot(ph,ohne,'bx',label='Werte ohne Störung')
plt.xlabel(r'$\phi/rad$')
plt.ylabel(r'$U/V$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/phasen.pdf')
print('------------------')
