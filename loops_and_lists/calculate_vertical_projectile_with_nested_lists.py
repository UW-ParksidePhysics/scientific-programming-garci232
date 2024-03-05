t = [0.0, 0.1, 0.2, 0.3, 0.4]
y = [0.0, 0.1, 0.4, 0.9, 1.6]

times_positions = [t, y]

print(f"{'t (s)':<10}{'y (m)':<10}")
for i in range(len(times_positions[0])):
    print(f"{times_positions[0][i]:.2f}{'':<6}{times_positions[1][i]:.2f}")