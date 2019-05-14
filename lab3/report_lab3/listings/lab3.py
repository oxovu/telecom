from __future__ import print_function
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


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
    ampl = 1
    fs = 1000
    ts = 1.0 / fs
    n = 1 << 13

    t = np.arange(0, n * ts, step=ts)

    sig = ampl * np.sin(2 * np.pi * sig_freq * t)

    noise = np.random.normal(0, 0.5, n)
    sig_noise = sig + noise

    plot_graphic(
        x=t[:int((n - 1) / 2)], y=sig_noise[:int((n - 1) / 2)],
        x_label='time(S)', y_label='amplitude (V)',
        xlim=[0, 1], ylim=[-2, 2],
        show=False
    )

    plot_graphic(
        x=t[:int((n - 1) / 2)], y=sig[:int((n - 1) / 2)],
        x_label='time(S)', y_label='amplitude (V)',
        xlim=[0, 1], ylim=[-2, 2],
        show=False
    )
    plt.legend(('noise', 'original'), loc='upper right', shadow=True)
    # plt.savefig('graphics/noise&sig.png')
    plt.show()

    nyq = 0.5 * fs
    Wn = 2 * sig_freq / nyq
    N = 6

    filt_func = signal.butter
    fnum, fdenom = filt_func(N=N, Wn=Wn)
    filtered = signal.filtfilt(fnum, fdenom, sig_noise)

    plot_graphic(
        x=t[:int((n - 1) / 2)], y=sig[:int((n - 1) / 2)],
        x_label='time(S)', y_label='signal',
        xlim=[0, 1], ylim=[-2, 2],
        show=False)

    plot_graphic(
        x=t[:int((n - 1) / 2)], y=filtered[:int((n - 1) / 2)],
        x_label='time(S)', y_label='signal',
        xlim=[0, 1], ylim=[-2, 2],
        show=False)

    plt.legend(('signal', 'filtered signal'), loc='upper right', shadow=False)
    # plt.savefig('graphics/filtered.png')
    plt.show()

    fft_freq = np.fft.fftfreq(n, ts)
    sig_fft = np.fft.fft(sig_noise) / n * 2

    plot_graphic(
        x=fft_freq[:int((n - 1) / 2)], y=abs(sig_fft)[:int((n - 1) / 2)],
        x_label='frequency (Hz)', y_label='amplitude (V)',
        xlim=[0, 50],
        show=False
    )

    fft_freq = np.fft.fftfreq(n, ts)
    sig_fft = np.fft.fft(filtered) / n * 2

    plot_graphic(
        x=fft_freq[:int((n - 1) / 2)], y=abs(sig_fft)[:int((n - 1) / 2)],
        x_label='frequency (Hz)', y_label='amplitude (V)',
        xlim=[0, 50],
        show=False
    )

    plt.legend(('signal', 'filtered signal'), loc='upper right', shadow=False)
    # plt.savefig('graphics/sector.png')
    plt.show()
