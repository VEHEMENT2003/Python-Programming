# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 08:55:24 2019

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
years = ['2016','2017','2018','2019','2020']
torturerate = [30,40,50,90,25]
plt.bar(years,torturerate,color = ['b','g','y','red','black'])
plt.xlabel('years')
plt.ylabel('torture ratein %')
plt.show()