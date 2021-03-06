"""
Created on Wed Aug 13 20:20:05 2014
@author: fritz
"""
import os
import numpy as np
#import matplotlib.pyplot as plt
#import scipy as sp
import pandas as pd


sleep_extension = pd.DataFrame(data={
    'extension factor': [1.2, 2.4, 1.3, 1.3, 0.0, 1.0, 1.8, 0.8, 4.6, 1.4]})
    

mendel_data = np.array([[45, 27, 24, 19, 32, 26, 88, 22, 28, 25],
                 [12, 8, 7, 10, 11, 6, 24, 10, 6, 7]]).T
mendel_plants = pd.DataFrame(data=mendel_data, columns=['round', 'edgy'])

chicks = pd.DataFrame(data={
    'weight':
        [107, 117, 105, 106, 114, 105, 113, 88, 119, 116,
         108, 98, 104, 126, 102, 100, 120, 121, 87, 110,
         111, 114, 121, 114, 104, 94, 101, 94, 95, 114,
         101, 82, 111, 108, 100, 109, 92, 96, 108, 108,
         97, 92, 112, 105, 112, 100, 108, 105, 97, 119,
         113, 102, 103, 100, 94, 102, 104, 110, 127, 102,
         109, 100, 76, 101, 95, 96, 118, 91, 118, 107,
         105, 112, 92, 99, 118, 100, 130, 112, 110, 103,
         116, 115, 96, 125, 97, 114, 111, 101, 101, 90,
         122, 106, 109, 116, 103, 134, 86, 124, 107, 107]})
         
         
waterfalls = pd.DataFrame(data={
    'name': ['Lower Yellowstone',  'Yosemite', 'Canadian Niagara', 
        'American Niagara', 'Upper Yellowstone', 'Gullfoss (Lower)',
        'Firehole', 'Godafoss', 'Gullfoss (Upper)', 'Fort Greeley'], 
    'height': [95, 72, 50, 53, 35, 27, 13.4, 10.9, 7.5, 5.2],
    'frequency': [5.6, 4.0, 6.2, 8.1, 8.7, 6.2, 19, 21, 39, 40]})


darper = pd.DataFrame(data={
    'moistsure': [4.7, 5.0, 5.2, 5.2, 5.9, 4.7, 5.9, 5.2, 5.3, 5.9, 5.6, 5.0],
    'density': [3, 3, 4, 5, 10, 2, 9, 3, 7, 6, 6, 4]})
    

file_name = os.path.join(os.path.split(__file__)[0], 'iris.txt')
print(file_name)
with open(file_name) as fid:
    iris = pd.read_table(fid, sep=';')


if __name__ == '__main__':
    print(sleep_extension.describe())
    print(mendel_plants.describe())
    print(chicks.describe())
    print(waterfalls.describe())
    print(darper.describe())
    print(iris.describe())