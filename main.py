import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from camera import Camera
from ray import Ray
from sphere import Sphere
from math import pi
from tool import maps
import numpy as np

fig, ax = plt.subplots()

w = 100
h = 100
cam = Camera( position=[0, 0, 0], rotation=[0, 0, 0], focale=20, resolution=[w, h], pitch=[1, 1])
sph = Sphere(position=[0, 0, 12], radius=5, color=[125, 0, 200])
sph2 = Sphere(position=[0, 5, 10], radius=3, color=[200, 123, 50])

scene = [sph, sph2]
l = 0
def update(frame, l):
    cam.rotation = [0, frame, 0]
    image = [[(0,0,0) for i in range(w)] for j in range(h)]
    rays = []
    for i in range(h):
        for j in range(w):
            alphamax = 1000
            rays.append(Ray(0, 0, 0))
            rays[-1].init_coord(cam, i ,j)
            for element in scene:
                alpha = element.intersection(rays[-1], cam)
                if alpha:
                    # print(alpha, alphamax)
                    if alpha < alphamax:
                        alphamax = alpha
                        # print(alphamax)
                        color = element.ambiante.copy()
                        color[0] = int(maps(alpha, 0, 1, 0, 255))%255
                        # print(color[0])
                        image[i][j] = color

    plt.imsave("res/{}.png".format(l),np.array(image).reshape(3,w*h))

for frame in np.linspace(0, 2*pi, 10):
    l+=1
    update(frame, l)

plt.show()


# print(scene)
# plt.show()
