import itertools

def generate_hexagons(start_angle, end_angle, delta):
    hexagons = []
    current_angle = start_angle
    while current_angle <= end_angle:
        hexagon = []
        for i in range(6):
            angles = [(current_angle + j * delta) % 360 for j in range(6)]
            hexagon.append(tuple(angles))
            current_angle += delta
            if max(angles) > end_angle:
                return hexagons
        hexagons.append(hexagon)
    return hexagons

start_angle = 30
end_angle = 150
delta = 1

hexagons = generate_hexagons(start_angle, end_angle, delta)

for hexagon in hexagons:
    for theta0 in hexagon:
        theta0_str = ", ".join(f"{angle}°" for angle in theta0)
        theta_rest = [angle for angle in hexagon if angle != theta0]
        theta_rest_str = ["(" + ", ".join(f"{angle}°" for angle in theta) + ")" for theta in theta_rest]
        print(f"θ0: {theta0_str}, θ1-θ5: {', '.join(theta_rest_str)}")
