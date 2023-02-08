import matplotlib.pyplot as plt
from matplotlib import rc
font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 22}
rc('font', **font)

import data_loader
import fit_models
import fitting


def fit_data_to_fringes(show=False, save=False):
        data = data_loader.DataLoader('PHY324_Interferometry_calibration_curve_data.txt')
        model = fit_models.Linear()

        fit = fitting.Fitting(model=model, x=data.x, x_error=data.x_error, y_measured=data.full_data, y_error=data.errors, units_for_parameters=('mm per fringe', 'mm'))

        fig, ax = plt.subplots(1, 1, figsize=(16, 9))

        fit.scatter_plot_data_and_fit(ax, plot_fit=False)

        ax.set_title('Calibration data')
        ax.grid(visible=True, which='both')
        ax.set_ylabel('Micrometer reading (mm)') # I disagree with putting units in brackets but TA forces this
        ax.set_xlabel('Fringes passed')

        if save:
                fig.savefig('PHY324_Interferometry_micrometer_reading_vs_fringes_passed.png')
        if show:
                fig.show()

def fit_data_to_path_length(show=False, save=False):
        data = data_loader.DataLoader('PHY324_Interferometry_calibration_curve_data.txt')
        model = fit_models.Linear()

        wavelength = 589.3e-6 # mm

        data.x = data.x * wavelength/2
        data.x_error = data.x_error * wavelength/2

        fit = fitting.Fitting(model=model, x=data.x, x_error=data.x_error, y_measured=data.full_data,
                              y_error=data.errors, units_for_parameters=('(unitless)', 'mm'))

        fig, ax = plt.subplots(1, 1, figsize=(16, 9))

        fit.scatter_plot_data_and_fit(ax)

        ax.set_title('Calibration curve for path length change')
        ax.grid(visible=True, which='both')
        ax.set_ylabel('Micrometer reading (mm)')  # I disagree with putting units in brackets but TA forces this
        ax.set_xlabel('Path length change (mm)')

        if save:
                fig.savefig('PHY324_Interferometry_micrometer_reading_vs_path_length_change.png')
        if show:
                fig.show()

def plot_residuals(show=True, save=False):
        data = data_loader.DataLoader('PHY324_Interferometry_calibration_curve_data.txt')
        model = fit_models.Linear()

        wavelength = 589.3e-6 # mm

        data.x = data.x * wavelength/2
        data.x_error = data.x_error * wavelength/2

        fit = fitting.Fitting(model=model, x=data.x, x_error=data.x_error, y_measured=data.full_data,
                              y_error=data.errors, units_for_parameters=('', ''))

        fig, ax2 = plt.subplots(1, 1, figsize=(16, 9))

        fit.plot_residuals(ax2)

        ax2.set_title('Calibration curve residuals')
        ax2.grid(visible=True, which='both')
        ax2.set_ylabel('Residuals (mm)')  # I disagree with putting units in brackets but TA forces this
        ax2.set_xlabel('Path length change (mm)')

        if show:
                fig.show()
        if save:
                fig.savefig('PHY324_Interferometry_calibration_curve_residuals.png')


fit_data_to_fringes(show=True, save=False)
fit_data_to_path_length(show=True, save=False)
plot_residuals(show=True, save=False)