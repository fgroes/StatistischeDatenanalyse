"""
Created on Thu Jul 03 16:05:57 2014
@author: f.groestlinger
"""
import numpy as np
import matplotlib.pyplot as plt
#import scipy as sp


if __name__ == '__main__':
    import statana.basicstats as bs
    data = np.array([1, 2, 3])
    print(bs.mean(data))