# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:08:23 2019

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
val = [[5.,25.,45.,20.],[4.,23.,48.,17.],[6.,22.,47.,19.]]
x = np.arange(4)
plt.bar(x+0.00,val[0],color = 'g',width = 0.25)
plt.bar(x+0.25,val[1],color = 'b',width = 0.25)
plt.bar(x+0.50,val[2],color = 'red',width = 0.25)
plt.xlabel('torture ratein %of\n ppl, adm,vppl')
plt.ylabel('torture ratein ')
plt.show()