import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Зададим количество отсчётов
N = 1000
t_min = 0
t_max = np.pi
dt = (t_max - t_min) / (N-1)

f0 = 40

# Определим массивы данных
t = np.arange(N) * dt + t_min

# Зададим функцию
a0 = 0.5    # постоянная составляющая
a1 = 4      # амплитуда
a2 = 2
s1 = a0 + a1 * np.cos(2 * np.pi * f0 * t)
s2 = a2 * np.sin(2 * np.pi * f0 * t / 2)
s = s1 + s2

def DPF(arr, dt = 1):
    len_arr = len(arr)
    F = np.zeros(len_arr, dtype=complex)
    k = -1j * 2 * np.pi / len_arr
    for m in range(len_arr):
        for n in range(len_arr):
            F[m] += arr[n] * np.exp(k * m * n)
    F = F / len_arr
    df = 1 / len_arr / dt
    f = np.arange(len_arr) * df
    return F, f

def InvDPF(arr, dt = 1):
    len_arr = len(arr)
    s = np.zeros(len_arr, dtype=float)
    k = 1j * 2 * np.pi / len_arr
    for n in range(len_arr):
        for m in range(len_arr):
            s[n] += np.real(arr[m] * np.exp(k * m * n))
    t = np.arange(len_arr) * dt
    return s, t


F, f = DPF(s, dt)
abs_F = abs(F)
Re_F = np.real(F)
Im_F = np.imag(F)

new_s, new_t = InvDPF(F, dt)


fig, ax = plt.subplots(2, 2, figsize = (16,8))
ax[0][1].scatter(f, abs_F)
ax[0][1].vlines(f, ymin = 0, ymax = abs_F)
ax[0][1].set(xlim = [0, 1/dt], ylim = [0, 2])
ax[0][0].plot(t, s)
ax[1][0].plot(new_t, new_s, 'r')
for ax in fig.axes:
    ax.grid()
    #  Устанавливаем интервал основных делений:
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    # ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
    # ax.yaxis.set_major_locator(ticker.MultipleLocator(100))
    # ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
plt.show()