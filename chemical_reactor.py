import matplotlib.pyplot as plt
import time


K1 = 0.05
K2 = 0.05

A = [1]
B = [0.5]
C = [0]

total_time = 100
steps = 50
dt = total_time / steps

t = 0
T = [t]


plt.ion()
figure, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim([0, total_time])
ax.set_ylim([0, max([A[0], B[0], C[0]])])
ax.set_xlabel('Time')
ax.set_ylabel('Quantity')

line1, = ax.plot(T, A, color='green')
line2, = ax.plot(T, B, color='blue')
line3, = ax.plot(T, C, color='red')

while t < total_time:
    a = A[-1] + (K2 * C[-1] - K1 * A[-1] * B[-1]) * dt
    b = B[-1] + (K2 * C[-1] - K1 * A[-1] * B[-1]) * dt
    c = C[-1] + (2 * K1 * A[-1] * B[-1] - 2 * K2 * C[-1]) * dt
    
    A += [a]
    B += [b]
    C += [c]
    
    t += dt
    T += [t]
    
    print(f'Time: {t:0.2f}, A:{a: 0.2f}, B:{b: 0.2f}, C:{c: 0.2f}')
    
    line1.set_xdata(T)
    line1.set_ydata(A)
    
    line2.set_xdata(T)
    line2.set_ydata(B)
    
    line3.set_xdata(T)
    line3.set_ydata(C)
    
    ax.set_title(f'Time: {t:0.2f}, A:{a: 0.2f}, B:{b: 0.2f}, C:{c: 0.2f}')
    ax.legend(['A', 'B', 'C'])
    
    figure.canvas.draw()
    figure.canvas.flush_events()
    time.sleep(0.2)
