from __future__ import print_function

from collections import OrderedDict
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

label_map = OrderedDict([
    ('PF6', r'$\ce{[PF6]-}$'),
    ('Tf2N', r'$\ce{[Tf2N]-}$'),
    ('BF4', r'$\ce{[BF4]-}$'),
    ('TfO', r'$\ce{[TfO]-}$'),
    ('TFA', r'$\ce{[TFA]-}$'),
    ('DCA', r'$\ce{[DCA]-}$'),
    # This is the in-plane thiocyanate.
    # ('SCN-N', r'$\ce{[SCN-N]-}$'),
    # This is the out-of-plane thiocyanate
    #  (SCN-.S, but not actually S-bound).
    ('SCN', r'$\ce{[SCN]-}$')
])
results_expt = OrderedDict([
    ('PF6', 2342.5),
    ('Tf2N', 2341.7),
    ('BF4', 2341.7),
    ('TfO', 2341),
    ('TFA', 2340),
    ('DCA', 2339),
#    ('SCN-N', 2336),
    ('SCN', 2336)
])
results_calc = OrderedDict([
    ('PF6', 2437.74),
    ('Tf2N', 2435.8),
    ('BF4', 2434.69),
    ('TfO', 2431.91),
    ('TFA', 2429.31),
    ('DCA', 2430.47),
#    ('SCN-N', 2431.64),
    ('SCN', 2430.24)
])
scale_factor = 0.9627


def main():
    """The main routine."""
    labels = list(label_map.values())
    ticks = list(range(len(labels)))
    freq_expt = [results_expt.get(cluster) for cluster in label_map]
    freq_calc = [results_calc.get(cluster) for cluster in label_map]
    freq_calc_scaled = [results_calc.get(cluster) * scale_factor
                        for cluster in label_map]
    calc_expt_diff = [((results_calc.get(cluster) * scale_factor) - results_expt.get(cluster))
                      for cluster in label_map]

    ##########

    fig, ax = plt.subplots()

    plot_settings = {
        'markersize': 10,
        # 'linestyle': '-',
        'linewidth': 2,
    }

    ax.plot(ticks,
            freq_expt,
            color='red',
            marker='o',
            linestyle='-',
            label=r'experiment, $\ce{[C4C1im+]}$',
            **plot_settings)
    ax.plot(ticks,
            freq_calc_scaled,
            color='blue',
            marker='s',
            linestyle='--',
            label=r'B3LYP/6-31G(d,p), scaled by {}, $\ce{{[C1C1im+]}}$'.format(scale_factor),
            **plot_settings)

    ax.tick_params(direction='out', top=False, right=False, labelsize='large')
    ax.set_xlabel('ionic liquid anion', fontsize='x-large')
    ax.set_ylabel(r'$\nu_{3}$ frequency ($\si{\wavenumber}$)', fontsize='x-large')
    ax.set_xlim((ticks[0], ticks[-1]))
    ax.set_xticklabels(labels)

    ax.legend(loc='best', fancybox=True, framealpha=0.5, numpoints=1)

    fig.savefig('frequencies_calc_vs_expt1.pdf', bbox_inches='tight')

    ##########

    return locals()


if __name__ == '__main__':

    main_locals = main()
