#!/usr/bin/env python

from __future__ import print_function

import os
import re
import pickle

from collections import OrderedDict

import numpy as np
import numpy.linalg as npl

from cclib.parser import ccopen

import matplotlib as mpl
# mpl.rc(usetex=True)
mpl.use("Agg")
import matplotlib.pyplot as plt


labels = OrderedDict([
    ('blyp', 'BLYP'),
    ('tpss', 'TPSS'),
    ('b3lyp', 'B3LYP'),
    ('wb97x-d', r'$\omega$B97X-D'),
    ('hf', 'HF'),
    ('ri-mp2', 'RI-MP2'),
])


def sort(snapnums_dict, results_dict):
    assert labels.keys() == snapnums_dict.keys() == results_dict.keys()
    for k in labels:
        sorting_indices = [i[0] for i in sorted(enumerate(snapnums_dict[k]),
                                                key=lambda x: x[1])]
        sorted_results = [i[1] for i in sorted(zip(sorting_indices, results_dict[k]),
                                               key=lambda x: x[0])]
        sorted_snapnums = [i[1] for i in sorted(zip(sorting_indices, snapnums_dict[k]),
                                                key=lambda x: x[0])]
        # assert sorted_snapnums == list(range(min(snapnums_dict[k]), max(snapnums_dict[k]) + 1))
        snapnums_dict[k] = sorted_snapnums
        results_dict[k] = sorted_results
    return


def get_single_snapshot_results(snapnum, snapnums_dict, results_dict):
    assert labels.keys() == snapnums_dict.keys() == results_dict.keys()
    single_dict = []
    for k in labels:
        idx = snapnums_dict[k].index(snapnum)
        single_result = results_dict[k][idx]
        single_dict.append((k, single_result))
    return OrderedDict(single_dict)


def plot_single_snapshot_dipoles(snapnum, snapnums_d, dipoles, inp_fig=None, inp_ax=None):

    dipoles_snap = get_single_snapshot_results(snapnum, snapnums_d, dipoles)

    fig, ax = plt.subplots()
    if inp_fig:
        fig = inp_fig
    if inp_ax:
        ax = inp_ax

    plot_list = [npl.norm(dipole) for dipole in dipoles_snap.values()]
    print(plot_list)
    ax.plot(ticks,
            plot_list,
            label=snapnum,
            marker='o')

    if not inp_ax:
        ax.tick_params(direction='out', top='off', right='off')
        ax.set_xticklabels(list(labels.values()))
        ax.set_xlabel('method', fontsize='large')
        ax.set_ylabel("total dipole moment (Debye)", fontsize='large')
        ax.set_title("snapshot {}".format(snapnum), fontsize='large')
        # ax.legend(loc='best', fancybox=True, framealpha=0.50)
    if not inp_fig:
        print('Saving dipole_snap{}.pdf'.format(snapnum))
        fig.savefig('dipole_snap{}.pdf'.format(snapnum), bbox_inches='tight')

        plt.close(fig)

    return


def plot_single_snapshot_frequencies(snapnum, snapnums_f, frequencies, inp_fig=None, inp_ax=None):

    frequencies_snap = get_single_snapshot_results(snapnum, snapnums_f, frequencies)

    fig, ax = plt.subplots()
    if inp_fig:
        fig = inp_fig
    if inp_ax:
        ax = inp_ax

    plot_list = [frequencies_snap[k] for k in labels]
    # plot_list = [frequency for frequency in frequencies_snap.values()]
    print(plot_list)
    ax.plot(ticks,
            plot_list,
            label=snapnum,
            marker='o')

    if not inp_ax:
        ax.tick_params(direction='out', top='off', right='off')
        ax.set_xticklabels(list(labels.values()))
        ax.set_xlabel('method', fontsize='large')
        ax.set_ylabel(r'$\nu_{3}$ frequency (cm$^{-1}$)', fontsize='large')
        ax.set_title("snapshot {}".format(snapnum), fontsize='large')
        # ax.legend(loc='best', fancybox=True, framealpha=0.50)
    if not inp_fig:
        print('Saving frequency_snap{}.pdf'.format(snapnum))
        fig.savefig('frequency_snap{}.pdf'.format(snapnum), bbox_inches='tight')

        plt.close(fig)

    return


def get_outputfiles_from_path(path):
    outputfiles = []
    # Walk the directory tree to find all potential output files.
    for (root, dirs, files) in os.walk(path):
        for f in files:
            if f.endswith(".out"):
                outputfiles.append(os.path.join(root, f))
    return sorted(outputfiles)


