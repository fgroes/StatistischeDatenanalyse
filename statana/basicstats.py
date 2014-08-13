"""
Created on Thu Jul 03 10:35:48 2014
@author: f.groestlinger
"""
import numpy as np
import pandas as pd


def empir_cum_dist(x, series):
    """
    empirical cummulative distribution function
    
    >>> empir_cum_dist(1.05, sleep_extension['extension factor'])
    0.3
    >>> empir_cum_dist([1.3, 1.9], sleep_extension['extension factor'])
    [0.6, 0.8]
    """
    series_sorted = series.copy()
    series_sorted.sort()
    try:
        f = [float((series_sorted <= i).sum()) / series_sorted.size 
            for i in np.asarray(x)]
    except TypeError:
        f = float((series_sorted <= x).sum()) / series_sorted.size
    return f
    
    
def median_abs_dev(x):
    """
    median absolute deviation
    
    >>> median_abs_dev(sleep_extension['extension factor'])
    0.40000000000000002
    """
    return (x - x.quantile()).apply(np.abs).quantile()   
    
    
def _cum_dist_scalar(x, rel_freq, bins):
    try: 
        j = (bins <= x).sum()
        f1 = np.sum(rel_freq[:j - 1])
        f2 = f1 + rel_freq[j - 1]
        f = f1 + (f2 - f1) / (bins[j] - bins[j - 1]) * (x - bins[j - 1])
    except IndexError:
        f = 1.0
    return f
    
    
def cum_dist(x, series, bins):
    """
    cummulative distribution function
    
    >>> cum_dist([90.0, 110.0, 134.5], chicks['weight in g'], \
np.r_[74.5:134.5 + 1:5.0])
    [0.058000000000000003, 0.64700000000000002, 1.0]
    """
    freq, bins = np.histogram(series, bins=bins)
    rel_freq = freq.astype(np.float) / series.size
    try:
        f = [_cum_dist_scalar(i, rel_freq, bins) for i in x]
    except TypeError:
        f = _cum_dist_scalar(x, rel_freq, bins)
    return f
           
    
if __name__ == '__main__':
    import doctest
    import data
    g = {'sleep_extension': data.sleep_extension, 'chicks': data.chicks}
    doctest.testmod(verbose=True, extraglobs=g)