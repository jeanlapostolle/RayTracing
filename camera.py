class Camera():
    def __init__(self, position, rotation, focale, resolution, pitch):
        self.position = position
        self.rotation = rotation
        self.focale = focale
        self.resolution = resolution
        self.pitch = pitch

# Elle est déterminée par plusieurs paramètres :
# - sa position dans l'espace (xr, yr, zr) et son orientation (rot_x, rot_y, rot_z)
# - sa focale f = distance entre le centre de la caméra et son plan de projection (écran)
# - sa résolution (res_x, res_y) et le pitch (pitch_x, pitch_y) des pixels = dimensions d'un pixel en unités du repère espace
