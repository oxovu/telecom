import numpy as np

ib = np.matrix([[1, 0, 0, 0, 1, 1, 0],
                [0, 1, 0, 0, 1, 0, 1],
                [0, 0, 1, 0, 0, 1, 1],
                [0, 0, 0, 1, 1, 1, 1]])

ht = np.matrix([[0, 1, 1],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1],
                [0, 0, 1],
                [0, 1, 0],
                [1, 0, 0]]
               )


def normalization(matrix):
    for i in range(matrix.__len__()):
        matrix[i] = matrix[i] % 2
    return matrix


def fix(m, syndrome):
    mistake = syndrome[0, 0] * 4 + syndrome[0, 1] * 2 + syndrome[0, 2]
    if mistake == 1:
        mistake = 4
    elif mistake == 2:
        mistake = 5
    elif mistake == 3:
        mistake = 0
    elif mistake == 4:
        mistake = 6
    elif mistake == 5:
        mistake = 1
    elif mistake == 6:
        mistake = 2
    elif mistake == 7:
        mistake = 3
    if mistake == 0:
        return m
    result = m
    result[0, mistake] = 0 if result[0, mistake] == 1 else 1
    return result


if __name__ == "__main__":
    g = np.matrix([[0, 1, 0, 1]])

    print("message: ", g)

    hamming = g * ib
    hamming.transpose()
    hamming = normalization(hamming)

    print("hamming code for this message: ", hamming)

    syndrome = hamming * ht
    syndrome.transpose()
    syndrome = normalization(syndrome)

    print("syndrome for this code: ", syndrome)

    hamming[0, 4] = 0 if hamming[0, 4] == 1 else 1
    print("make mistake in 5 digit: ", hamming)

    syndrome = hamming * ht
    syndrome.transpose()
    syndrome = normalization(syndrome)

    print("syndrome for code with error: ", syndrome)
    print("fix the mistake: ", fix(hamming, syndrome))
