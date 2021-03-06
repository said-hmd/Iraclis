from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import iraclis

if sys.version_info[0] > 2:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve
    input = raw_input


def run_test():

    dataset_files = [
        'icy021ljq_raw.fits',
        'icy021l6q_raw.fits',
        'icy021m2q_raw.fits',
        'icy021kuq_raw.fits',
        'icy021lgq_raw.fits',
        'icy021kmq_raw.fits',
        'icy021k1q_raw.fits',
        'icy021kxq_raw.fits',
        'icy021lrq_raw.fits',
        'icy021l0q_raw.fits',
        'icy021lyq_raw.fits',
        'icy021ksq_raw.fits',
        'icy021kfq_raw.fits',
        'icy021llq_raw.fits',
        'icy021jzq_raw.fits',
        'icy021ltq_raw.fits',
        'icy021kkq_raw.fits',
        'icy021laq_raw.fits',
        'icy021lkq_raw.fits',
        'icy021kaq_raw.fits',
        'icy021m3q_raw.fits',
        'icy021ktq_raw.fits',
        'icy021l7q_raw.fits',
        'icy021lfq_raw.fits',
        'icy021klq_raw.fits',
        'icy021kyq_raw.fits',
        'icy021lsq_raw.fits',
        'icy021k0q_raw.fits',
        'icy021lxq_raw.fits',
        'icy021kgq_raw.fits',
        'icy021lmq_raw.fits',
        'icy021luq_raw.fits',
        'icy021k6q_raw.fits',
        'icy021kjq_raw.fits',
        'icy021l4q_raw.fits',
        'icy021m0q_raw.fits',
        'icy021kwq_raw.fits',
        'icy021lhq_raw.fits',
        'icy021kbq_raw.fits',
        'icy021k3q_raw.fits',
        'icy021l9q_raw.fits',
        'icy021kzq_raw.fits',
        'icy021lpq_raw.fits',
        'icy021leq_raw.fits',
        'icy021koq_raw.fits',
        'icy021kdq_raw.fits',
        'icy021lnq_raw.fits',
        'icy021l2q_raw.fits',
        'icy021k8q_raw.fits',
        'icy021kqq_raw.fits',
        'icy021kiq_raw.fits',
        'icy021lcq_raw.fits',
        'icy021k5q_raw.fits',
        'icy021lvq_raw.fits',
        'icy021m1q_raw.fits',
        'icy021kvq_raw.fits',
        'icy021l5q_raw.fits',
        'icy021liq_raw.fits',
        'icy021kcq_raw.fits',
        'icy021lqq_raw.fits',
        'icy021k2q_raw.fits',
        'icy021l8q_raw.fits',
        'icy021ldq_raw.fits',
        'icy021knq_raw.fits',
        'icy021keq_raw.fits',
        'icy021loq_raw.fits',
        'icy021jxq_flt.fits',
        'icy021lzq_raw.fits',
        'icy021kpq_raw.fits',
        'icy021l3q_raw.fits',
        'icy021k9q_raw.fits',
        'icy021lbq_raw.fits',
        'icy021lwq_raw.fits',
        'icy021jyq_raw.fits',
        'icy021k4q_raw.fits',
    ]

    destination = os.path.join(os.path.expanduser('~'), 'iraclis_test_dataset_hatp26b')

    if not os.path.isdir(destination):
        os.mkdir(destination)

    if not os.path.isdir(os.path.join(destination, 'raw_data')):
        for num, dataset_file in enumerate(dataset_files):
            print('{0}/{1}: '.format(num + 1, len(dataset_files)), dataset_file)
            if not os.path.isfile(os.path.join(destination, dataset_file)):
                urlretrieve('https://mast.stsci.edu/portal/Download/file/HST/product/{0}'.format(
                    dataset_file), os.path.join(destination, dataset_file))

    bins_file = os.path.join(destination, 'iraclis_test_dataset_hatp26b_bins.txt')
    w = open(bins_file, 'w')
    w.write('\n'.join([
                '11108 11416 0.985047 -1.385670 1.781030 -0.726723',
                '11416 11709 0.949097 -1.266470 1.640630 -0.675474',
                '11709 11988 0.928715 -1.195690 1.553730 -0.645291',
                '11988 12257 0.903069 -1.109910 1.456180 -0.610773',
                '12257 12522 0.878225 -1.023230 1.361070 -0.578062',
                '12522 12791 0.859841 -0.950740 1.274760 -0.548146',
                '12791 13058 0.849884 -0.896126 1.203900 -0.526715',
                '13058 13321 0.832077 -0.833290 1.125660 -0.494123',
                '13321 13586 0.809188 -0.726211 0.991314 -0.443848',
                '13586 13860 0.795028 -0.641081 0.872551 -0.397134',
                '13860 14140 0.788556 -0.586294 0.802106 -0.373986',
                '14140 14425 0.784454 -0.561833 0.775730 -0.368569',
                '14425 14719 0.772069 -0.460859 0.627183 -0.309136',
                '14719 15027 0.772703 -0.404730 0.517165 -0.259778',
                '15027 15345 0.772846 -0.296638 0.327104 -0.175439',
                '15345 15682 0.798113 -0.256525 0.198611 -0.110803',
                '15682 16042 0.848830 -0.376905 0.274511 -0.125175',
                '16042 16432 0.894871 -0.410984 0.233093 -0.093986'
            ]))
    w.close()

    parameters_file = os.path.join(destination, 'iraclis_test_dataset_hatp26b_parameters.txt')
    w = open(parameters_file, 'w')
    w.write('\n'.join([
                'data_directory                     {0}'.format(destination),
                '# directory path                            ',
                'output_directory_copy              False    ',
                '# directory name/False                      ',
                '                                            ',
                'reduction                          True     ',
                '# True/False                                ',
                'splitting                          False    ',
                '# True/False                                ',
                'extraction                         True     ',
                '# True/False                                ',
                'splitting_extraction               False    ',
                '# True/False                                ',
                'fitting_white                      True     ',
                '# True/False                                ',
                'fitting_spectrum                   True     ',
                '# True/False                                ',
                '                                            ',
                'target_x_offset                    0.0      ',
                '# number                                    ',
                'target_y_offset                    0.0      ',
                '# number                                    ',
                'aperture_lower_extend              -20.0    ',
                '# number                                    ',
                'aperture_upper_extend              20.0     ',
                '# number                                    ',
                'extraction_method                  gauss    ',
                '# gauss/integral                            ',
                'extraction_gauss_sigma             47.0     ',
                '# number                                    ',
                '                                            ',
                'method                             claret   ',
                '# claret/linear/quad/sqrt                   ',
                '                                            ',
                'white_lower_wavelength             10880.0  ',
                '# number/default                            ',
                'white_upper_wavelength             16800.0  ',
                '# number/default                            ',
                'white_ldc1                         0.850033 ',
                '# number/default                            ',
                'white_ldc2                         -0.728096',
                '# number/default                            ',
                'white_ldc3                         0.908153 ',
                '# number/default                            ',
                'white_ldc4                         -0.397691',
                '# number/default                            ',
                '                                            ',
                '# Comment: You can set the above six parameters to default, if you want to use the pre-calculated limb-darkening         ',
                '# coefficients. In this case, the claret limb-darkening method will be used. These coefficients have been calculated for ',
                '# a wavelength range between 10880.0 and 16800.0 Angstroms.                                                              ',
                '                                                                                                                         ',
                'bins_file                          {0}'.format(bins_file),
                '# file path/default_high/default_low/default_vlow                                                                        ',
                '                                                                                                                         ',
                '# Comment: You can set the above parameter to default_high, default_low or default_vlow. In this case, the claret        ',
                '# limb-darkening method will be used. Be careful to avoid conflicts, as the limb-darkening method used between spectral  ',
                '# and white light curves should be the same.    ',
                '                                                ',
                'planet                             HAT-P-26 b   ',
                '# name/auto                                     ',
                'star_teff                          5079         ',
                '# number/auto                                   ',
                'star_logg                          4.56         ',
                '# number/auto                                   ',
                'star_meta                          -0.04        ',
                '# number/auto                                   ',
                'rp_over_rs                         0.0715       ',
                '# number/auto                                   ',
                'fp_over_fs                         0.0001       ',
                '# number/auto                                   ',
                'period                             4.234515     ',
                '# number/auto                                   ',
                'sma_over_rs                        13.44        ',
                '# number/auto                                   ',
                'eccentricity                       0.0          ',
                '# number/auto                                   ',
                'inclination                        88.6         ',
                '# number/auto                                   ',
                'periastron                         0.0          ',
                '# number/auto                                   ',
                'mid_time                           2455304.65118',
                '# number/auto                                   ',
                '                                                ',
                '# Comment: You can set any of the above 12 parameters to auto, to use the data from the Open Exoplanet Catalogue.',
                '                                        ',
                'apply_up_down_stream_correction    False ',
                '# True/False                            ',
                'exclude_initial_orbits             1     ',
                '# number                                ',
                'exclude_final_orbits               0     ',
                '# number                                ',
                'exclude_initial_orbit_points       0     ',
                '# number                                ',
                '                                        ',
                'mcmc_iterations                    150000',
                '# number                                ',
                'mcmc_walkers                       200   ',
                '# number                                ',
                'mcmc_burned_iterations             50000 ',
                '# number                                ',
                'spectral_mcmc_iterations           50000 ',
                '# number                                ',
                'spectral_mcmc_walkers              100   ',
                '# number                                ',
                'spectral_mcmc_burned_iterations    20000 ',
                '# number                                ',
                '                                       ',
                'first_orbit_ramp                   True  ',
                '# True/False                            ',
                'second_order_ramp                  False ',
                '# True/False                            ',
                'mid_orbit_ramps                    True  ',
                '# True/False                            ',
                '                                        ',
                'fit_ldc1                           False ',
                '# True/False                            ',
                'fit_ldc2                           False ',
                '# True/False                            ',
                'fit_ldc3                           False ',
                '# True/False                            ',
                'fit_ldc4                           False ',
                '# True/False                            ',
                'fit_inclination                    False ',
                '# True/False                            ',
                'fit_sma_over_rs                    False ',
                '# True/False                            ',
                'fit_mid_time                       True  '
            ]))
    w.close()

    os.system('iraclis -p {0}'.format(parameters_file))
