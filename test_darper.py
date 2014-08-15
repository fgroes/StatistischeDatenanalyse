"""
Created on Fri Aug 15 22:49:53 2014
@author: fritz
"""
from statana.data import darper
from statana.basicstats import lin_regression


if __name__ == '__main__':
    print(darper.describe())
    print(lin_regression(darper['moistsure'], darper['density']))
