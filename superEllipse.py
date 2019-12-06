
import warnings as wrn
from copy import deepcopy
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from   matplotlib.patches import Ellipse


def creerEtOuEffacerUnFichier(unNomDeFichier):
    fio = open(unNomDeFichier,'w')
    fio.close()

def afficherUnFichier(unNomDeFichier):
    print("\n-------------------------------")
    print("| ",unNomDeFichier," |")
    print("------------------------------------")
    with open(unNomDeFichier, 'r') as file: 
        print(file.read(), end='')
    print("------------------------------------\n")



class SuperEllipse:
    parameters = ['xy', 'width', 'height', 'angle']
    properties = ['agg_filter', 'value', 'alpha', 'animated',
                  'antialiased', 'capstyle', 'clip_box', 'clip_on',
                  'clip_path', 'color', 'contains', 'edgecolor',
                  'facecolor', 'figure', 'fill', 'gid',  'hatch',
                  'in_layout', 'joinstyle', 'label', 'linestyle',
                  'linewidth', 'path_effects', 'picker',
                  'rasterized', 'sketch_params', 'snap',
                  'transform', 'url', 'visible', 'zorder']
    
    def __init__(self):
        self.specifications = dict()
        
    def __str__(self):
        "pour avoir une Ellipse joliment affichee"
        return self.specifications.__str__()

    def clear(self):
        self.specifications.clear()
    
    def aPartirDUnNomDeFichier(self, filename):
        '''
        Pour initialiser la SuperEllipse a partir d'un fichier
        '''
        # on ouvre le fichier et on charge les lignes
        # chaque ligne correspond a un spécification
        # i.e. un couple (clef,valeur) du dictionnaire
        #
        # Remarque :
        # * Dans le fichier, on lit les caractères qu'il contient.
        # * On convertit un peu comme on le peut les chaînes de caractères lues en entier et en flottant
        #
        with open(filename) as f:
            for ligne in f:
                items = ligne.split(' ; ')
                assert len(items) == 2
                key, valuesList = items[0], items[1]
                values = valuesList.split(',')
                values[-1] = values[-1][0:-1]
                if len(values) == 1:
                    try :
                       values[0]  = int(values[0])
                    except ValueError:
                        try :
                            values[0] = float(values[0])
                        except ValueError:
                            pass
                    self.specifications[key] = values[0]
                else:
                    for i in range(len(values)):
                        try :
                            values[i] = int(values[i])
                        except ValueError:
                            try :
                                values[i] = float(values[i])
                            except ValueError:
                                pass
                    self.specifications[key] = values
            return self
        
    def aPartirDunDictionnaire(self, datadict):
        "Pour initialiser une superEllipse a partir d'un dictionnaire"
        # on copie datadict dans l'attribut specifications
        # attention a la nature de la copie
        
        self.specifications= deepcopy (datadict)
        
    def ecrireDansUnFichier(self,filename):
        "Pour ecrire la liste dans un fichier"
        # on ouvre un fichier 
        # on ecrit chaque specification sur une ligne ligne
        # on ferme le fichier
        #
        # Remarques :
        #  * On fera quelque chose qui est coherent avec ce qui est ecrit pour la lecture
        #  * L'ecriture est beaucoup plus simple que la lecture
        #



        pass
    
    def ajouterAUnFichier(self,nomDeFichier):
        """
           Pour completer le fichier avec des specifications supplementaires.
        """
        # on charge le fichier dans un dictionnaire
        # on ajoute les spécifications i.e. les couples (clef,valeur)
        # on ecrase le fichier precedent




        pass
    
    def ajouterUneSpecification(self,specificationAAjouter,qualite=None):
        '''
           Pour ajouter une spécification a la superEllipside
        '''
        # tester si la spécification existe
        # si elle existe et qu'elle est différente complete on emet un message d'alerte
        # avec quelque chose du type wrn.warn("Pour le champs {}, on remplace {} par {}"....
        # En ajoute la spécifiation (en ecrasant celle qui existait si elle existait)
        #
        if qualite== None:
            self.ajouterUneValeurParDefaut(specificationAAjouter)
        else:
            for v in self.specifications.keys():
                if v == specificationAAjouter and self.specifications[v] != self.specifications[specificationAAjouter]:

                    wrn.warn("Pour le champs {}, on remplace {} par {}".format(specificationAAjouter,self.specifications[specificationAAjouter], qualite ))
            self.specifications[specificationAAjouter]= qualite
                    



        
    
    def ajouterDesSpecifications(self,dictEnPlus):
        '''
           Pour ajouter plusieurs specifications a une SuperEllipse
        '''
        # Pour chacun des elements de dictEnPlus
        # et ajout de chaque couple (clef,valeur) comme une specification
        for k in dictEnPlus:
            #self.specifications[k]= dictEnPlus[k]
            self.ajouterUneSpecification(k,dictEnPlus[k])


        
        
    def estElleCoherente(self):
        # On verifie que les tous les parametres sont presents dans specification
        # On verifie qu'une specification est soit un parametre soit une propriete
        specifi= self.specifications.keys()
        paraManquant=[]
        speciEnPlus=[]
        rep= True
        for p in self.parameters:
            if p in specifi:
                print('il y a tous les parametres')
            else:
                print('il manque un parametre {}'.format(p))
                paraManquant.append(p)
                rep=False
        for s in specifi:
            if s in self.parameters== False:
                if s in self.properties == False:
                    print('la specification {} est ni un parametre ni une property'.format(s))
                    speciEnPlus.append(s)
                    rep=False
                else:
                    print('la specification {} est une property'.format(s))
            else: 
                print('la specification {} est un parametre '.format(s))
        return rep

            

    def ajouterUneValeurParDefaut(self,uneSpecification):
        if uneSpecification == 'xy':
            self.ajouterUneSpecification(uneSpecification,(0,0))
        elif uneSpecification == 'width':
            self.ajouterUneSpecification(uneSpecification,1)
        elif uneSpecification == 'height':
            self.ajouterUneSpecification(uneSpecification,2)
        elif uneSpecification == 'angle':
            self.ajouterUneSpecification(uneSpecification,0)
        elif uneSpecification == 'facecolor':
            self.ajouterUneSpecification(uneSpecification,'k')
        elif uneSpecification == 'linewidth':
            self.ajouterUneSpecification(uneSpecification,1)
        else:
            raise ValueError("On n'a pas de valeur par defaut pour '{}'.".format(self.specifications[specificationAAjouter]))

    def supprimerUneSpecification(self,uneSpecification):
        del self.specifications[uneSpecification]
        
    def nettoyage(self):
        # on supprime les specification ne correspondant pas a des parametres/proprietes connus
        # on ajoute les parametres manquants
        specifi= self.specifications.keys()
        for p in self.parameters:
            if p in specifi== False:
                self.ajouterUneSpecification(p)
                
        for s in specifi:
            if s in self.parameters== False:
                if s in self.properties == False:
                    del self.specifications[s]

    
    def afficher(self):
        # on nettoye i.e. appel de la methode nettoyage
        # A partir de l'attribut specifications on cree un objet de type matplotlib.patches.Ellipse
        # on l'ajoute a l'axe courant avec la commande : plt.gca().add_patch(ellipse)
        self.nettoyage()
        ellipse = mpl.patches.Ellipse(**self.specifications)
        plt.gca().add_patch(ellipse)
            
if __name__ == "__main__":

    # deux ellipses vides et de quoi les remplir
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




















