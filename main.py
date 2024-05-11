# main.py
from matplotlib import pyplot as plt
from hexagonal_angles import generate_hexagons
from interference_angles import generate_interference_angles
from radiationpat import radiationpat
import numpy as np

# Constants
num_interference = 18  # Maximum number of interference signals
num_elements = 24  # Number of elements in the antenna array
wavelength = 1  # Wavelength (normalized to 1)

# Generate hexagonal angles
start_angle = 30
end_angle = 150
delta = 1
hexagons = generate_hexagons(start_angle, end_angle, delta)

# Generate interference angles for each hexagon
for hexagon in hexagons:
    theta_main = hexagon[0]  # Use the first angle of the hexagon as theta_main
    interference_angles = generate_interference_angles(theta_main, num_interference, num_elements, wavelength)
    print("Hexagon:", hexagon)
    print("Interference Angles:", interference_angles)

    # Calculate radiation pattern for each hexagon and interference angle
    for theta in [theta_main] + interference_angles:
        SNR = 10  # Example SNR value
        AF, angleofzeros, angleofmax, SLL = radiationpat(SNR, np.array([theta]))
        print(f"Theta: {theta}, Angle of Zeros: {angleofzeros}, Angle of Max: {angleofmax}, SLL: {SLL}")

    
    # Plot radiation pattern
    plt.figure()
    plt.plot(AF)
    plt.title("Radiation Pattern")
    plt.xlabel("Angle")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    print("Hexagon:", hexagon)
    print("Interference Angles:", interference_angles)
    print("Radiation Pattern (AF):", AF)
    print("Angle of Maximum:", angleofmax)
    print("Angles of Zeros:", angleofzeros)
    print("Side Lobe Level (SLL):", SLL)
    print("\n")
