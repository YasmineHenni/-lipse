
from copy import deepcopy
import matplotlib.pyplot as plt

from superEllipse import creerEtOuEffacerUnFichier, afficherUnFichier
from superEllipse import SuperEllipse

# trois ellipses vides et de quoi les remplir
# ------------------------------------------
ellipse_1 = SuperEllipse()
ellipse_1_specificationOriginales = {'xy':(1,2)}
ellipse_1_fichier_sauvegarde = "ellipse_1_bis.txt"

ellipse_2 = SuperEllipse()
ellipse_2_specificationOriginales = "unFichierContenantUneSuperEllipse.txt"
ellipse_2_specifications_ajout_1 = {"color":'r',"linestyle":':'}
ellipse_2_specifications_ajout_2 = {"alpha":.6,"linewidth":4}
ellipse_2_fichier_sauvegarde = "ellipse_2_bis.txt"

ellipse_3 = SuperEllipse()
ellipse_3_specificationOriginales = {"xy":(-1,-2),"color":'b',"alpha":.7}
ellipse_3_fichier_sauvegarde  = "unFichierVideARemplir.txt"


# on charge une SuperEllipse a partir d'un dictionnaire
# -----------------------------------------------------
print("\n\nChargement d'une ellipse a partir d'un dictionnaire : ")
print("  ellipse_1            (cree vide) : ",ellipse_1)
ellipse_1.aPartirDunDictionnaire(ellipse_1_specificationOriginales)
print("  ellipse_1 (remplie dictionnaire) : ",ellipse_1)


# Que se passe-t-il quand on utilise "=" ? 
print("""\nQue se passe-t-il quand on utilise "=" ? : """)
ellipse_1bis = ellipse_1
print("  id(ellipse_1):",id(ellipse_1))
print("  id(ellipse_1bis) :",id(ellipse_1bis))
del ellipse_1bis


# on charge une SuperEllipse a partir d'un fichier
# ---------------------------------------------------
print("\n\nChargement d'une SuperEllipse a partir d'un fichier : ")
print("  ellipse_2  (cree vide) : ",ellipse_2)
ellipse_2.aPartirDUnNomDeFichier(ellipse_2_specificationOriginales)
print("  ellipse_2  (remplie fichier) : ",ellipse_2)


# Ajout un element a la fois
# --------------------------
print("\n\nAjouts une specification à la fois : ")
print("  ellipse_1  (avant ajout) : ",ellipse_1)
ellipse_1.ajouterUneSpecification("angle")
ellipse_1.ajouterUneSpecification("color",'m')
print("  ellipse_1  (ajout angle et couleur) : ",ellipse_1)


# Ecriture d'ellipse_1 dans un fichier
# ------------------------------------
print("\n\nEcriture de Ajout, ellipse_1 dans le fichier" +
      """ "{}".""".format(ellipse_1_fichier_sauvegarde))
ellipse_1.ecrireDansUnFichier(ellipse_1_fichier_sauvegarde)


# Ajout de plusieurs spécifications 
# ----------------------------------
print("\n\nAjout de plusieurs specifications simultanee: ")
print("  ellipse_2  (avant ajout) : ",ellipse_2)
ellipse_2.ajouterDesSpecifications(ellipse_2_specifications_ajout_1)
ellipse_2.ajouterDesSpecifications(ellipse_2_specifications_ajout_2)
print("  ellipse_2  (ajout color+linestyle alpha+linewidth) : ",ellipse_2)


# Ecriture d'ellipse_1 dans un fichier
# ------------------------------------
print("\n\nEcriture de Ajout, ellipse_2 dans le fichier" +
      """ "{}".""".format(ellipse_2_fichier_sauvegarde))
ellipse_2.ecrireDansUnFichier(ellipse_2_fichier_sauvegarde)


# Modification d'un fichier contenant une ellipse
# -----------------------------------------------
print("""\n\nEcrasemant du fichier "{}".""".format(ellipse_2_fichier_sauvegarde))
creerEtOuEffacerUnFichier(ellipse_3_fichier_sauvegarde)
print("  fichier avant         (vide) : ")#, end='')
afficherUnFichier(ellipse_3_fichier_sauvegarde)

# ajout au fichier
ellipse_2.ajouterAUnFichier(ellipse_3_fichier_sauvegarde)
print("  fichier apres      (ajout 1) : ")#, end='')
afficherUnFichier(ellipse_3_fichier_sauvegarde)

# creation de la liste de la SuperEllipse
ellipse_3.aPartirDunDictionnaire(ellipse_3_specificationOriginales)
ellipse_3.ajouterAUnFichier(ellipse_3_fichier_sauvegarde)
print("  fichier apres      (ajout 2) : ")#, end='')
afficherUnFichier(ellipse_3_fichier_sauvegarde)


print("ellipse_1: ",ellipse_1)
print("ellipse_2: ",ellipse_2)
print("ellipse_3: ",ellipse_3)

plt.figure()
try:
    ellipse_1.afficher()
    ellipse_2.afficher()
    ellipse_3.afficher()
except TypeError:
    print("Il va falloir completer.")
plt.xlim([-5,5])
plt.ylim([-5,5])

plt.show()

