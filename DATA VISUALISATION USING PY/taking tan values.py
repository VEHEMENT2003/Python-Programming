# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:18:42 2019

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
a = np.arange(1,40,0.25)
b = np.tan(a)
plt.plot(a,b)
plt.plot(a,b,'b',linestyle= 'dashed')
plt.xlabel('dhiraj values')
plt.ylabel('vrushabh values')

