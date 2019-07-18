from math import cos, sin
class Ray():
    def __init__(self, vx, vy, vz):
        self.x = vx
        self.y = vy
        self.z = vz

    def init_coord(self, camera, i, j):
        self.x = (i-camera.resolution[0]/2)*camera.pitch[0]/2
        self.y = (j-camera.resolution[1]/2)*camera.pitch[1]/2
        self.z = camera.focale
        # rx, ry, rz = camera.rotation
        # self.rotation(rx, ry, rz)
        return self

    def rotation(self, rot_x=0, rot_y=0, rot_z=0):
        x, y, z = self.x, self.y, self.z
        y = y * cos(rot_x) - z * sin(rot_x)
        z = y * sin(rot_x) + z * cos(rot_x)
        x = x * cos(rot_y) - z * sin(rot_y)
        z = x * sin(rot_y) + z * cos(rot_y)
        x = x * cos(rot_z) - y * sin(rot_z)
        y = x * cos(rot_z) + y * sin(rot_z)
        self.x, self.y, self.z = x, y, z
        return self



    #         V->vyr = tmp*cosinus[*alpha] - V->vzr*sinus[*alpha];
    # V->vzr = tmp*sinus[*alpha] + V->vzr*cosinus[*alpha];

#
#         Si l'on considère que le pixel (0,0) est en haut à gauche de l'écran, alors ses coordonnées dans le repère caméra sont :
# vx = (i - res_x/2)*pitch_x        // Pour que le point au centre de l'écran aie x = 0
# vy = (i - res_y/2)*pitch_y        // Pour que le point au centre de l'écran aie y = 0
# vz = f
# qui sont en
#
