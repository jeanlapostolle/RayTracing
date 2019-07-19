from materiau import Materiau

class Plan():
    def __init__(self, arg, color):
        self.ambiante = color
        self.arg = arg
        self.color = color

    def intersection(self, ray, camera):
        a, b, c, d = self.arg
        vx, vy, vz = ray.x, ray.y, ray.z
        xr, yr, zr = camera.position
        A = (a*vx + b*vy + c*vz)
        B = (a*xr + b*yr + c*zr + d)
        return -B/A if A != 0 else 0

        # A(a*vx + b*vy + c*vz) + (a*xr + b*yr + c*zr + d) = 0
