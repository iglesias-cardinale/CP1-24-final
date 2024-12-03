'''This module contains all of the functions necessary to complete 
the Final Exam for Computational Physics 1, 2024.'''

import os
import numpy as np

def fahrenheit_to_kelvin(fahrenheit):
    '''This function converts a given temperature in Degrees Fahrenheit 
    to the equivalent absolute temperature in Kelvin.
    
    Parameters:
        -fahrenheit: Degrees Fahrenheit, to be converted
        
    Returns:
        -kelvin: Equivalent temperature in Kelvin
    '''
    kelvin = (fahrenheit-32)*5/9 + 273.15

    return kelvin

def get_temp(path):
    '''Reads the temperature of a given experiment from that 
    trials metadata markdown file
    
    Parameters:
        -path: String. Path to markdown file containing metadata
    
    Returns:
        -temp: temperature from metadata file'''
    
    data = np.loadtxt(path, unpack=True)
    temp = data[0]

    return temp
