# ==========================================================
# Simulation of a Chemical Reactor
# ==========================================================
# 
# Md. Ahanaf Arif Khan
# Roll: 1910676110
# Session: 2018-19
# Course: CSE4132: Computer Simulation and Modeling Lab
# ==========================================================

# Importing Dependencies
import matplotlib.pyplot as plt
import time


# Initial Quantities
chemical_A = 1
chemical_B = 0.5
chemical_C = 0

# Rate Constants
k1 = 0.05
k2 = 0.05

# Maximum time (minutes)
t_max = 100
# Total Number of timesteps
t_steps = 500

# Figure Initialization
plt.ion()
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111)
chemical_A_line, = ax.plot([chemical_A])
chemical_B_line, = ax.plot([chemical_B])
chemical_C_line, = ax.plot([chemical_C])
plt.xlabel("Time (minutes)")
plt.xlim([0, t_max])
plt.ylim([0, max(chemical_A, chemical_B)])
plt.ylabel("Quantity (moles / quantity)")
plt.legend(['Chemical A','Chemical B', 'Chemical C'])
plt.title("Simulation of a Chemical Reactor")

# Calculate the length of each timestep
delt = t_max / t_steps

# List to hold each timestep and the values of
# each chemical at the given timestep
list_t = [0]
list_a = [chemical_A]
list_b = [chemical_B]
list_c = [chemical_C]


t = 0 
print("==========================================================")
print('Time\t\tA\t\tB\t\tC')
print("==========================================================")
while t <= t_max:
    # Printing out the quantity of each chemical for current time
    print(f'{t:2.2f}\t\t{chemical_A:2.2f}\t\t{chemical_B:2.2f}\t\t{chemical_C:2.2f}')
    
    # Calculating the changes in quantity of chemicals
    da = k2 * chemical_C - k1 * chemical_A * chemical_B
    db = k2 * chemical_C - k1 * chemical_A * chemical_B
    dc = 2 * k1 * chemical_A * chemical_B - 2 * k2 * chemical_C
    
    chemical_A += da * delt
    chemical_B += db * delt
    chemical_C += dc * delt
    
    chemical_A_line.set_xdata(list_t)
    chemical_A_line.set_ydata(list_a)
    
    chemical_B_line.set_xdata(list_t)
    chemical_B_line.set_ydata(list_b)
    
    chemical_C_line.set_xdata(list_t)
    chemical_C_line.set_ydata(list_c)
    
    # Update the lists with new values
    list_a.append(chemical_A)
    list_b.append(chemical_B)
    list_c.append(chemical_C)
    t += delt
    list_t.append(t)
    
    # Update figure with new datapoints
    fig.canvas.draw()
    fig.canvas.flush_events()
    # time.sleep(0.0001)
    
print("==========================================================")
    
input()
