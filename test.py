"""
Created on Thu Jul 03 16:05:57 2014
@author: f.groestlinger
"""
import numpy as np
import matplotlib.pyplot as plt
#import scipy as sp


if __name__ == '__main__':
    import statana.basicstats as bs
    import data.data as data
    print(data.sleep_extension.describe())
    x = np.linspace(0, 5, 1000)
    f = bs.empir_cum_dist(x, data.sleep_extension['extension factor'])
    plt.plot(x, f, 'r-')
    plt.show()