from __future__ import print_function

import scipy.io as spio

import matplotlib as mpl
mpl.rc('text', usetex=True)
# mpl.rc('font', family='serif')
mpl.rcParams['text.latex.preamble'] = [
    r'\usepackage{sfmath}',
    r'\usepackage[version=4]{mhchem}',
    r'\mhchemoptions{font=sf}',
    r'\usepackage{siunitx}',
    r'\sisetup{detect-all}',
    r'\DeclareSIUnit\wavenumber{\per\centi\metre}',
]
mpl.use('Agg')
import matplotlib.pyplot as plt


mat_contents = spio.loadmat('linear_spectroscopy_summary.mat', struct_as_record=False)

data_1_CO2 = mat_contents['data'][0, 0].CO2[0, 0]
data_2_CO2 = mat_contents['data'][0, 1].CO2[0, 0]
data_3_CO2 = mat_contents['data'][0, 2].CO2[0, 0]
data_4_CO2 = mat_contents['data'][0, 3].CO2[0, 0]
data_5_CO2 = mat_contents['data'][0, 4].CO2[0, 0]
data_6_CO2 = mat_contents['data'][0, 5].CO2[0, 0]

data_1_neat = mat_contents['data'][0, 0].neat[0, 0]
data_2_neat = mat_contents['data'][0, 1].neat[0, 0]
data_3_neat = mat_contents['data'][0, 2].neat[0, 0]
data_4_neat = mat_contents['data'][0, 3].neat[0, 0]
data_5_neat = mat_contents['data'][0, 4].neat[0, 0]
data_6_neat = mat_contents['data'][0, 5].neat[0, 0]

# plot single spectrum

fig, ax = plt.subplots()

plot_settings = {
    'linestyle': '-',
    'linewidth': 0.75,
}

ax.plot(data_4_CO2.freq, data_4_CO2.abs, label=r'$\ce{[C4C1im][TfO]}$ with $\ce{CO2}$', color='red', **plot_settings)
ax.plot(data_4_neat.freq, data_4_neat.abs, label=r'$\ce{[C4C1im][TfO]}$ neat', color='#898c8a', **plot_settings)

ax.set_xlim(left=1000, right=3500)
ax.set_ylim(bottom=-0.25, top=1.75)
# ax.set_ylim(bottom=0.0, top=1.75)
ax.set_xlabel(r'frequency ($\si{\wavenumber}$)', fontsize='x-large')
ax.set_ylabel('absorbance', fontsize='x-large')
ax.tick_params(direction='out', top=False, right=False, labelsize='large')
ax.legend(fancybox=True, loc='upper right', framealpha=0.50)

fig.savefig('experimental_spectra_TfO.pdf', bbox_inches='tight')

# plot CO2 \nu_{3} peak for all anions

fig, ax = plt.subplots()

plot_settings = {
    # 'linestyle': '-',
    'linewidth': 1.5,
    'marker': '',
    'markersize': 10,
}


ax.plot(data_5_CO2.freq,
        data_5_CO2.normed_subbed,
        label=r'$\ce{[PF6]-}$',
        linestyle='-.',
        color='orange',
        **plot_settings)

ax.plot(data_2_CO2.freq,
        data_2_CO2.normed_subbed,
        label=r'$\ce{[Tf2N]-}$',
        linestyle='--',
        color='green',
        **plot_settings)

ax.plot(data_4_CO2.freq,
        data_4_CO2.normed_subbed,
        label=r'$\ce{[TfO]-}$',
        linestyle='-',
        color='black',
        **plot_settings)

ax.plot(data_1_CO2.freq,
        data_1_CO2.normed_subbed,
        label=r'$\ce{[TFA]-}$',
        linestyle='-.',
        color='blue',
        **plot_settings)

ax.plot(data_3_CO2.freq.transpose(),
        data_3_CO2.normed_subbed.transpose(),
        label=r'$\ce{[DCA]-}$',
        linestyle='--',
        color='red',
        **plot_settings)

ax.plot(data_6_CO2.freq,
        data_6_CO2.normed_subbed,
        label=r'$\ce{[SCN]-}$',
        linestyle='-',
        color='purple',
        **plot_settings)

ax.set_xlim(left=2332, right=2348)
ax.set_ylim(bottom=0, top=1.05)
ax.set_xlabel(r'frequency ($\si{\wavenumber}$)', fontsize='x-large')
ax.set_ylabel('absorbance (normalized)', fontsize='x-large')
ax.tick_params(direction='out', top=False, right=False, labelsize='large')
ax.legend(fancybox=True, loc='best', framealpha=0.50)

fig.savefig('experimental_spectra_shifting.pdf', bbox_inches='tight')
