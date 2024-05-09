import numpy as np
import matplotlib.pyplot as plt
# Define parameters
elevator_mass = 7150  # in kg
counterweight_mass = 5000  # in kg
gravity_acceleration = 9.81  # acceleration due to gravity in m/s^2
# Calculate cable tension using the formula T = m * g
cable_tension = elevator_mass * gravity_acceleration
# Define vectors for forces
elevator_force = np.array([0, elevator_mass * gravity_acceleration])
counterweight_force = np.array([0, -counterweight_mass * gravity_acceleration])
tension_force = np.array([0, -cable_tension])
# Create a figure and axis
fig, ax = plt.subplots()
# Plot elevator and forces
ax.arrow(0, 0, 0, elevator_mass * gravity_acceleration, head_width=0.5, head_length=0.5, fc='b', ec='b', label='Elevator')
ax.arrow(0, 0, 0, -counterweight_mass * gravity_acceleration, head_width=0.5, head_length=0.5, fc='r', ec='r', label='Counterweight')
ax.arrow(0, 0, 0, -cable_tension, head_width=0.5, head_length=0.5, fc='g', ec='g', label=f'Tension: {cable_tension} N')
# Set axis limits
ax.set_xlim(-20000, 20000)
ax.set_ylim(-10000, 20000)
# Add labels and title
ax.set_xlabel('Horizontal Direction')
ax.set_ylabel('Vertical Direction')
ax.set_title('Forces Acting on Elevator System')
# Add legend
ax.legend()
# Show plot
plt.grid(True)
plt.show()
