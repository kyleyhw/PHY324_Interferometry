import numpy as np
import scipy.stats as spstats

class CurveFitFuncs():
    def __init__(self):
        pass

    def baseplot_errorbars(self, ax, x, y, yerr=None, xerr=None, label=None, **kwargs):
        ax.errorbar(x, y, yerr=yerr, xerr=xerr, linestyle='None', capsize=2, label=label, **kwargs)

    def baseplot_errorbars_with_markers(self, ax, x, y, yerr=None, xerr=None, label=None, marker='.', **kwargs):
        ax.errorbar(x, y, yerr=yerr, xerr=xerr, linestyle='None', capsize=2, label=label, marker=marker)
    
    def to_sf(self, num, sf=4):
        result = '%.*g' % (sf, num)
        # result = (f'{num:.{sf}g}')
        return result




    def remove_systematic_error(self, arr):
        return arr - arr[0]

    def residual(self, yarr_measured, yarr_predicted):
        return yarr_measured - yarr_predicted

    def sum_squared_ratio(self, numer, denom):
        return np.sum((numer ** 2) / (denom ** 2))

    def calc_dof(self, yarr_measured, params_in_model):
        dof = len(yarr_measured) - params_in_model
        return dof

    def calc_raw_chi_squared(self, yarr_measured, yarr_predicted, y_uncertainty):
        numer = self.residual(yarr_measured, yarr_predicted)
        denom = y_uncertainty
        return self.sum_squared_ratio(numer, denom)

    def calc_reduced_chi_squared(self, yarr_measured, yarr_predicted, y_uncertainty, params_in_model):
        numer = self.residual(yarr_measured, yarr_predicted)
        denom = y_uncertainty
        dof = len(yarr_measured) - params_in_model
        return self.sum_squared_ratio(numer, denom) / dof

    def calc_chi2_probability(self, raw_chi2, dof):
        chi2_prob = (1 - spstats.chi2.cdf(raw_chi2, dof))
        return chi2_prob




class CurveFitAnalysis():
    def __init__(self, xarr, yarr_measured, yarr_uncertainty, FittedFunc): # FittedFunc must have params_in_model attribute
        cff = CurveFitFuncs()
        yarr_predicted = FittedFunc(xarr)

        self.degrees_of_freedom = cff.calc_dof(yarr_measured, FittedFunc.params_in_model)
        self.raw_chi2 = cff.calc_raw_chi_squared(yarr_measured, yarr_predicted, yarr_uncertainty)
        self.reduced_chi2 = cff.calc_reduced_chi_squared(yarr_measured, yarr_predicted, yarr_uncertainty, FittedFunc.params_in_model)
        self.chi2_probability = cff.calc_chi2_probability(self.raw_chi2, self.degrees_of_freedom)

