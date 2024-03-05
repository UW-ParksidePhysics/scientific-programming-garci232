def y_t(v0, g, t):
  return v0*t - 0.5*g*t**2
def print_table(v0, g, n):
  upper_limit = 2*v0/g
  delta_t = upper_limit / n

  print('-----------------------------------------------------')
  print('Gliese 667 Cb (g = 14.12 m/s^2)   Cc (g = 12.94 m/s^2)')
  print('-----------------------------------------------------')
  print('t (s)\ty (m)\tt (s)\ty (m)')
  print('-----\t-----\t-----\t-----')


  for i in range(n+1):
      t = i * delta_t
      y = y_t(v0, g, t)
      t2 = t
      y2 = y
      print(f'{t:.3f}\t{y:.3f}\t{t2:.3f}\t{y2:.3f}')

  print('-----\t-----\t-----\t-----')

  t = 0
  while t <= upper_limit:
      y = y_t(v0, g, t)
      t2 = 0
      y2 = 0
      print(f'{t:.3f}\t{y:.3f}', end='\t')
      if t != 0:
          t2 = t + delta_t
          y2 = y_t(v0, g, t2)
          print(f'{t2:.3f}\t{y2:.3f}')
      else:
          print()
      t += delta_t
  print('-----------------------------------------------------')


v0 = 10.00
g_cb = 14.12

print_table(v0, g_cb, 10)
#In this code snippet, the y_t function calculates the y(t) value based on the projectile motion formula, and the print_table function prints the nicely formatted table using for and while loops. The code includes input values for Gliese 667 Cb (initial velocity = 10.00 m/s and acceleration = 14.12 m/s^2), and the table includes values for t and y(t). The bonus section prints the while loop values on the same line.


