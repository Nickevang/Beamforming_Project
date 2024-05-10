# interference_angles.py
import numpy as np

def calculate_sll(theta_main, theta_interference, num_elements, wavelength):
    # Constants
    k = 2 * np.pi / wavelength
    
    # Array factor for main lobe
    array_factor_main = np.sum(np.exp(1j * k * np.arange(num_elements) * np.cos(np.deg2rad(theta_main)))) / num_elements
    
    # Array factor for interference
    array_factor_interference = np.sum(np.exp(1j * k * np.arange(num_elements) * np.cos(np.deg2rad(theta_interference)))) / num_elements
    
    # Calculate SLL in dB
    sll = 20 * np.log10(np.abs(array_factor_interference / array_factor_main))
    
    return sll

def generate_interference_angles(theta_main, num_interference, num_elements, wavelength, sigma=10):
    interference_angles = []
    
    for _ in range(num_interference):
        theta = np.random.normal(theta_main, sigma)
        sll = calculate_sll(theta_main, theta, num_elements, wavelength)
        if sll <= -20:  # Check if SLL is less than or equal to -20 dB
            interference_angles.append(theta)
    
    return interference_angles
