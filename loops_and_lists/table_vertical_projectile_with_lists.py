def y_t(v0, g, t):
  return v0*t - 0.5*g*t**2
def generate_table(v0, g, n):
  upper_limit = 2*v0/g
  delta_t = upper_limit / n

  times = []
  positions = []
  for i in range(n+1):
      t = i * delta_t
      y = y_t(v0, g, t)
      times.append(t)
      positions.append(y)

  print('t (s)\ty (m)')
  print('-------------')

  for t, y in zip(times, positions):
      print(f'{t:.3f}\t{y:.3f}')

  print('-------------')

v0 = 10.00
g_cc = 12.94
generate_table(v0, g_cc, 10)


