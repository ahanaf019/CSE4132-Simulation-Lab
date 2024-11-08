import matplotlib.pyplot as plt
import random
import math
import time

distance = 150
MAX_DST = 900
MIN_DIST = 100

xf = 100
yf = 100
vf = 50

XF = [xf]
YF = [yf]

XB = []
YB = []


plt.ion()
figure, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim([0, 1000])
ax.set_ylim([0, 1000])
ax.axis('on')
line1, = ax.plot(XF, YF, 'x--', color='red')
line2, = ax.plot(XB, YB, 'x--', color='blue')


while distance > MIN_DIST and distance < MAX_DST:
    xb = random.randint(0, 1000)
    yb = random.randint(0, 1000)
    
    distance = math.sqrt((xf - xb)**2 + (yf - yb)**2)
    
    xf = xf + vf * (xb - xf) / distance
    yf = yf + vf * (yb - yf) / distance
    
    print(f'Bomber=({xb:4.2f},{yb:4.2f}), Fighter=({xf:4.2f},{yf:4.2f}), distance={distance:4.2f}')
    
    XB += [xb]
    YB += [yb]
    XF += [xf]
    YF += [yf]
    line1.set_xdata(XF)
    line1.set_ydata(YF)
    
    line2.set_xdata(XB)
    line2.set_ydata(YB)
    ax.set_title(f'Distance: {distance:0.2f}')

    
    if distance < MIN_DIST:
        print('Bomber caught')
        ax.set_title(f'Distance: {distance:0.2f}, Bomber caught')
        # break

    if distance > MAX_DST:
        print('Bomber escaped')
        ax.set_title(f'Distance: {distance:0.2f}, Bomber escaped')
        # break
    
    figure.canvas.draw()
    figure.canvas.flush_events()
    time.sleep(1)
    
time.sleep(5)