def get_CO2_frequencies(outputfilenames):

    snapnums = []
    CO2_frequencies = []
    CO2_intensities = []

    for outputfilename in outputfilenames:
        print("Parsing frequencies from {}".format(outputfilename))

        job = ccopen(outputfilename)
        try:
            data = job.parse()
        except:
            # Is this the right control flow statement?
            continue
        # geometry = data.atomcoords[-1]
        # atoms = data.atomnos
        # start_indices = find_CO2_atom_indices(atoms, geometry)
        # assert isinstance(start_indices, list)
        try:
            vibfreqs = data.vibfreqs
            vibirs = data.vibirs
        except AttributeError:
            # Is this the correct control flow statement?
            continue
        # Assumption!
        # start_index = start_indices[0]
        # Assumption?
        start_index = len(data.atomnos) - 3
        # mode_indices = find_CO2_mode_indices(start_index, vibdisps, thresh=0.50)
        mode_indices = [2]
        # freqs = [vibfreqs[modeidx] for modeidx in mode_indices]
        # freqs = filter(lambda x: x > 0.0, freqs)
        # print(freqs)
        # Let's only take the last one...
        # print(outputfilename)
        CO2_frequencies.append(vibfreqs[mode_indices[-1]])
        CO2_intensities.append(vibirs[mode_indices[-1]])
        snapnum = int(re.search('drop_(\d+)_', outputfilename).groups()[0])
        snapnums.append(snapnum)

    return CO2_frequencies, CO2_intensities, snapnums


