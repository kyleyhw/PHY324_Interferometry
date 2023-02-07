import fit_models
from fitting_and_analysis import Output
Output = Output()

class Gaussian(): # height is usually 1; not probability density
    def __init__(self, popt, parameter_errors, info_sigfigs=2):
        self.popt = popt
        (self.base, self.scale, self.mu, self.sigma) = popt

        self.function = fit_models.Gaussian()
        self.number_of_parameters = self.function.number_of_parameters

    def __call__(self, x):
        result = self.function(x, *self.popt)
        return result


class GaussianZeroCenter(): # height is usually 1; not probability density
    def __init__(self, popt, parameter_errors, info_sigfigs=2):
        self.popt = popt
        (self.base, self.scale, self.sigma) = popt

        self.function = fit_models.GaussianZeroCenter()
        self.number_of_parameters = self.function.number_of_parameters

    def __call__(self, x):
        result = self.function(x, *self.popt)
        return result


class Linear():
    def __init__(self, popt, parameter_errors, units_for_parameters, info_sigfigs=4, override_info=False): # OVERRIDE_INFO
        self.popt = popt
        (self.m, self.c) = popt
        (self.m_error, self.c_error) = parameter_errors

        self.function = fit_models.Linear()
        self.number_of_parameters = self.function.number_of_parameters
        self.units_for_parameters = units_for_parameters


        if override_info: # OVERRIDE_INFO
            self.parameter_info = '\nm = (' + f'{float(Output.to_sf(self.m, info_sigfigs)):1.2f}' + ' $\pm$ ' + Output.to_sf(
                self.m_error, 1) + ') ' + self.units_for_parameters[0] + \
                                  '\nc = (' + f'{float(Output.to_sf(self.c, info_sigfigs)):2.3f}' + ' $\pm$ ' + Output.to_sf(
                self.c_error, 1) + ') ' + self.units_for_parameters[1]

        else:
            self.parameter_info = '\nm = (' + Output.to_sf(self.m, info_sigfigs) + ' $\pm$ ' + Output.to_sf(
                self.m_error, 1) + ') ' + self.units_for_parameters[0] + \
                                  '\nc = (' + Output.to_sf(self.c, info_sigfigs) + ' $\pm$ ' + Output.to_sf(
                self.c_error, 1) + ') ' + self.units_for_parameters[1]


    def __call__(self, x):
        result = self.function(x, *self.popt)
        return result