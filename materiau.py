class Materiau():
    def __init__(self, ambiante):
        self.ambiante = ambiante
        self.diffuse = diffuse
        self.reflexion = reflexion
        self.speculaire = speculaire
        self.weights = weights
        self.opacite = opacite

 # diffuse, reflexion, speculaire, weights, opacite




#
#   Chaque objet est associé à un matériau (plastique, métal, ...) déterminé par :
# - une couleur ambiante : celle que l'on voit toujours (même kan l'objet n'est pas éclairé)
# - une couleur diffuse : celle que l'on voit seulement kan l'objet est éclairé
# - une couleur de réflexion : les reflets seront teintés par cette couleur
# - une couleur spéculaire : les reflets des lumières seront teintés par cette couleur
# - une série de coefficients pour attribuer plus ou moins d'importance à chacune de ces couleurs
# - un coefficient d'opacité : pour les objets transparents
