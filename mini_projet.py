# Import de la librairie random pour la gestion du hasard#
from random import*            

#Définition de la fonction nombre_mystere correspondant à une partie#
#Retourne True (vrai) si le joueur a gagne#
#Retourne False (faux) si le joueur a perdu#
def nombre_mystere():           
    
    # Choix d'un nombre entier au hasard entre 1 et 50 #
    nbr_myst=randint(1,50)      
   
    #Boucle autorisant 7 coups#
    for i in range(1,8):        
       
        # Recuperation de la proposition du joueur#
        nb=int(input("Entrer un nombre:"))   
        
       # Le premier cas étant si nb (la proposition) est égale au nombre mystère #
        if nb==nbr_myst:
            print("Vous avez trouvé le nombre mystère",i,"coups.")
            #La fonction retourne True (vrai) pour indiquer une victoire
            return True      

        # On définit inf_ou_sup afin d'avoir le choix pour #
        # ne pas demander au joueur d'écrire la question à chaque fois #
        inf_ou_sup =int(input("Voulez vous savoir si le nombre mystère est\n1-supérieur\n2-inférieur\nau nombre choisis ?")) 
  
        # Cas supérieur ou non à nb, lorsque nous choisissons inf_ou_sup=1 # 
        if inf_ou_sup==1:
            if nb<=nbr_myst:                                            
                print("Oui, le nombre mystère est supérieur au nombre choisis.") 
            else:
                print("Non")
       
        # Cas inférieur ou non à n, lorque nous choisissons inf_ou_sup=2 #
        elif inf_ou_sup==2:
            if nb>=nbr_myst:                                             
                print("Oui, le nombre mystère est inférieur au nombre choisis.") 
            else:
                print("Non")
    
    # Si au bout de 7 coups le nombre mystère n'est pas trouvé, alors la fonction #
    # imprime cette phrase qui nous indique le nombre mystère #
    print("Le nombre mystère était",nbr_myst)  

    #La fonction retourne False pour indiquer que c'est perdu
    return False     


#Programme Principal

nb_parties = 0 #Variable contenant le nombre de partie jouée
nb_parties_gagnees = 0 #Variable comptabilisant les victoires
continuer_a_jouer = True #Variable pour gérer si le jouer souhaite continuer

#Boucle de jeu principale
while continuer_a_jouer:

    #Augmente le nb de partie de 1
    nb_parties = nb_parties + 1  
    
    #Appel de la fonction de partie
    resultat = nombre_mystere()

    #Augmente de 1 le nombre de parties gagnées si le resultat est True (vrai)
    if resultat:
        nb_parties_gagnees = nb_parties_gagnees + 1

    #Demande si le joueur souhaite continuer
    question = input("Voulez-vous continuer à jouer [O/N]?")
    if question == "O":
        continuer_a_jouer = True
    else:
        continuer_a_jouer = False

#Affichage du bilan
print("\n###########################") # le charactere \n permet de sauter une ligne
print("Vous avez gagné",nb_parties_gagnees,"partie(s) sur",nb_parties,"partie(s) jouée(s)")
print("###########################")
