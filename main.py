import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from camera import Camera
from ray import Ray
from sphere import Sphere
from plan import Plan
from math import pi
from tool import maps
import numpy as np

fig, ax = plt.subplots()

w = 640
h = 480
cam = Camera( position=[10, 0, 0], rotation=[0, 0, 0], focale=20, resolution=[w, h], pitch=[1, 1])
sph = Sphere(position=[0, 0, 12], radius=5, color=[125, 0, 200])
sph2 = Sphere(position=[0, 5, 10], radius=3, color=[200, 123, 50])
pla = Plan(arg=[1,0,0,50], color=[0, 0, 225] )

scene = [pla,sph, sph2]
l = 0
frame = 0
def update(frame, l):
    cam.position[2] = frame
    cam.rotation = [0,0, 0]
    image = [[(0,0,0) for i in range(w)] for j in range(h)]
    rays = []
    for i in range(h):
        for j in range(w):
            alphamax = float("inf")
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
                        # color[0] = int(maps(alpha, 0, 1, 0, 255))%255
                        # print(color[0])
                        image[i][j] = color

    plt.imsave("res/{}.png".format(l),np.array(image, dtype="uint8").reshape(w, h, 3))
#
for frame in np.linspace(0,15, 25):
    l+=1
    update(frame, l)

# plt.imshow(image)
# plt.show()


# print(scene)
# plt.show()
