from materiau import Materiau
from math import sqrt
class Sphere():
    def __init__(self, position, radius, color):
        self.ambiante = color
        self.position = position
        self.radius = radius

    def intersection(self, ray, camera):
        vx, vy, vz = ray.x, ray.y, ray.z
        R = self.radius
        x0, y0, z0 = self.position
        xr, yr, zr = camera.position
        a = (vx**2 + vy**2 + vz**2)
        b = 2 * (vx*(xr-x0) + vy*(yr-y0) + vz*(zr-z0))
        c = ((xr-x0)**2 + (yr-y0)**2 + (zr-z0)**2 - R**2)

        delta = b**2 - 4*a*c


        if delta > 0:
            alpha = None
            alpha1 = -(b - sqrt(delta)) / (2 * a)
            if alpha1 > 0:
                alpha = alpha1
            alpha2 = -(b + sqrt(delta)) / (2 * a)
            if alpha2 > 0:
                alpha = alpha2
        elif delta == 0:
            alpha = -b / (2 * a)
            if alpha < 0:
                alpha = None
        else:
            alpha =  None

        return alpha
