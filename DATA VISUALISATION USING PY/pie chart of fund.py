# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:44:14 2019

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
contri = [17,9,9.9,12,15]
houses = ['shivraj','rushikesh','dhiraj','vrushabh','vj2003']
plt.pie(contri, labels=houses,autopct = "%1.1f%%")