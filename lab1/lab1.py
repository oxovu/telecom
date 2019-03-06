from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np


def get_sin_sig(t, freeq, ampl):
    return ampl * np.cos(2 * np.pi * freeq * t)


def get_rect_sig(t, freeq, ampl):
    return ampl * np.sign(np.cos(2 * np.pi * freeq * t))


def plot_graphic(x, y, title, x_label="x", y_label="y", show=True, save=False):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x, y)
    if show:
        plt.show()
    if save:
        plt.savefig('graphics/' + title + '.png')
        plt.close()


if __name__ == '__main__':

    freeq = 20
    ampl = 1
    fs = 1000  # sampling rate
    ts = 1.0 / fs
    n = 1 << 13  # number of fft points
    t = np.arange(0, n * ts, ts)  # time vector
    pts_num = 100
    signals = [get_sin_sig(t, freeq, ampl), get_rect_sig(t, freeq, ampl)]
    functions = ['sinus', 'rectangle']
    for sig, title in zip(signals, functions):
        sig_fft = np.fft.fft(sig) / n * 2  # Compute the one-dimensional discrete Fourier Transform.
        fft_freq = np.fft.fftfreq(n, ts)  # Return the Discrete Fourier Transform sample frequencies.

        plot_graphic(x=t[:pts_num], y=sig[:pts_num], title=title + '_signal', x_label='time(S)',
                     y_label='amplitude (V)')
        plot_graphic(x=fft_freq[:fs], y=abs(sig_fft)[:fs], title=title + '_spectrum', x_label='frequency (Hz)',
                     y_label='amplitude (V)')
