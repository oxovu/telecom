from __future__ import print_function
import numpy as np
from scipy.signal import butter, filtfilt, hilbert
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')


def plot_graphic(x, y, title=None, x_label="x", y_label="y", gr_form='-', xlim=None, ylim=None, show=False, save=False):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if title != None:
        plt.title(title)

    plt.plot(x, y, gr_form)

    if xlim != None:
        plt.xlim(xlim[0], xlim[1])
    if ylim != None:
        plt.ylim(ylim[0], ylim[1])

    if show:
        plt.show()
    if save:
        plt.savefig(title + '.png')
        plt.close()


if __name__ == '__main__':
    sig_freq = 5
    T = 1.0 / sig_freq
    sig_ampl = 1
    fs = 1000
    ts = 1.0 / fs
    n = 1 << 13

    t = np.arange(0, n * ts, step=ts)
    sig = sig_ampl * np.sin(2 * np.pi * sig_freq * t)

    carr_freq = sig_freq * 10
    carr_ampl = sig_ampl
    carr_sig = carr_ampl * np.sin(2 * np.pi * carr_freq * t)

    m = sig_ampl / carr_ampl
    singleton_mod = (1 + m * sig_ampl * sig) * carr_ampl * carr_sig
    supp_carr_mod = sig_ampl * carr_ampl * sig * carr_sig
    single_sideband_mod = hilbert(sig) * np.cos(2 * np.pi * carr_freq * t) - hilbert(sig) * carr_sig

    order = 5
    normal_cutoff = sig_freq / carr_freq

    fnum, fdenom = butter(order, normal_cutoff)
    singleton_demodulated = filtfilt(fnum, fdenom, abs(singleton_mod))
    suppressed_carried_demod = supp_carr_mod * carr_ampl * carr_sig
    sig_xlim = (0, 0.5)

    fft_freq = np.fft.fftfreq(n, ts)

    singleton_modulated_fft = \
        abs(np.fft.fft(singleton_mod)) / n * 2
    singleton_demodulated_fft = abs(np.fft.fft(singleton_demodulated)) / n * 2

    suppressed_carried_mod_fft = abs(np.fft.fft(supp_carr_mod)) / n * 2
    suppressed_carried_demod_fft = abs(np.fft.fft(suppressed_carried_demod)) / n * 2

    single_sideband_mod_fft = abs(np.fft.fft(single_sideband_mod)) / n * 2

    plot_graphic(t, singleton_mod,
                 xlim=sig_xlim,
                 x_label='time (s)', y_label='amplitude (V)', show=False)

    plot_graphic(t, singleton_demodulated,
                 xlim=sig_xlim,
                 x_label='time (s)', y_label='amplitude (V)', show=False)

    plt.legend(("Singleton Modulated sine wave", "Singleton Demodulated sine wave"), loc='upper right')
    plt.savefig('graphics/1.png')
    plt.show()
    plot_graphic(fft_freq, singleton_modulated_fft,
                 xlim=[0, 100],
                 x_label='frequency (hz)', y_label='amplitude (V)', show=False)

    plot_graphic(fft_freq, singleton_demodulated_fft,
                 xlim=[0, 100],
                 x_label='frequency (hz)', y_label='amplitude (V)', show=False)

    plt.legend(("Singleton Modulated sine wave", "Singleton Demodulated sine wave"), loc='upper right')
    plt.savefig('graphics/2.png')
    plt.show()
    plot_graphic(t, supp_carr_mod,
                 xlim=sig_xlim,
                 x_label='time (s)', y_label='amplitude (V)', show=False)

    plot_graphic(t, suppressed_carried_demod,
                 xlim=sig_xlim,
                 x_label='time (s)', y_label='amplitude (V)', show=False)

    plt.legend(("Suppressed carrier Modulated sine wave", "Suppressed carrier Demodulated sine wave"),
               loc='upper right')
    plt.savefig('graphics/3.png')
    plt.show()
    plot_graphic(fft_freq, suppressed_carried_mod_fft,
                 xlim=[0, 200],
                 x_label='frequency (hz)', y_label='amplitude (V)', show=False)

    plot_graphic(fft_freq, suppressed_carried_demod_fft,
                 xlim=[0, 200],
                 x_label='frequency (hz)', y_label='amplitude (V)', show=False)

    plt.legend(("Suppressed carrier Modulated sine wave", "Suppressed carrier Demodulated sine wave"),
               loc='upper right')
    plt.savefig('graphics/4.png')
    plt.show()
    plot_graphic(t, single_sideband_mod,
                 xlim=sig_xlim,
                 x_label='time (s)', y_label='amplitude (V)', show=False)

    plt.legend(("Single sideband Modulated sine wave",), loc='upper right')
    plt.savefig('graphics/5.png')
    plt.show()
    plot_graphic(fft_freq, single_sideband_mod_fft,
                 xlim=[0, 100],
                 title='Single sideband carrier Modulated sine wave',
                 x_label='frequency (hz)', y_label='amplitude (V)', show=False)

    plt.legend(("Single sideband carrier Modulated sine wave",), loc='upper right')
    plt.savefig('graphics/6.png')
    plt.show()
