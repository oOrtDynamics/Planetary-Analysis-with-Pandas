# Planetary Analysis with Pandas


planet_distances = {
    "Mercury": 57.9,
    "Venus": 108.2,
    "Earth": 149.6,
    "Mars": 227.9,
    "Jupiter": 778.6,
    "Saturn": 1433.5,
    "Uranus": 2872.5,
    "Neptune": 5906.4
}

moon_data = {
    "Planet": ["Jupiter", "Jupiter", "Saturn", "Saturn", "Uranus", "Neptune"],
    "Moon": ["Io", "Ganymede", "Titan", "Rhea", "Titania", "Triton"],
    "Diameter (km)": [3642, 5262, 5150, 1528, 1578, 2707],
    "Orbital Period (days)": [1.77, 7.15, 15.95, 4.52, 8.71, 5.88]
}

import pandas as pd

planet_distances = pd.Series(planet_distances)

moon_characteristics = pd.DataFrame(moon_data)

print("Average distance of planets from Sun: ")

print(planet_distances.mean())

print("\nNumber of moons for each outer planet: ")

outer_planets = ["Jupiter", "Saturn", "Neptune"]

for planet in outer_planets:
    num_moons = moon_characteristics[moon_characteristics["Planet"] == planet].shape[0]

print(f"{planet}: {num_moons} ")
print("\n")

for planet in outer_planets:
    largest_moon = moon_characteristics[moon_characteristics["Planet"] == planet].sort_values(by="Diameter (km)", ascending=False).iloc[0] # .iloc gets specific column data
    print(f"{planet}: {largest_moon["Moon"]} ({largest_moon["Diameter (km)"]} km)")