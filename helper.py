from constant import ROUTES

def get_routes(city):
  output = []
  for route in ROUTES:
    if city not in route['cities']: continue
    first_city = route['cities'][0]
    dest_city = first_city if first_city != city else route['cities'][1]
    output.append((dest_city, route['color'], route['length']))
  return output

