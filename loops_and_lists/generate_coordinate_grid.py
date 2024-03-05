a = 1
b = 2
n = 20
h = (b - a) / n

coordinates_for_loop = []
for i in range(n+1):
    coordinates_for_loop.append(a + i*h)

coordinates_list_comp = [a + i*h for i in range(n+1)]
print(f"For x in [{a}, {b}] with {n} intervals, the interval length is h = {h:.3f}")
print("Using a for loop: x =", coordinates_for_loop)
print("Using list comprehension: x =", coordinates_list_comp)