def get_dipoles(outputfilenames):

    dipoles = []
    snapnums = []

    for outputfilename in outputfilenames:

        with open(outputfilename) as outputfile:
            print("Parsing dipole from {}".format(outputfilename))
            for line in outputfile:
                if 'Dipole Moment (Debye)' in line:
                    line = next(outputfile)
                    dipole = list(map(float, line.split()[1::2]))
                    dipoles.append(dipole)
                    snapnum = int(re.search('drop_(\d+)_', outputfilename).groups()[0])
                    snapnums.append(snapnum)
                    # Only take the first one! This avoids problems
                    # when parsing numerical frequency runs.
                    break

    return dipoles, snapnums


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("file_operation", choices=("none", "save", "read"))
    parser.add_argument("parse_operation", choices=("none", "save", "read"))

    args = parser.parse_args()

    if args.file_operation == "save":
        print("Trying to find output files...")
        basedir = "/home/eric/Chemistry/calc.sgr/droplets/incorrect/droplets_in_box"
        outputfiles_blyp = get_outputfiles_from_path(os.path.join(basedir, "inputs_blyp_6-31gdp_gas_chelpg_freq_0qm_numerical"))
        outputfiles_b3lyp = get_outputfiles_from_path(os.path.join(basedir, "inputs_b3lyp_6-31gdp_gas_chelpg_freq_0qm_numerical"))
        outputfiles_hf = get_outputfiles_from_path(os.path.join(basedir, "inputs_hf_6-31gdp_gas_chelpg_freq_0qm_numerical"))
        outputfiles_rimp2 = get_outputfiles_from_path(os.path.join(basedir, "inputs_ri-mp2_6-31gdp_gas_chelpg_freq_0qm_numerical"))
        outputfiles_wb97xd = get_outputfiles_from_path(os.path.join(basedir, "inputs_wb97x-d_6-31gdp_gas_chelpg_freq_0qm_numerical"))
        outputfiles_tpss = get_outputfiles_from_path(os.path.join(basedir, "inputs_tpss_6-31gdp_gas_chelpg_freq_0qm_numerical"))
        outputfiles = OrderedDict([
            ('blyp', outputfiles_blyp),
            ('b3lyp', outputfiles_b3lyp),
            ('hf', outputfiles_hf),
            ('ri-mp2', outputfiles_rimp2),
            ('wb97x-d', outputfiles_wb97xd),
            ('tpss', outputfiles_tpss),
        ])
        with open('outputfiles.pypickle', 'wb') as picklefile:
            pickle.dump(outputfiles, picklefile)
    elif args.file_operation == "read":
        print("Reading list of output files from: {}".format(os.path.abspath("outputfiles.pypickle")))
        with open("outputfiles.pypickle", "rb") as picklefile:
            outputfiles = pickle.load(picklefile)
    elif args.file_operation == "none":
        pass
    else:
        raise Exception

    if args.parse_operation == "save":
        print("Extracting valuable information from outputs...")
        print("Parsing frequencies/intensities...")
        frequencies_blyp, intensities_blyp, snapnums_f_blyp = get_CO2_frequencies(outputfiles_blyp)
        frequencies_b3lyp, intensities_b3lyp, snapnums_f_b3lyp = get_CO2_frequencies(outputfiles_b3lyp)
        frequencies_hf, intensities_hf, snapnums_f_hf = get_CO2_frequencies(outputfiles_hf)
        frequencies_rimp2, intensities_rimp2, snapnums_f_rimp2 = get_CO2_frequencies(outputfiles_rimp2)
        frequencies_wb97xd, intensities_wb97xd, snapnums_f_wb97xd = get_CO2_frequencies(outputfiles_wb97xd)
        frequencies_tpss, intensities_tpss, snapnums_f_tpss = get_CO2_frequencies(outputfiles_tpss)
        print("Parsing dipoles...")
        dipoles_blyp, snapnums_d_blyp = get_dipoles(outputfiles_blyp)
        dipoles_b3lyp, snapnums_d_b3lyp = get_dipoles(outputfiles_b3lyp)
        dipoles_hf, snapnums_d_hf = get_dipoles(outputfiles_hf)
        dipoles_rimp2, snapnums_d_rimp2 = get_dipoles(outputfiles_rimp2)
        dipoles_wb97xd, snapnums_d_wb97xd = get_dipoles(outputfiles_wb97xd)
        dipoles_tpss, snapnums_d_tpss = get_dipoles(outputfiles_tpss)
        frequencies = OrderedDict([
            ('blyp', frequencies_blyp),
            ('b3lyp', frequencies_b3lyp),
            ('hf', frequencies_hf),
            ('ri-mp2', frequencies_rimp2),
            ('wb97x-d', frequencies_wb97xd),
            ('tpss', frequencies_tpss),
        ])
        intensities = OrderedDict([
            ('blyp', intensities_blyp),
            ('b3lyp', intensities_b3lyp),
            ('hf', intensities_hf),
            ('ri-mp2', intensities_rimp2),
            ('wb97x-d', intensities_wb97xd),
            ('tpss', intensities_tpss),
        ])
        dipoles = OrderedDict([
            ('blyp', dipoles_blyp),
            ('b3lyp', dipoles_b3lyp),
            ('hf', dipoles_hf),
            ('ri-mp2', dipoles_rimp2),
            ('wb97x-d', dipoles_wb97xd),
            ('tpss', dipoles_tpss),
        ])
        snapnums_f = OrderedDict([
            ('blyp', snapnums_f_blyp),
            ('b3lyp', snapnums_f_b3lyp),
            ('hf', snapnums_f_hf),
            ('ri-mp2', snapnums_f_rimp2),
            ('wb97x-d', snapnums_f_wb97xd),
            ('tpss', snapnums_f_tpss),
        ])
        snapnums_d = OrderedDict([
            ('blyp', snapnums_d_blyp),
            ('b3lyp', snapnums_d_b3lyp),
            ('hf', snapnums_d_hf),
            ('ri-mp2', snapnums_d_rimp2),
            ('wb97x-d', snapnums_d_wb97xd),
            ('tpss', snapnums_d_tpss),
        ])
        with open('frequencies.pypickle', 'wb') as picklefile:
            pickle.dump(frequencies, picklefile)
        with open('intensities.pypickle', 'wb') as picklefile:
            pickle.dump(intensities, picklefile)
        with open('dipoles.pypickle', 'wb') as picklefile:
            pickle.dump(dipoles, picklefile)
        with open('snapnums_frequencies.pypickle', 'wb') as picklefile:
            pickle.dump(snapnums_f, picklefile)
        with open('snapnums_dipoles.pypickle', 'wb') as picklefile:
            pickle.dump(snapnums_d, picklefile)
    elif args.parse_operation == "read":
        print("Reading frequency data from: {}".format(os.path.abspath('frequencies.pypickle')))
        with open('frequencies.pypickle', 'rb') as picklefile:
            frequencies = pickle.load(picklefile)
        print("Reading intensity data from: {}".format(os.path.abspath('intensities.pypickle')))
        with open('intensities.pypickle', 'rb') as picklefile:
            intensities = pickle.load(picklefile)
        print("Reading dipole data from: {}".format(os.path.abspath('dipoles.pypickle')))
        with open('dipoles.pypickle', 'rb') as picklefile:
            dipoles = pickle.load(picklefile)
        print("Reading snapshot number data from: {}".format(os.path.abspath('snapnums_frequencies.pypickle')))
        with open('snapnums_frequencies.pypickle', 'rb') as picklefile:
            snapnums_f = pickle.load(picklefile)
        print("Reading snapshot number data from: {}".format(os.path.abspath('snapnums_dipoles.pypickle')))
        with open('snapnums_dipoles.pypickle', 'rb') as picklefile:
            snapnums_d = pickle.load(picklefile)
        # sort(frequencies, snapnums_f)
        # sort(intensities, snapnums_f)
        # sort(dipoles, snapnums_d)
    elif args.parse_operation == "none":
        pass
    else:
        raise Exception

    ticks = range(len(labels))

    cutoff = 300
    means_frequencies = [np.mean(frequencies[k][:cutoff]) for k in labels]
    means_dipole_moments = [np.mean([npl.norm(dipole) for dipole in dipoles[k][:cutoff]]) for k in labels]

    ##################################################

    fig, ax = plt.subplots()

    ax.plot(ticks, means_frequencies, marker='s', color='green')

    ax.set_xticklabels(list(labels.values()))
    ax.set_xlabel('method', fontsize='large')
    ax.set_ylabel(r'$\nu_{3}$ frequency (cm$^{-1}$)', fontsize='large')

    # ax.legend(fancybox=True, loc='best', framealpha=0.50)

    fig.savefig('frequencies_line.pdf', bbox_inches='tight')

    ##################################################

    fig, ax = plt.subplots()

    ax.plot(ticks, means_dipole_moments, marker='s', color='green')

    ax.set_xticklabels(list(labels.values()))
    ax.set_xlabel('method', fontsize='large')
    ax.set_ylabel('total dipole moment (Debye)', fontsize='large')

    # ax.legend(fancybox=True, loc='best', framealpha=0.50)

    fig.savefig('dipole_moments_line.pdf', bbox_inches='tight')

    ##################################################

    ax1_color = 'blue'
    ax2_color = 'green'

    fig, ax1 = plt.subplots()

    ax1.plot(ticks, means_frequencies, marker='s', linestyle='-', color=ax1_color)

    ax1.set_ylabel(r'$\nu_{3}$ frequency (cm$^{-1}$)', fontsize='large')

    for tl in ax1.get_yticklabels():
        tl.set_color(ax1_color)

    ax2 = ax1.twinx()

    ax2.plot(ticks, means_dipole_moments, marker='*', linestyle='--', color=ax2_color)

    ax2.set_ylabel('total dipole moment (Debye)', fontsize='large')

    ax2.set_ylim(ax2.get_ylim()[::-1])

    for tl in ax2.get_yticklabels():
        tl.set_color(ax2_color)

    ax1.set_xticklabels(list(labels.values()))
    ax1.set_xlabel('method', fontsize='large')

    ax1.tick_params(direction='out', top='off', right='off')
    ax2.tick_params(direction='out', top='off', left='off')

    fig.savefig('frequencies_dipole_moments_combined_line.pdf', bbox_inches='tight')

    ##################################################

    snapnums = (50, 100, 150, 200, 250)
    # snapnums = [random.randrange(1, cutoff + 1) for _ in range(5)]

    # for snapnum in snapnums:
    #     print(snapnum, get_single_snapshot_results(snapnum, snapnums_f, frequencies))

    # for snapnum in snapnums:
    #     plot_single_snapshot_frequencies(snapnum, snapnums_f, frequencies)
    #     plot_single_snapshot_dipoles(snapnum, snapnums_d, dipoles)

    ##################################################

    fig, ax = plt.subplots()
    for snapnum in snapnums:
        plot_single_snapshot_dipoles(snapnum, snapnums_d, dipoles, inp_ax=ax, inp_fig=fig)
    ax.tick_params(direction='out', top='off', right='off')
    ax.set_xticklabels(list(labels.values()))
    ax.set_xlabel('method', fontsize='large')
    ax.set_ylabel("total dipole moment (Debye)", fontsize='large')
    ax.legend(loc='best', fancybox=True, framealpha=0.50)
    print('Saving dipole_snapshots.pdf')
    fig.savefig('dipole_snapshots.pdf', bbox_inches='tight')

    plt.close(fig)

    fig, ax = plt.subplots()
    for snapnum in snapnums:
        plot_single_snapshot_frequencies(snapnum, snapnums_d, frequencies, inp_ax=ax, inp_fig=fig)
    ax.tick_params(direction='out', top='off', right='off')
    ax.set_xticklabels(list(labels.values()))
    ax.set_xlabel('method', fontsize='large')
    ax.set_ylabel(r'$\nu_{3}$ frequency (cm$^{-1}$)', fontsize='large')
    ax.legend(loc='best', fancybox=True, framealpha=0.50)
    print('Saving frequency_snapshots.pdf')
    fig.savefig('frequency_snapshots.pdf', bbox_inches='tight')

    plt.close(fig)

    ###

    cutoff = 100
    ticklabels = list(snapnums_f.values())[:cutoff]
    print(type(ticklabels))

    fig, ax = plt.subplots()

    for k in labels:
        ax.plot(frequencies[k][:cutoff], label=labels[k])

    ax.set_xticks(ticklabels)
    ax.set_xticklabels(ticklabels)
    ax.set_xlabel('snapshot #', fontsize='large')
    ax.set_ylabel(r'$\nu_{3}$ frequency (cm$^{-1}$)', fontsize='large')

    ax.legend(fancybox=True, loc='upper right', framealpha=0.50)

    fig.savefig('frequencies.pdf', bbox_inches='tight')

    ##################################################
