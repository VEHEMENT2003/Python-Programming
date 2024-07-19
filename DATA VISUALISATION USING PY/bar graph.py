# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 08:55:24 2019

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
cities = ['delhi','mumbai','banglore','solapur','kolhapur']
population = [958977547,987798767,978856767,98654566,98877865]
plt.bar(cities,population,color = ['red','b','g','black','y'])
plt.xlabel('cities')
plt.ylabel('population')
plt.show()