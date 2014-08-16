"""
Created on Fri Aug 15 23:24:59 2014
@author: fritz
"""
import pandas as pd
from statana.data import iris


if __name__ == '__main__':
    print(iris.describe())
    pd.scatter_matrix(iris)