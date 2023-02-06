import numpy as np
import fitting_and_analysis as cff
cff = cff.CurveFitFuncs()

class DataLoader():
    def __init__(self, filename):
        self.full_data = np.loadtxt(filename)
        self.zeroed_data = cff.remove_systematic_error(self.full_data)