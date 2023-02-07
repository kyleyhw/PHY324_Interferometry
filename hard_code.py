# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 20:18:12 2023

@author: shash
"""

import numpy as np


def convert_fringe_to_distance(fringes, fringe_error):
    '''
    Parameters
    ----------
    fringes : araray
        Fringe Values (x values of the plot)
    fringe_error: array
    errors in the fringe values (should be +-1)
    Returns
    -------
    Array. returns array of displacements and its corresponding uncertainties.

    '''
    return(fringes * 589.3/2, fringe_error* 589.3/2)

def indexrefrac(fit_slope, micrometer_displacement, thickness, slope_uncert, micrometer_uncert, thickness_uncert):
    '''   
    Parameters
    ----------
    fit_slope : float
        slope of best fit, should be in units of distance of mirror movement/units of micrometer displacement
        enter units as m/mm
    micrometer_displacement : float
        value of micrometer displacement in mm
    thickness : float
        thickness of slide (enter with units of meters)

    Returns
    -------
    value of index of refraction and the associated uncertainty

    '''
    return((micrometer_displacement * fit_slope)/(thickness) + 1, np.sqrt(((fit_slope/thickness)*micrometer_uncert)**2 + ((micrometer_displacement/thickness)*slope_uncert)**2 + ((micrometer_displacement * fit_slope/thickness**2)*thickness_uncert)**2))


def reciprocal_uncertainty(value, uncertainty):
    '''
    Parameters
    ----------
    value : float
        value you wish to reciprocal
    uncertainty : float
        uncertainty of this value

    Returns
    -------
    returns 1/value and its overall uncertainty

    '''    
    return(1/value, uncertainty/(value**2))



def quadratic_error_sum(err_a, err_b):
    return np.sqrt(err_a**2 + err_b**2)

fit_slope = 5.064
slope_uncert = 0.01

(fit_slope, slope_uncert) = reciprocal_uncertainty(fit_slope, slope_uncert)

micrometer_displacement_trial_1 = 19.03-16.32
micrometer_displacement_trial_2 = 19.045-16.355
micrometer_uncert = quadratic_error_sum(0.005, 0.005)

thickness = 1
thickness_uncert = 0.1

index1, index1_error = indexrefrac(fit_slope, micrometer_displacement_trial_1, thickness, slope_uncert, micrometer_uncert, thickness_uncert)
index2, index2_error = indexrefrac(fit_slope, micrometer_displacement_trial_2, thickness, slope_uncert, micrometer_uncert, thickness_uncert)

mean_index = (index1 + index2) / 2
mean_index_error = quadratic_error_sum(index1_error, index2_error)

print('index1, index1 error = ', index1, ',',  index1_error)
print('index2, index2 error = ', index2, ',', index2_error)
print('mean index, mean index error = ', mean_index, ',', mean_index_error)

