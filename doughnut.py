import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spinning Donut")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Donut constants
A, B = 0, 0
radius1 = 1
radius2 = 2
K1 = 100
K2 = 300

# Main loop
clock = pygame.time.Clock()
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Pre-compute sin/cos for A and B
    cosA = math.cos(A)
    sinA = math.sin(A)
    cosB = math.cos(B)
    sinB = math.sin(B)

    # Loop through theta and phi to calculate the 3D points
    for theta in range(0, 628, 7):  # 0 to 2pi in steps
        costheta = math.cos(theta / 100)
        sintheta = math.sin(theta / 100)

        for phi in range(0, 628, 2):  # 0 to 2pi in steps
            cosphi = math.cos(phi / 100)
            sinphi = math.sin(phi / 100)

            # Calculate 3D coordinates of the point on the torus
            circleX = radius2 + radius1 * costheta
            circleY = radius1 * sintheta

            # Project 3D to 2D coordinates
            x = int(width / 2 + K1 * (cosB * circleX * cosphi - sinA * sinB * circleY + cosA * sinB * circleX * sinphi))
            y = int(height / 2 - K2 * (cosA * circleY + sinA * circleX * sinphi) / (4 + cosA * circleY + sinA * circleX * sinphi))

            # Draw the pixel
            if 0 <= x < width and 0 <= y < height:
                luminance_index = int(8 * ((cosA * cosphi * sintheta - cosA * sinB * sinphi - sinA * sintheta + sinA * cosB * circleX)))
                color = WHITE if luminance_index > 0 else BLACK
                screen.set_at((x, y), color)

    # Update angles
    A += 0.04
    B += 0.02

    # Refresh display
    pygame.display.flip()
    clock.tick(30)  # Frame rate