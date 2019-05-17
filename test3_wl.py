import pywt
import matplotlib.pyplot as plt

"""
mode = ['zero', 'constant', 'symmetric', 'reflect', 'periodic', 'smooth', 'periodization']
"""


def waveletdec(signal, coef_type='d', wname='sym7', level=7, mode='symmetric'):
    N = len(signal)
    w = pywt.Wavelet(wname)
    a = signal
    ca = []
    cd = []
    for i in range(level):
        (a, d) = pywt.dwt(a, w, mode)
        ca.append(a)
        cd.append(d)
    rec_a = []
    rec_d = []
    for i, coeff in enumerate(ca):
        coeff_list = [coeff, None] + [None] * i
        rec_a.append(pywt.waverec(coeff_list, w)[0:N])
    for i, coeff in enumerate(cd):
        coeff_list = [None, coeff] + [None] * i
        rec_d.append(pywt.waverec(coeff_list, w)[0:N])
    if coef_type == 'd':
        return rec_d
    return rec_a


if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    s = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    d = waveletdec(s, 'd', 'sym3', 3)
    a = waveletdec(s, 'a', 'sym3', 3)
    plt.subplot(3, 1, 1)
    plt.plot(s)
    plt.title('data')
    plt.subplot(3, 1, 2)
    r = d[0] + d[1] + d[2] + a[2]
    plt.plot(r)
    plt.title('rec data')
    plt.subplot(3, 1, 3)
    plt.plot(s - r)
    plt.title('error')
    plt.show()
