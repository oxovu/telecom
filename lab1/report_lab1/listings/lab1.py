from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def get_sin_sig(t, freq, ampl):
    return ampl * np.cos(2 * np.pi * freq * t)


def get_rect_sig(t, freq, ampl):
    return ampl * signal.square(2 * np.pi * freq * t)


def get_triang_sig(t, freq, ampl):
    return ampl * signal.sawtooth(2 * np.pi * freq * t)


def plot_graphic(x, y, title, x_label="x", y_label="y", xlim=None, ylim=None, show=False, save=False):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x, y)

    if xlim != None:
        plt.xlim(xlim[0], xlim[1])
    if ylim != None:
        plt.ylim(ylim[0], ylim[1])

    if show:
        plt.show()
    if save:
        plt.savefig('graphics/' + title + '.png')
        plt.close()


if __name__ == '__main__':

    sig_freq = 5  # frequency of original signal
    ampl = 1  # amplitude of original signal
    fs = 1000  # sampling rate
    ts = 1.0 / fs  # sampling interval
    n = 1 << 13  # number of fft points, pick power of 2

    t = np.arange(0, n * ts, step=ts)  # time vector
    signals = \
        [
            get_sin_sig(t, sig_freq, ampl),
            get_rect_sig(t, sig_freq, ampl),
            get_triang_sig(t, sig_freq, ampl)
        ]

    # Parameters for graphics
    functions_names = ['sinus_', 'rectangle_', 'triangle_']
    show = False
    save = not show

    # Spectrum calculating and plotting
    for sig, title in zip(signals, functions_names):
        fft_freq = np.fft.fftfreq(n, ts)  # discrete Fourier Transform frequencies

        sig_fft = np.fft.fft(sig) / n * 2  # discrete Fourier Transform ( / n * 2 - normalization)

        # [:(n - 1) / 2], because second half it's mirror image of first half
        plot_graphic(
            x=t[:int((n - 1) / 2)], y=sig[:int((n - 1) / 2)],
            title=title + 'signal',
            x_label='time(S)', y_label='signal',
            xlim=[0, 1],
            show=show, save=save
        )

        plot_graphic(
            x=fft_freq[:int((n - 1) / 2)], y=abs(sig_fft)[:int((n - 1) / 2)],
            title=title + 'spectrum',
            x_label='frequency (Hz)', y_label='amplitude (V)',
            xlim=[0, 100],
            show=show, save=save
        )
