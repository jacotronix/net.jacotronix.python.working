'''
Created on 4 Dec 2012

@author: Jamie
'''

import matplotlib
from pylab import *

n = 256
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plot(X,C),plot(X,S)

#savefig("./exercice.png",dpi=72)
show()
