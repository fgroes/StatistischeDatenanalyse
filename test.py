"""
Created on Thu Jul 03 16:05:57 2014
@author: f.groestlinger
"""
import numpy as np
import matplotlib.pyplot as plt
#import scipy as sp


if __name__ == '__main__':
    import statana.basicstats as bs
    import statana.data as data
    print(data.sleep_extension.describe())
    x1 = np.linspace(0, 5, 100)
    f1 = bs.empir_cum_dist(x1, data.sleep_extension['extension factor'])
    x2 = np.linspace(70.0, 140.0, 100)
    bins = np.r_[74.5:134.5 + 1:5.0]
    f2 = bs.cum_dist(x2, data.chicks['weight in g'], bins)
    plt.subplot(2, 1, 1)
    plt.plot(x1, f1, 'r-')
    plt.subplot(2, 1, 2)
    plt.plot(x2, f2, 'r-')
    plt.show()