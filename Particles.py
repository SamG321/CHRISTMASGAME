import pygame
import random

class Particles:
    def __init__(self, position):
        self.particles = []

        # randomly decide how many particles
        for i in range(int(random.randint(5, 10))):
            # location, velocity, time alive
            self.particles.append([[position[0]+25, position[1]+50], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

    def update(self, screen, chimneyspeed):
        for particle in self.particles:
            # move particle
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            
            # time alive 
            particle[2] -= 0.1

            # speed
            particle[1][1] += 0.1

            # move with the chimneys
            particle[0][0] -= chimneyspeed

            # draw
            pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

            # remove particles after dead
            if particle[2] <= 0:
                self.particles.remove(particle)