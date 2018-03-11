#!/usr/bin/env python

from __future__ import print_function
import pandas as pd
import numpy as np
from numpy import nan
from collections import OrderedDict


def make_df_single_valued(df, key, default=nan):
    """For each element of a DataFrame that's a dict, replace that element
    with a value from the dict.
    """
    newdf = pd.DataFrame()
    for row in df.index:
        for column in df.columns:
            if isinstance(df.loc[row, column], dict):
                newdf.loc[row, column] = df.loc[row, column].get(key, default)
            else:
                newdf.loc[row, column] = df.loc[row, column]
    return newdf


def make_alpha_beta(d, systems, calc_types):
    """"""
    for system in systems:
        for calc_type in calc_types:
            d[system][calc_type]['alpha'] = (d[system][calc_type]['s'] + d[system][calc_type]['a']) / 2
            d[system][calc_type]['beta'] = (d[system][calc_type]['s'] - d[system][calc_type]['a']) / 2

def main(do_plot=False, dump_pd=False):
    """The main routine."""

    results = dict()

    systems = ('cation', 'BF4', 'DCA', 'PF6', 'SCN', 'TFA', 'Tf2N', 'TfO')
    calc_types = ('free', 'geometry', 'point\ncharges', 'ALMO', 'full')

    system_label_map = {
        'cation': r'''cation
alone''',
        'BF4': r'[BF$_{4}$]$^{-}$',
        'DCA': r'[DCA]$^{-}$',
        'PF6': r'[PF$_{6}$]$^{-}$',
        'SCN': r'[SCN]$^{-}$',
        'TFA': r'[TFA]$^{-}$',
        'Tf2N': r'[Tf$_{2}$N]$^{-}$',
        'TfO': r'[TfO]$^{-}$'
    }

    system_color_map = {
        'cation': '#2d4182',
        'BF4': '#2d4182',
        'DCA': '#166C36',
        'PF6': '#D32026',
        'SCN': '#28AAA4',
        'TFA': '#8A357B',
        'Tf2N': '#ADB030',
        'TfO': '#4F4F4E'
    }

    freq_dict = dict()
    freq_noCT_dict = dict()
    for system in systems:
        freq_dict[system] = dict()
        freq_noCT_dict[system] = dict()

    # 1. CO2, free geometry
    freq_CO2_free = {'a': 2436.10, 's': 1371.93}
    for system in systems:
        freq_dict[system][calc_types[0]] = freq_CO2_free
        freq_noCT_dict[system][calc_types[0]] = freq_CO2_free

    # 2. CO2, cluster geometry, free
    freq_dict['cation'][calc_types[1]] = {'a': 2443.07, 's': 1372.12}
    freq_dict['BF4'][calc_types[1]] = {'a': 2434.71, 's': 1372.96}
    freq_dict['DCA'][calc_types[1]] = {'a': 2430.85, 's': 1370.71}
    freq_dict['PF6'][calc_types[1]] = {'a': 2437.48, 's': 1373.95}
    freq_dict['SCN'][calc_types[1]] = {'a': 2430.27, 's': 1370.35}
    freq_dict['TFA'][calc_types[1]] = {'a': 2429.81, 's': 1371.68}
    freq_dict['Tf2N'][calc_types[1]] = {'a': 2437.74, 's': 1372.68}
    freq_dict['TfO'][calc_types[1]] = {'a': 2433.89, 's': 1371.14}

    # 3. CO2, cluster geometry, electrostatics from point charges (PC)
    freq_dict['cation'][calc_types[2]] = {'a': 2447.34, 's': 1373.96}
    freq_dict['BF4'][calc_types[2]] = {'a': 2438.87, 's': 1374.04}
    freq_dict['DCA'][calc_types[2]] = {'a': 2436.12, 's': 1371.88}
    freq_dict['PF6'][calc_types[2]] = {'a': 2441.30, 's': 1375.02}
    freq_dict['SCN'][calc_types[2]] = {'a': 2434.23, 's': 1371.33}
    freq_dict['TFA'][calc_types[2]] = {'a': 2434.60, 's': 1372.69}
    freq_dict['Tf2N'][calc_types[2]] = {'a': 2441.30, 's': 1373.69}
    freq_dict['TfO'][calc_types[2]] = {'a': 2438.87, 's': 1372.16}

    # 4. CO2, cluster geometry, electrostatics from ALMO
    freq_dict['cation'][calc_types[3]] = {'a': 2445.99, 's': 1376.27}
    freq_dict['BF4'][calc_types[3]] = {'a': 2437.69, 's': 1374.51}
    freq_dict['DCA'][calc_types[3]] = {'a': 2434.75, 's': 1372.58}
    freq_dict['PF6'][calc_types[3]] = {'a': 2440.03, 's': 1375.55}
    freq_dict['SCN'][calc_types[3]] = {'a': 2433.14, 's': 1371.40}
    freq_dict['TFA'][calc_types[3]] = {'a': 2432.93, 's': 1372.90}
    freq_dict['Tf2N'][calc_types[3]] = {'a': 2439.46, 's': 1374.21}
    freq_dict['TfO'][calc_types[3]] = {'a': 2436.75, 's': 1372.68}

    # 5. CO2, cluster geometry, full system
    freq_dict['cation'][calc_types[4]] = {'a': 2442.19, 's': 1374.38}
    freq_dict['BF4'][calc_types[4]] = {'a': 2434.69, 's': 1372.55}
    freq_dict['DCA'][calc_types[4]] = {'a': 2430.47, 's': 1368.48}
    freq_dict['PF6'][calc_types[4]] = {'a': 2437.74, 's': 1374.45}
    freq_dict['SCN'][calc_types[4]] = {'a': 2430.24, 's': 1368.38}
    freq_dict['TFA'][calc_types[4]] = {'a': 2429.31, 's': 1369.09}
    freq_dict['Tf2N'][calc_types[4]] = {'a': 2435.80, 's': 1372.81}
    freq_dict['TfO'][calc_types[4]] = {'a': 2431.91, 's': 1370.02}

    freqs_cation = [freq_dict['cation'][calc_type]['a'] for calc_type in calc_types]
    freqs_BF4 = [freq_dict['BF4'][calc_type]['a'] for calc_type in calc_types]
    freqs_DCA = [freq_dict['DCA'][calc_type]['a'] for calc_type in calc_types]
    freqs_PF6 = [freq_dict['PF6'][calc_type]['a'] for calc_type in calc_types]
    freqs_SCN = [freq_dict['SCN'][calc_type]['a'] for calc_type in calc_types]
    freqs_TFA = [freq_dict['TFA'][calc_type]['a'] for calc_type in calc_types]
    freqs_Tf2N = [freq_dict['Tf2N'][calc_type]['a'] for calc_type in calc_types]
    freqs_TfO = [freq_dict['TfO'][calc_type]['a'] for calc_type in calc_types]
    freqs = {
        'cation': freqs_cation,
        'BF4': freqs_BF4,
        'DCA': freqs_DCA,
        'PF6': freqs_PF6,
        'SCN': freqs_SCN,
        'TFA': freqs_TFA,
        'Tf2N': freqs_Tf2N,
        'TfO': freqs_TfO
    }

    # 2b. CO2, cluster geometry (no CT), free
    freq_noCT_dict['cation'][calc_types[1]] = {'a': 2439.86, 's': 1371.47}
    freq_noCT_dict['BF4'][calc_types[1]] = {'a': 2438.56, 's': 1373.31}
    freq_noCT_dict['DCA'][calc_types[1]] = {'a': 2439.10, 's': 1373.44}
    freq_noCT_dict['PF6'][calc_types[1]] = {'a': 2438.47, 's': 1373.33}
    freq_noCT_dict['SCN'][calc_types[1]] = {'a': 2438.78, 's': 1373.14}
    freq_noCT_dict['TFA'][calc_types[1]] = {'a': 2438.39, 's': 1373.65}
    freq_noCT_dict['Tf2N'][calc_types[1]] = {'a': 2438.76, 's': 1373.06}
    freq_noCT_dict['TfO'][calc_types[1]] = {'a': 2439.37, 's': 1373.45}

    # 3b. CO2, cluster geometry (no CT), electrostatics from point charges (PC)
    freq_noCT_dict['cation'][calc_types[2]] = {'a': 2443.70, 's': 1373.03}
    freq_noCT_dict['BF4'][calc_types[2]] = {'a': 2442.50, 's': 1374.36}
    freq_noCT_dict['DCA'][calc_types[2]] = {'a': 2443.61, 's': 1374.39}
    freq_noCT_dict['PF6'][calc_types[2]] = {'a': 2441.94, 's': 1374.25}
    freq_noCT_dict['SCN'][calc_types[2]] = {'a': 2442.66, 's': 1373.96}
    freq_noCT_dict['TFA'][calc_types[2]] = {'a': 2442.20, 's': 1374.48}
    freq_noCT_dict['Tf2N'][calc_types[2]] = {'a': 2442.07, 's': 1373.80}
    freq_noCT_dict['TfO'][calc_types[2]] = {'a': 2444.06, 's': 1374.41}

    # 4b. CO2, cluster geometry (no CT), electrostatics from ALMO
    freq_noCT_dict['cation'][calc_types[3]] = {'a': 2442.67, 's': 1374.13}
    freq_noCT_dict['BF4'][calc_types[3]] = {'a': 2441.62, 's': 1374.81}
    freq_noCT_dict['DCA'][calc_types[3]] = {'a': 2442.59, 's': 1374.74}
    freq_noCT_dict['PF6'][calc_types[3]] = {'a': 2441.03, 's': 1374.61}
    freq_noCT_dict['SCN'][calc_types[3]] = {'a': 2441.37, 's': 1374.20}
    freq_noCT_dict['TFA'][calc_types[3]] = {'a': 2441.06, 's': 1374.71}
    freq_noCT_dict['Tf2N'][calc_types[3]] = {'a': 2440.85, 's': 1374.07}
    freq_noCT_dict['TfO'][calc_types[3]] = {'a': 2442.54, 's': 1374.84}

    # 5b. CO2, cluster geometry (no CT), full system
    freq_noCT_dict['cation'][calc_types[4]] = {'a': 2440.19, 's': 1373.05}
    freq_noCT_dict['BF4'][calc_types[4]] = {'a': 2439.36, 's': 1373.79}
    freq_noCT_dict['DCA'][calc_types[4]] = {'a': 2438.95, 's': 1372.50}
    freq_noCT_dict['PF6'][calc_types[4]] = {'a': 2438.69, 's': 1373.77}
    freq_noCT_dict['SCN'][calc_types[4]] = {'a': 2438.45, 's': 1372.67}
    freq_noCT_dict['TFA'][calc_types[4]] = {'a': 2438.78, 's': 1373.07}
    freq_noCT_dict['Tf2N'][calc_types[4]] = {'a': 2438.37, 's': 1373.23}
    freq_noCT_dict['TfO'][calc_types[4]] = {'a': 2438.52, 's': 1373.08}

    freqs_noCT_cation = [freq_noCT_dict['cation'][calc_type]['a'] for calc_type in calc_types]
    freqs_noCT_BF4 = [freq_noCT_dict['BF4'][calc_type]['a'] for calc_type in calc_types]
    freqs_noCT_DCA = [freq_noCT_dict['DCA'][calc_type]['a'] for calc_type in calc_types]
    freqs_noCT_PF6 = [freq_noCT_dict['PF6'][calc_type]['a'] for calc_type in calc_types]
    freqs_noCT_SCN = [freq_noCT_dict['SCN'][calc_type]['a'] for calc_type in calc_types]
    freqs_noCT_TFA = [freq_noCT_dict['TFA'][calc_type]['a'] for calc_type in calc_types]
    freqs_noCT_Tf2N = [freq_noCT_dict['Tf2N'][calc_type]['a'] for calc_type in calc_types]
    freqs_noCT_TfO = [freq_noCT_dict['TfO'][calc_type]['a'] for calc_type in calc_types]
    freqs_noCT = {
        'cation': freqs_noCT_cation,
        'BF4': freqs_noCT_BF4,
        'DCA': freqs_noCT_DCA,
        'PF6': freqs_noCT_PF6,
        'SCN': freqs_noCT_SCN,
        'TFA': freqs_noCT_TFA,
        'Tf2N': freqs_noCT_Tf2N,
        'TfO': freqs_noCT_TfO
    }

    make_alpha_beta(freq_dict, systems, calc_types)
    make_alpha_beta(freq_noCT_dict, systems, calc_types)

    results['freq_dict'] = freq_dict
    results['freq_noCT_dict'] = freq_noCT_dict
    freq_df = pd.DataFrame(freq_dict)
    freq_noCT_df = pd.DataFrame(freq_noCT_dict)
    results['freq_df'] = freq_df
    results['freq_noCT_df'] = freq_noCT_df

    if dump_pd:
        with pd.ExcelWriter('frequencies.xlsx') as writer:
            make_df_single_valued(freq_df, 'a').to_excel(writer, sheet_name='CT (a)')
            make_df_single_valued(freq_noCT_df, 'a').to_excel(writer, sheet_name='noCT (a)')
            make_df_single_valued(freq_df, 's').to_excel(writer, sheet_name='CT (s)')
            make_df_single_valued(freq_noCT_df, 's').to_excel(writer, sheet_name='noCT (s)')
            make_df_single_valued(freq_df, 'alpha').to_excel(writer, sheet_name='CT (alpha)')
            make_df_single_valued(freq_noCT_df, 'alpha').to_excel(writer, sheet_name='noCT (alpha)')
            make_df_single_valued(freq_df, 'beta').to_excel(writer, sheet_name='CT (beta)')
            make_df_single_valued(freq_noCT_df, 'beta').to_excel(writer, sheet_name='noCT (beta)')

    if do_plot:
        mpl_font_dict = {
            # 'family': ['Myriad Pro', 'Lucida Grande', 'Helvetica', 'sans-serif'],
            'family': ['Helvetica', 'sans-serif'],
        }
        mpl_mathtext_dict = {
            'default': 'regular',
        }
        mpl_tick_dict = {
            'major.size': 3,
            'minor.size': 1.5,
        }
        mpl_axes_dict = {
            'linewidth': 0.5,
        }
        import matplotlib as mpl
        # mpl.rc('text', usetex=True)
        mpl.rc('font', **mpl_font_dict)
        mpl.rc('mathtext', **mpl_mathtext_dict)
        mpl.rc('xtick', **mpl_tick_dict)
        mpl.rc('ytick', **mpl_tick_dict)
        mpl.rc('axes', **mpl_axes_dict)
        import matplotlib.pyplot as plt

        ######
        # Compare absolute results for all methods.

        fig0, (ax0, ax0_noCT) = plt.subplots(nrows=2, ncols=1, sharex=True,
                                             figsize=(3.3, 4.5), dpi=600)

        axes = [ax0, ax0_noCT]

        plot_common_settings = {
            'marker' : 'o',
            'markersize': 2.5,
            'markeredgewidth': 0.0,
            'linewidth': 0.5,
        }

        calc_types_no_pc = OrderedDict([
            ('free', r'\omega_{\mathrm{free}}'),
            ('geometry', r'+\omega_{\mathrm{GEOM}}'),
            ('ALMO', r'+\omega_{\mathrm{FRZ}}\n+\omega_{\mathrm{POL}}'),
            ('full', r'+\omega_{\mathrm{CT}}'),
        ])
        xticks = list(range(len(calc_types_no_pc)))
        freqs_no_pc =

        xytext_CT_offset_map = {
            'cation': 0.0,
            'BF4': -0.2,
            'DCA': 0.25,
            'PF6': 0.0,
            'SCN': -0.65,
            'TFA': -1.0,
            'Tf2N': 0.0,
            'TfO': 0.2
        }

        for system in systems:
            ax0.plot(xticks,
                     freqs[system],
                     label=system_label_map[system],
                     color=system_color_map[system],
                     **plot_common_settings)
            ax0_noCT.plot(xticks,
                          freqs_noCT[system],
                          label=system_label_map[system],
                          color=system_color_map[system],
                          **plot_common_settings)
            # Add a label to the rightmost side of the plot. For now,
            # only do the CT one; no_CT is too hard to tell.
            xy_CT = [xticks[-1], freqs[system][-1]]
            xytext_CT = [xy_CT[0] + 0.10, xy_CT[1] + xytext_CT_offset_map[system]]
            print(xy_CT, xytext_CT)
            ax0.annotate(system_label_map[system], xy=xy_CT, xytext=xytext_CT,
                         fontsize=7,
                         ha='left', va='center')

        ylim_start = 2428
        ylim_stop = 2448
        ytickstep = 4
        y_formatter = mpl.ticker.ScalarFormatter(useOffset=False)
        for axis in axes:
            axis.set_ylim(ylim_start, ylim_stop)
            axis.yaxis.set_ticks(np.arange(ylim_start, ylim_stop + ytickstep, ytickstep))
            axis.yaxis.set_major_formatter(y_formatter)
            axis.set_xticks(xticks)
            axis.tick_params(top='off', direction='out', labelsize=7)
        ax0_noCT.set_xticklabels(calc_types_no_pc, fontsize=7)
        fig0.text(0.00, 0.50, r'$\nu_{3}$ frequency (cm$^{-1}$)',
                  ha='center', va='center', rotation='vertical', fontsize=8,
                  transform=fig0.transFigure)
        fig0.savefig('00_all.pdf', bbox_inches='tight')

    covp_dict = dict()
    covp_noCT_dict = dict()
    for system in systems:
        covp_dict[system] = dict()
        covp_noCT_dict[system] = dict()

    def calculate_net(d):
        d['cation']['net'] = d['cation']['ILtoCO2'] - d['cation']['CO2toIL']
        d['BF4']['net'] = d['BF4']['ILtoCO2'] - d['BF4']['CO2toIL']
        d['DCA']['net'] = d['DCA']['ILtoCO2'] - d['DCA']['CO2toIL']
        d['PF6']['net'] = d['PF6']['ILtoCO2'] - d['PF6']['CO2toIL']
        d['SCN']['net'] = d['SCN']['ILtoCO2'] - d['SCN']['CO2toIL']
        d['TFA']['net'] = d['TFA']['ILtoCO2'] - d['TFA']['CO2toIL']
        d['Tf2N']['net'] = d['Tf2N']['ILtoCO2'] - d['Tf2N']['CO2toIL']
        d['TfO']['net'] = d['TfO']['ILtoCO2'] - d['TfO']['CO2toIL']
        return d

    covp_dict['cation']['CO2toIL'] = 2.251
    covp_dict['BF4']['CO2toIL'] = 1.264
    covp_dict['DCA']['CO2toIL'] = 2.259
    covp_dict['PF6']['CO2toIL'] = 1.012
    covp_dict['SCN']['CO2toIL'] = 1.323
    covp_dict['TFA']['CO2toIL'] = 1.618
    covp_dict['Tf2N']['CO2toIL'] = 1.603
    covp_dict['TfO']['CO2toIL'] = 2.339

    covp_dict['cation']['ILtoCO2'] = 0.079
    covp_dict['BF4']['ILtoCO2'] = 4.558
    covp_dict['DCA']['ILtoCO2'] = 3.376
    covp_dict['PF6']['ILtoCO2'] = 3.336
    covp_dict['SCN']['ILtoCO2'] = 3.317
    covp_dict['TFA']['ILtoCO2'] = 5.131
    covp_dict['Tf2N']['ILtoCO2'] = 2.493
    covp_dict['TfO']['ILtoCO2'] = 3.009

    covp_dict = calculate_net(covp_dict)

    covp_noCT_dict['cation']['CO2toIL'] = 1.743
    covp_noCT_dict['BF4']['CO2toIL'] = 1.038
    covp_noCT_dict['DCA']['CO2toIL'] = 1.836
    covp_noCT_dict['PF6']['CO2toIL'] = 1.154
    covp_noCT_dict['SCN']['CO2toIL'] = 1.302
    covp_noCT_dict['TFA']['CO2toIL'] = 1.023
    covp_noCT_dict['Tf2N']['CO2toIL'] = 1.246
    covp_noCT_dict['TfO']['CO2toIL'] = 1.941

    covp_noCT_dict['cation']['ILtoCO2'] = 0.039
    covp_noCT_dict['BF4']['ILtoCO2'] = 3.053
    covp_noCT_dict['DCA']['ILtoCO2'] = 2.266
    covp_noCT_dict['PF6']['ILtoCO2'] = 2.221
    covp_noCT_dict['SCN']['ILtoCO2'] = 1.640
    covp_noCT_dict['TFA']['ILtoCO2'] = 2.916
    covp_noCT_dict['Tf2N']['ILtoCO2'] = 1.274
    covp_noCT_dict['TfO']['ILtoCO2'] = 2.048

    covp_noCT_dict = calculate_net(covp_noCT_dict)

    results['covp_dict'] = covp_dict
    results['covp_noCT_dict'] = covp_noCT_dict
    covp_df = pd.DataFrame(covp_dict)
    covp_noCT_df = pd.DataFrame(covp_noCT_dict)
    results['covp_df'] = covp_df
    results['covp_noCT_df'] = covp_noCT_df

    if dump_pd:
        with pd.ExcelWriter('covps.xlsx') as writer:
            covp_df.to_excel(writer, 'CT geometries')
            covp_noCT_df.to_excel(writer, 'no CT geometries')

    return results

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    # Don't make the plots or export data by default.
    parser.add_argument('--do_plot', action='store_true')
    parser.add_argument('--dump_pd', action='store_true')
    args = parser.parse_args()

    results = main(args.do_plot, args.dump_pd)
