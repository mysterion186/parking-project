from tkinter import *

##############################################################################################################################
# Infos en vrac                                                                                                              #
##############################################################################################################################
""" 
RAPPEL: background ne fonctionne pas sur macos d'où l'utilisation de highlightbackground => pb si on quitte la fenêtre tkinter
on aura que les bordures qui auront une couleur sinon toutes les places seront coloriées normalement 
"""
# - il faut 20 pixel d'écart selon y pour avoir de "jolie bouton"
# - il faut 55 pixel d'écart selon x pour avoir de "jolie bouton"

"""
Configuration : 
niveau 0 : 2 allées de 5 places et 4 places 
niveau 1 : 2 allées de 5 places et 4 places 
niveau 2 : 2 allées de 5 places et 4 places 
"""

##############################################################################################################################
# Déclaration des variables                                                                                                  #
##############################################################################################################################
place_occupe = 0   #nombre de place prise dans le parking
place_libre = 0    #nombre de place libre dans le parking
place_max = 0      #nombre de place maximal dans le parking

##############################################################################################################################
# Déclaration de classe                                                                                                      #
##############################################################################################################################

class Parking :
    def __init__(self,frame,name,x,y):
        global place_libre,place_max
        self.name = name #nom de la place 
        self.x = x #coordonnée x du bouton
        self.y = y #coordonnée y du bouton
        self.frame = frame #nom de le fenêtre tkinter
        #creation d'un bouton, on utilise highlightbackground à la place de background car ça ne marche pas sur macos 
        self.button = Button(self.frame,text = str(self.name),command = self.update_place,highlightbackground='green',background = 'green')
        #on met à jour le nombre de place libre et maximal à la création de chaque place de parking
        place_libre +=1 
        place_max +=1

    #ajoute le bouton crée dans la fenêtre tkinter 
    def add(self):
        self.button.place(x = self.x,y = self.y)
    
    #modifie la couleur de la place selon qu'elle est prise(red) ou non(green)
    def change_color(self):
        #on teste highlightbackground et non background à cause des pb sur macos et pour être sûr qu'il y ait un changement de couleur
        if self.button["highlightbackground"]=='red':
            self.button["highlightbackground"]= 'green'
            self.button["background"]= 'green'
        else :
            self.button["highlightbackground"]='red'
            self.button["background"]='red' 

    #met à jour le nombre de place libre/occupé dans le parking
    def update_place(self):
        global place_occupe,place_libre,place_max,place_libre

        #place de parking libre, on essaye de se garer
        if self.button["highlightbackground"]=="green" : #on regarde la couleur car elle nous indique l'état de la place (prise ou non)
            place_occupe+=1
            place_libre -=1
            print("Nombre de place Libre = {}, nombre de place occupée occupé = {}".format(place_libre,place_occupe))
            self.change_color()

        #place de parking prise, on essaye de sortir 
        elif self.button["highlightbackground"]=="red": 
            place_libre +=1
            place_occupe -=1
            print("Nombre de place Libre = {}, nombre de place occupée occupé = {}".format(place_libre,place_occupe))
            self.change_color()
        else : 
            print("Action illégal")

        #mise à jour des valeur de place libre/occupe dans le parking
        place_libre_var.set("Nombre de place dispo dans le parking : "+str(place_libre)+"/"+str(place_max))
        place_occupe_var.set("Nombre de place occupé dans le parking : "+str(place_occupe)+"/"+str(place_max))


##############################################################################################################################
# Déclaration de fonction                                                                                                    #
##############################################################################################################################

#fonction pour ajouter des boutons/places de parking dans la fenêtre tkinter
#frame = nom de la fenêtre tkinter; x/y_base = coordonnées du premier élément, allee_num = numéro de l'allée, num_max = nb de place par allée
def add_places(frame,x_base,y_base,allee_num,num_max):
    allee = Label(frame,text = f"Allé {allee_num}").place(x = x_base,y=y_base)
    for k in range(1,num_max+1):
        spot = Parking(fenetre,f"place {str(k)}",(x_base+(k-1)*55),y_base+20)
        spot.add()
    return True


##############################################################################################################################
# Partie graphique                                                                                                           #
##############################################################################################################################


#################################### initialisation de la fenêtre  ############################################################
fenetre = Tk()
#nom de la fenêtre tkinter
fenetre.title("Parking Manager")
#dimension de départ de la fenêtre tkinter
fenetre.geometry("500x500")

#################################### Initialisation des places de parking ######################################################
#coordonées y de départ, qu'on va ensuite modifier dans la boucle pour avoir les différents éléments à la bonne place
y = 50 
#on utilise une boucle pour ne pas répeter 3 fois les mêmes lignes de codes
for k in range(0,3):
    #nom du niveau k
    etage_k = Label(fenetre,text = f"Niveau n°{str(k)}") .place(x=200,y = y)
    y+=10
    #allée 1 du niveau k 
    allee_k_1 = add_places(frame=fenetre,x_base=0, y_base=y,allee_num = 1,num_max=5)
    y+=50
    #allée 2 du niveau k 
    allee_k_2 = add_places(frame=fenetre,x_base=0, y_base=y,allee_num = 2,num_max=4)
    y+=60

#################################### Initialisation des compteur de place ######################################################
place_libre_var = StringVar()
place_occupe_var = StringVar()

place_libre_var.set("Nombre de place disponible dans le parking : "+str(place_libre)+"/"+str(place_max))
place_occupe_var.set("Nombre de place occupé dans le parking     : "+str(place_occupe)+"/"+str(place_max))

place_libre_label = Label(fenetre,textvariable = place_libre_var).place(x=0,y = 0)
place_occupe_label = Label(fenetre,textvariable = place_occupe_var).place(x=0,y = 20)

#bouton pour fermer la fenêtre tkinter
fermer = Button(fenetre,text = "quitter" ,command = fenetre.quit,highlightbackground='blue',background = 'blue')
fermer.place(x=200,y=460)
fenetre.mainloop()