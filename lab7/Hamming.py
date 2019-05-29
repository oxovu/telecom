import numpy as np


def hamming(m):
    b0 = parity(m, [0, 2, 3])
    b1 = parity(m, [0, 1, 3])
    b2 = parity(m, [0, 1, 2])

    return [b0, b1, m[3], b2, m[2], m[1], m[0]]


def parity(s, indexes):
    return int(s[indexes[0]]) ^ int(s[indexes[1]]) ^ int(s[indexes[2]])


def syndrome(num, indexes):
    return int(num[indexes[0]]) ^ int(num[indexes[1]]) ^ int(num[indexes[2]] ^ int(num[indexes[3]]))


def full_syndrome(m):
    s0 = syndrome(m, [0, 2, 4, 6])
    s1 = syndrome(m, [1, 2, 5, 6])
    s2 = syndrome(m, [3, 4, 5, 6])
    return np.array([s2, s1, s0])


def fix(m, syndrome):
    mistake = syndrome[0] * 4 + syndrome[1] * 2 + syndrome[2] - 1
    if mistake == 0:
        return m
    result = m
    result[mistake] = 0 if result[mistake] == 1 else 1
    return result


if __name__ == "__main__":
    message = np.array([1, 0, 1, 0])
    hamming = hamming(message)

    print("message: ", message)
    print("hamming code for this message: ", hamming)
    print("syndrome for this code: ", full_syndrome(hamming))
    hamming[4] = 0 if hamming[4] == 1 else 1
    print("make mistake in 5 digit: ", hamming)
    print("syndrome for code with error: ", full_syndrome(hamming))
    print("fix the mistake: ", fix(hamming, full_syndrome(hamming)))
