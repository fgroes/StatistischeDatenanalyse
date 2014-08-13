"""
Created on Wed Aug 13 20:20:05 2014
@author: fritz
"""
import numpy as np
#import matplotlib.pyplot as plt
#import scipy as sp
import pandas as pd


sleep_extension = pd.DataFrame(data={
    'extension factor': [1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4]})
    

mendel_data = np.array([[45, 27, 24, 19, 32, 26, 88, 22, 28, 25],
                 [12, 8, 7, 10, 11, 6, 24, 10, 6, 7]]).T
mendel_plants = pd.DataFrame(data=mendel_data, columns=['round', 'edgy'])


if __name__ == '__main__':
    print(sleep_extension.describe())
    print(mendel_plants.describe())