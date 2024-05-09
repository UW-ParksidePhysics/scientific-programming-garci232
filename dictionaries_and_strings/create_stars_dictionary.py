def convert_list_of_tuples(nearby_star_data):
  stars = {}
  for star_data in nearby_star_data:
      star = {
          'distance': star_data[1],
          'apparent brightness': star_data[2],
          'luminosity': star_data[3]
      }
      stars[star_data[0]] = star
  return stars
def print_star_information(stars, star_name):
  if star_name in stars:
      star = stars[star_name]
      print(f"Star: {star_name}")
      print(f"    Distance (ly):            {star['distance']}")
      print(f"    Apparent brightness (m):  {star['apparent brightness']}")
      print(f"    Luminosity (L_sun):       {star['luminosity']}")
  else:
      print("Star not found in the data.")
# Nearby star data list of tuples
nearby_star_data = [
  ('Alpha Centauri A',    4.3,  0.26,      1.56),
  ('Alpha Centauri B',    4.3,  0.077,     0.45),
  ('Alpha Centauri C',    4.2,  0.00001,   0.00006),
  ("Barnard's Star",      6.0,  0.00004,   0.0005),
  ('Wolf 359',            7.7,  0.000001,  0.00002),
  ('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
  ('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
  ('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
  ('Sirius A',            8.6,  1.00,      23.6),
  ('Sirius B',            8.6,  0.001,     0.003),
  ('Ross 154',            9.4,  0.00002,   0.0005),
]
# Convert the nearby star data to a nested dictionary
stars = convert_list_of_tuples(nearby_star_data)
# Print star information for two different stars
print_star_information(stars, 'Sirius A')
print('\n')
print_star_information(stars, 'Alpha Centauri C')