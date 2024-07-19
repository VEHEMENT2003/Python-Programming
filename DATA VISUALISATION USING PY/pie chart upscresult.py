# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:44:14 2019

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
upscresult = [35,19,25,18,61]
years = ['2015','2016','2017','2018','2019']
plt.pie(upscresult, labels=years,autopct = "%1.1f%%")