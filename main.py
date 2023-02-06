import matplotlib.pyplot as plt
from matplotlib import rc
font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 22}
rc('font', **font)

import data_loader
import fit_models
import fitting

data = data_loader.DataLoader('PHY324_Interferometry_calibration_curve_data.txt')
model = fit_models.Linear()

fit = fitting.Fitting(model=model, x=data.x, y_measured=data.full_data, y_error=data.errors)

fig, ax = plt.subplots(1, 1, figsize=(32, 18))

fit.plot_data_and_fit(ax)

ax.set_title('Interferometry calibration curve')
ax.grid(visible=True, which='both')

fig.savefig('PHY324_Interferometry_calibration_curve.png')
fig.show()