"""
Created on Thu Jul 03 10:35:48 2014
@author: f.groestlinger
"""
import numpy as np
import matplotlib.pyplot as plt


def empir_cum_dist(x, series):
    """
    empirical cummulative distribution function
    
    >>> import pandas as pd
    >>> sleep_extension = pd.DataFrame(data={'extension factor': [1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4]})
    >>> empir_cum_dist([1.3, 1.9], sleep_extension['extension factor'])
    [0.6, 0.8]
    """
    series_sorted = series.copy()
    series_sorted.sort()
    try:
        f = [float((series_sorted <= i).sum()) / series_sorted.size 
            for i in np.asarray(x)]
    except TypeError:
        f = (float(series_sorted <= x).sum()) / series_sorted.size
    return f
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)