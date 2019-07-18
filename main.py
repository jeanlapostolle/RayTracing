import matplotlib.pyplot as plt
from camera import Camera
from ray import Ray
from sphere import Sphere
from math import pi

w = 100
h = 100
cam = Camera( position=[0,0, 0], rotation=[0,0,0], focale=40, resolution=[w, h], pitch=[1, 1])
sph = Sphere(position=[0, 0, 50], radius=5, color=[125, 0, 200])
sph2 = Sphere(position=[0, 0, 10], radius=5, color=[200, 123, 50])

scene = [sph, sph2]

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
                print(alpha, alphamax)
                if alpha < alphamax:
                    print("Ok")
                    alphamax = alpha
                    color = element.ambiante
                    # color[0] *= alpha
                    image[i][j] = color

# print(scene)
plt.imshow(image)
plt.show()
