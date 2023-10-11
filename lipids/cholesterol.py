# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:11:54 2022

@author: Fabrizio
"""

import matplotlib.pyplot as plt

def plot_happiness():
    age = [6, 14, 15, 16, 17, 21, 23, 26, 26.1, 38, 41, 41.1, 41.2, 43, 44, 45, 45.1]
    year = [1977, 1983, 1991, 1992, 1993, 1994, 1998, 2003, 2003.1, 2015, 2018, 2018.1, 2018.2, 2020, 2021, 2022, 2022.1, 2023]
    happiness = [0.80, 0.80, 0.84, 0.99, 1.0, 0.91, 0, -0.64, -0.35, -0.8, -0.40, -0.50, -0.58, -0.38, 0.53, 0.72, 0.65, 0.51]
    plt.title("happiness over time")
    plt.plot(year, happiness)
    plt.ylim([-1.2, 1.2])
    plt.xlim([1977, 2023])
    plt.xlabel('time')
    plt.ylabel('happiness')
    plt.show()
    
def plot_cholesterol():
    age = [6, 14, 15, 16, 17, 21, 23, 26, 26.1, 38, 41, 41.1, 41.2, 43, 44, 45, 45.2, 45.3, 45.4, 45.5, 45.7, 45.8]
    year = [1977, 2005, 2007, 2013, 2015, 2019, 2021, 2022, 2022.6, 2023.1, 2023.2, 2023.3, 2023.6, 2023.8]
    total_cholesterol = [5.67, 5.67, 5.67, 6.77, 7.78, 7.10, 6.24, 6.5, 6.1, 5.54, 5.84, 5.85, 5.85, 6.22]
    triglycerids = [1.4, 1.4, 1.4, 2.15, 2.99, 1.92, 2.38, 1.49, 1.83, 1.35, 1.96, 1.96, 1.67, 1.57]
    ldl_cholesterol = [3.58, 3.58, 3.58, 4.47, 5.1, 5.36, 4.24, 4.83, 3.99, 3.61, 3.68, 3.78, 3.92, 4.21]
# 2022.3,     , 45.1  7.6,, 3.6, 4.33
    plt.plot(year, total_cholesterol)
    plt.plot(year, ldl_cholesterol)
    plt.xlabel('time')
    plt.plot(year, triglycerids)
    plt.plot([1977, 2022.6], [5.2, 5.2], color='cornflowerblue', linewidth='0.3')
    plt.plot([1977, 2022.6], [1.83, 1.83], color='g', linewidth='0.3')
    plt.plot([1977, 2022.6], [4.0, 4.0], color='orange', linewidth='0.3')
    plt.legend(["total cholesterol", "ldl cholesterol", "triglycerids"])
    plt.title("lipid profile")
    plt.show()

# plot_happiness()   
plot_cholesterol() 

