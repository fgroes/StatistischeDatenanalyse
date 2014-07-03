"""
Created on Thu Jul 03 10:35:48 2014
@author: f.groestlinger
"""
import numpy as np
import matplotlib.pyplot as plt


def mean(x):
    """
    Mean of array in first dimension
    
    >>> data = np.array([1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4])
    >>> mean(data)
    1.5800000000000001
    """
    N = x.shape[0]
    return np.sum(x) / N
    

def median(x):
    """
    Median of array in first dimension
    
    >>> data = np.array([1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4])
    >>> median(data)
    1.3
    >>> data_new = data[:-3]
    >>> median(data_new)
    1.3
    """
    N = x.shape[0]
    x_sorted = np.sort(x)
    if (N % 2 == 1):
        m = x_sorted[(N + 1) / 2 - 1]
    else:
        m = (x_sorted[N / 2 - 1] + x_sorted[N / 2]) / 2
    return m
    

def quantile(x, a):
    """
    a-quantile of array in first dimension
    
    >>> data = np.array([1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4])
    >>> quantile(data, 0.2)
    0.90000000000000002
    >>> quantile(data, 0.72)
    1.8
    >>> quantile(data, -0.3)
    Traceback (most recent call last):
        ...
    ValueError: a must be in 0.0 <= a <= 1.0
    >>> quantile(data, 1.1)
    Traceback (most recent call last):
        ...
    ValueError: a must be in 0.0 <= a <= 1.0
    """
    if not 0.0 <= a <= 1.0:
        raise ValueError('a must be in 0.0 <= a <= 1.0')
    N = x.shape[0]
    x_sorted = np.sort(x)
    idx = a * N
    if (idx.is_integer()):
        q = (x_sorted[idx - 1] + x_sorted[idx]) / 2
    else:
        idx = np.round(idx + 1.0 / 2)
        q = x_sorted[idx - 1]
    return q
    
    
def variance(x):
    """
    Variance of array in first dimension
        
    >>> data = np.array([1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4])
    >>> variance(data)
    1.5128888888888889
    """
    N = x.shape[0]
    m = mean(x)
    v = np.sum((x - m) ** 2) / (N - 1)
    return v
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()