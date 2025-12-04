#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                   RENDU 4 DECEMBRE 2025
#                                                                       Steve NONO
#                                                                       HETIC - MD4
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                   CONVERSION d'une image en image pair  By Steve
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Image_to_pair(input_path, output_path):
    # Ouvrir l'image
    image = Image.open(input_path).convert("RGB")
    pixels = image.load()

    width, height = image.size

    #Parcour raster scan (il est fort HAKIM)
    for y in range(height):  # Parcours des lignes (de haut en bas)
        for x in range(width): # Parcours des colonnes (de gauche à droite)
            r, g, b = pixels[x, y]

            # mettre le LSB à 0
            r_even = r - (r%2)
            g_even = g - (g%2)
            b_even = b - (b%2)

            pixels[x, y] = (r_even, g_even, b_even)

    # Sauvegarde en PNG pour garder les bits intacts merci Hakim :)
    image.save(output_path, format="PNG")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                AFFICHAGE EN MATRICE DE L'IMAGE
#---------------------------------------------

def affiche_image_matrix(path):

    image = Image.open(path).convert("RGB")
    matrix = np.array(image)   # shape : (hauteur, largeur, 3)

    print("Taille de l'image (hauteur, largeur, canaux) :", matrix.shape)
    print("Matrice de l'image :")
    print(matrix)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                   CONVERSION DU MESSAGE EN BINAIRE By Steve
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def message_to_bits(message: str) -> str:
    bits = ""
    for char in message:
        code_ascii = ord(char) #  Récupère le code ASCII
        # conversion en binaire
        convert = bin(code_ascii)[2:].zfill(21)
        # Ajout la chaîne globale de bits
        bits += convert

    return bits

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                  AMUSONS NOUS A AFFICHER DANS UNE FENETRE NOTRE IMAGE SINON CE N'est plus fun :)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def affiche_image(path):
    image = Image.open(path)
    plt.imshow(image)
    plt.axis("off")   # cache les axes
    plt.show()

# test
if __name__ == "__main__":
    """ j'appelle la fonction pour convertir l'image"""
    Image_to_pair("signature mail KONOS.jpeg", "image-paire.png")
    print("l'image transformé est disponible :)")

    """ j'appelle la fonction pour afficher la matrice de l'image converti"""
    affiche_image_matrix("image_paire.png")

    """ j'appelle la fonction pour afficher  l'image converti"""
    affiche_image("image_paire.png")

    """ j'appelle la fonction pour convertir le message"""
    msg = "Salut"
    bits = message_to_bits(msg)
    print("Le message devient : ", bits)


""" ce n'est pas l'espace pour faire mon readme mais c'était chaud pour le faire avec le temps 

ceci pour indiquer que j'ajoute l'image signature mail KONOS.jpeg que j'utilise pour faire des tests

On fera un readme prochainement """