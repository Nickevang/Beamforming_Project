# main.py
from hexagonal_angles import generate_hexagons
from interference_angles import generate_interference_angles

# Constants
num_interference = 5  # Number of interference signals
num_elements = 24  # Number of elements in the antenna array
wavelength = 1  # Wavelength (normalized to 1)

# Generate hexagonal angles
hexagon_list = generate_hexagons()

# Generate interference angles for each hexagon
for hexagon in hexagon_list:
    theta_main = hexagon[0]  # Use the first angle of the hexagon as theta_main
    interference_angles = generate_interference_angles(theta_main, num_interference, num_elements, wavelength)
    print("Hexagon:", hexagon)
    print("Interference Angles:", interference_angles)
