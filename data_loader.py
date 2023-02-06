import numpy as np
from astropy import units as u

from physical_quantity import PhysicalQuantity
import fitting_and_analysis as cff
cff = cff.CurveFitFuncs()

class DataLoader():
    def __init__(self, filename):
        self.full_data = np.loadtxt(filename)
        self.zeroed_data = cff.remove_systematic_error(self.full_data)

        instrumental_uncertainty = 0.25 * u.millimeter
        self.physical_quantities = np.array([PhysicalQuantity(data=data * u.millimeter, uncertainty=instrumental_uncertainty)] for data in self.full_data)
        self.zeroed_physical_quantities = np.array([PhysicalQuantity(data=data * u.millimeter, uncertainty=instrumental_uncertainty)] for data in self.zeroed_data)

        self.errors = np.zeros_like(self.zeroed_data) + instrumental_uncertainty.value

        self.x = np.linspace(0, 1000, len(self.full_data), endpoint=True)