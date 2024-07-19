# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:28:29 2019

@author: Dell
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.,10,0.1)
a = np.cos(x)
b = np.sin(x)
plt.plot(x,a,'r',linestyle= 'dotted')
plt.plot(x,b,'b',linestyle = 'dashed')
plt.xlabel('shivraj values')
plt.ylabel('rushikesh values')
plt.show()
           