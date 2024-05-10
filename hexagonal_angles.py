# hexagonal_angles.py

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
