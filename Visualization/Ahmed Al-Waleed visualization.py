# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:19:28 2022

@author: ahmed
"""

import pandas as pd
import matplotlib.pyplot as plt



covidDf = pd.read_excel("C:/Users/ahmed/Desktop/finalDataset_test.xlsx")

Cumulative_tests = covidDf['Cumulative_recovered_cases']
Cumulative_recovered_cases = covidDf['Cumulative_tests']
plt.figure(figsize=(20,20))
plt.scatter(Cumulative_tests, Cumulative_recovered_cases, edgecolors='r')
plt.xlabel('Cumulative_recovered_cases')
plt.ylabel('Cumulative_tests')
plt.title('Relation between Cumulative_recovered_cases and Cumulative_tests ')
plt.show()

plt.ylim(0, 200000)
plt.xlim(0,10000)