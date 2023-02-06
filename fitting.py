import numpy as np
from scipy.optimize import curve_fit
from matplotlib import rc
font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 22}
rc('font', **font)
from matplotlib.offsetbox import AnchoredText

from fitting_and_analysis import CurveFitAnalysis
from fitting_and_analysis import Output
Output = Output()

class Fitting():
    def __init__(self, model, x, y_measured, y_error, p0=None):
        self.model = model
        self.x = x
        self.y_measured = y_measured
        self.y_error = y_error

        self.popt, self.pcov = curve_fit(self.model, self.x, self.y_measured, sigma=y_error, absolute_sigma=True, p0=p0)
        self.parameter_errors = np.sqrt(np.diag(self.pcov))

        self.fitted_function = self.model.CorrespondingFittedFunction(popt=self.popt, parameter_errors=self.parameter_errors)

        self.cfa = CurveFitAnalysis(self.x, self.y_measured, self.y_error, self.fitted_function)

    def plot_data_and_fit(self, ax, **kwargs):

        Output.baseplot_errorbars(ax=ax, x=self.x, y=self.y_measured, yerr=self.y_error, xerr=None, label='data')

        x_for_plotting_fit = np.linspace(*ax.get_xlim(), 10000)

        ax.plot(x_for_plotting_fit, self.fitted_function(x_for_plotting_fit), label='fit')

        info_sigfigs = 3
        info_fontsize = 22

        info_on_ax = '\n$\chi^2$ / DOF = ' + Output.to_sf(self.cfa.raw_chi2, sf=info_sigfigs) + ' / ' + str(self.cfa.degrees_of_freedom) + ' = ' + Output.to_sf(self.cfa.reduced_chi2, sf=info_sigfigs) + \
                     '\n$\chi^2$ prob = ' + Output.to_sf(self.cfa.chi2_probability, sf=info_sigfigs) + \
                     self.fitted_function.other_info

        ax_text = AnchoredText(info_on_ax, loc='lower left', frameon=False, prop=dict(fontsize=info_fontsize))
        ax.add_artist(ax_text)
        ax.legend()