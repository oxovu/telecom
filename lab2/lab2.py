from __future__ import print_function
from timeit import default_timer as timer
from scipy import signal
import numpy as np

if __name__ == '__main__':

    sig = np.array([0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0])
    sync_mess = np.array([1, 0, 1])
    p_size = 8

    for method in ['fft', 'direct', 'auto']:
        t = timer()
        corr = signal.correlate(sig, sync_mess, mode='full', method=method)
        elapsed = timer() - t
        print("\ncorrelation method ", method)
        print(corr)
        print("time = ", elapsed)

    sy_mess_end = 0
    max_corr = 0
    i = 0
    for n in corr:
        if n > max_corr:
            max_corr = n
            sy_mess_end = i
        i += 1

    p_start = sy_mess_end + 1
    p_end = p_start + p_size
    p = sig[p_start:p_end]

    print("\nsync_mess = sig[%.d : %.d] = " % (p_start, p_start + p_size),
          sig[p_start - sync_mess.__len__():p_start])
    print("package start = ", p_start)
    print("package = ", p)

